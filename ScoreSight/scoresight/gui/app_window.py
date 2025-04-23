# scoresight/gui/app_window.py
import customtkinter as ctk
from tkinter import filedialog, messagebox
import os
import pandas as pd
import sys # For checking if running executable
import traceback # For detailed error logging
import subprocess # For potentially opening report directory

# --- Matplotlib Integration ---
import matplotlib
matplotlib.use('TkAgg') # Set backend BEFORE importing pyplot
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# --- ScoreSight Modules ---
# Use try-except for imports to handle potential issues when packaged
try:
    from ..analysis import analyzer
    from ..analysis import plotter
    from ..reporting import generator
except ImportError:
    print("Relative import failed, attempting direct import (may work if run from root)...")
    try:
        from analysis import analyzer
        from analysis import plotter
        from reporting import generator
    except ImportError as e:
        print(f"Direct import also failed: {e}")
        messagebox.showerror("Import Error", "Could not load application modules (analysis, plotter, reporting). Ensure the project structure is correct and accessible.")
        sys.exit(1)


class AppWindow(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("ScoreSight - Student Result Analyzer")
        self.geometry("1150x720") # Adjusted size
        self.minsize(900, 600)

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.data_frame = None # Processed DataFrame for analysis
        self.original_data_frame = None # Raw loaded DataFrame
        self.analysis_results = {} # Dict from analyzer
        self.plots = {} # Dict of generated Figure objects {plot_name: fig}

        # --- Configure grid layout ---
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- Sidebar Frame ---
        self.sidebar_frame = ctk.CTkFrame(self, width=220, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1) # Push elements towards top

        # Sidebar Widgets
        self.logo_label = ctk.CTkLabel(self.sidebar_frame, text="ScoreSight", font=ctk.CTkFont(size=22, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

        self.load_button = ctk.CTkButton(self.sidebar_frame, text="Load Data File", command=self.load_file)
        self.load_button.grid(row=1, column=0, padx=20, pady=10, sticky="ew")

        self.analyze_button = ctk.CTkButton(self.sidebar_frame, text="Run Analysis", state="disabled", command=self.run_analysis)
        self.analyze_button.grid(row=2, column=0, padx=20, pady=10, sticky="ew")

        self.report_button = ctk.CTkButton(self.sidebar_frame, text="Generate PDF Report", state="disabled", command=self.generate_report)
        self.report_button.grid(row=3, column=0, padx=20, pady=10, sticky="ew")

        self.appearance_mode_label = ctk.CTkLabel(self.sidebar_frame, text="Theme:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(20, 0), sticky="ew")
        self.appearance_mode_optionmenu = ctk.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"], command=self.change_appearance_mode)
        self.appearance_mode_optionmenu.grid(row=6, column=0, padx=20, pady=(5, 20), sticky="ew")
        self.appearance_mode_optionmenu.set(ctk.get_appearance_mode())

        # --- Main Content Frame ---
        self.main_frame = ctk.CTkFrame(self, corner_radius=5, fg_color="transparent")
        self.main_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(1, weight=1)

        self.status_label = ctk.CTkLabel(self.main_frame, text="Welcome to ScoreSight! Please load a student data file (.csv or .xlsx).", font=ctk.CTkFont(size=14), anchor="w")
        self.status_label.grid(row=0, column=0, padx=10, pady=(5, 10), sticky="ew")

        # --- Tab View ---
        self.tab_view = ctk.CTkTabview(self.main_frame, corner_radius=6)
        self.tab_view.grid(row=1, column=0, padx=10, pady=(0, 10), sticky="nsew")

        tab_names = ["Summary", "Subject Details", "Graphs", "Data Preview"]
        for name in tab_names:
            self.tab_view.add(name)
            self.tab_view.tab(name).grid_columnconfigure(0, weight=1)
            self.tab_view.tab(name).grid_rowconfigure(0, weight=1)

        # --- Tab Contents ---
        self.summary_textbox = ctk.CTkTextbox(self.tab_view.tab("Summary"), state="disabled", wrap="word", corner_radius=5, font=("Arial", 12))
        self.summary_textbox.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.subjects_textbox = ctk.CTkTextbox(self.tab_view.tab("Subject Details"), state="disabled", wrap="word", corner_radius=5, font=("Arial", 12))
        self.subjects_textbox.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self.graphs_frame = ctk.CTkScrollableFrame(self.tab_view.tab("Graphs"), corner_radius=5, label_text="Result Visualizations")
        self.graphs_frame.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
        self.graphs_frame.grid_columnconfigure(0, weight=1)

        self.preview_textbox = ctk.CTkTextbox(self.tab_view.tab("Data Preview"), state="disabled", wrap="none", corner_radius=5, font=("Consolas", 10))
        self.preview_textbox.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

        self._create_placeholder_graph_label() # Initial placeholder

    # --- Helper Methods ---
    def _create_placeholder_graph_label(self, text="Graphs will appear here after analysis."):
         """Creates or updates the placeholder label in the Graphs tab."""
         # Ensure previous placeholder/widgets are gone
         for widget in self.graphs_frame.winfo_children():
               widget.destroy()
         # Create and grid the label
         placeholder_label = ctk.CTkLabel(self.graphs_frame, text=text, text_color="gray")
         placeholder_label.grid(row=0, column=0, padx=20, pady=40, sticky="")

    def _update_status(self, message: str):
         """Updates the status label."""
         self.status_label.configure(text=message)
         self.update_idletasks() # Force immediate update

    # --- Core Functionality Methods ---
    def change_appearance_mode(self, new_mode: str):
        """Changes the application's appearance mode and redraws plots."""
        ctk.set_appearance_mode(new_mode)
        # If analysis results exist, regenerate plots with the new theme
        if self.analysis_results and not self.analysis_results.get('error') and self.data_frame is not None:
             self._update_status(f"Applying {new_mode} theme and redrawing plots...")
             self.generate_and_display_plots()
             self._update_status(f"{new_mode} theme applied.")
        else:
            self._update_status(f"{new_mode} theme applied.")

    def load_file(self):
        """Opens a file dialog to select a CSV/Excel file and loads it using pandas."""
        # (This method remains unchanged from the previous version)
        file_path = filedialog.askopenfilename(
            title="Select Student Data File",
            filetypes=(("Excel files", "*.xlsx"), ("CSV files", "*.csv"), ("All files", "*.*"))
        )
        if not file_path: self._update_status("File loading cancelled."); return

        file_name = os.path.basename(file_path)
        self._update_status(f"Loading {file_name}...")

        try:
            if file_path.lower().endswith('.csv'): df_loaded = pd.read_csv(file_path)
            elif file_path.lower().endswith('.xlsx'): df_loaded = pd.read_excel(file_path, engine='openpyxl')
            else: messagebox.showerror("Error", "Unsupported file type."); self._update_status("Unsupported file type."); return

            self.original_data_frame = df_loaded.copy()

            if df_loaded.empty: messagebox.showerror("Error", "File is empty."); self._update_status("Error: File is empty."); return
            if len(df_loaded.columns) < 2: messagebox.showerror("Error", "File needs identifier & at least one subject column."); self._update_status("Error: Insufficient columns."); return

            identifier_col = df_loaded.columns[0]
            potential_subject_cols = df_loaded.columns[1:]
            numeric_cols = []; df_processed = df_loaded.copy()

            for col in potential_subject_cols:
                try:
                    df_processed[col] = pd.to_numeric(df_processed[col], errors='coerce')
                    if not df_processed[col].isnull().all(): numeric_cols.append(col)
                except Exception as e: print(f"Could not process column {col} as numeric: {e}")

            if not numeric_cols:
                messagebox.showerror("Error", "No valid numeric columns found for marks."); self._update_status("Error: No numeric mark columns found."); self.data_frame = None; return

            self.data_frame = df_processed[[identifier_col] + numeric_cols]

            dropped_cols = set(potential_subject_cols) - set(numeric_cols)
            if dropped_cols: messagebox.showwarning("Column Warning", f"Ignored non-numeric columns:\n{', '.join(dropped_cols)}")

            self._update_status(f"Loaded & Prepared: {file_name} ({len(self.data_frame)} rows, {len(numeric_cols)} subjects)")
            self.analyze_button.configure(state="normal"); self.report_button.configure(state="disabled")
            self.display_data_preview(); self.clear_results()

        except ImportError as imp_err:
             if 'openpyxl' in str(imp_err): messagebox.showerror("Missing Library", "Reading .xlsx files requires 'openpyxl'.\nInstall it: pip install openpyxl"); self._update_status("Error: Missing 'openpyxl'.")
             else: messagebox.showerror("Import Error", f"Missing library: {imp_err}"); self._update_status("Error: Missing library.")
             self.data_frame = None
        except FileNotFoundError: messagebox.showerror("File Not Found", f"Could not find file:\n{file_path}"); self._update_status("Error: File not found."); self.data_frame = None
        except Exception as e: messagebox.showerror("Error Loading File", f"Error loading/processing file:\n{e}"); self._update_status("Error loading/processing file."); self.data_frame = None; traceback.print_exc()
        finally:
            if self.data_frame is None: self.analyze_button.configure(state="disabled"); self.report_button.configure(state="disabled"); self.clear_results(); self.clear_preview()

    def display_data_preview(self):
        """Displays the head of the loaded and processed DataFrame."""
        # (This method remains unchanged)
        self.clear_preview()
        if self.data_frame is not None:
            self.preview_textbox.configure(state="normal")
            try: preview_text = self.data_frame.head(30).to_string(); self.preview_textbox.insert("1.0", preview_text)
            except Exception as e: self.preview_textbox.insert("1.0", f"Error generating data preview:\n{e}")
            finally: self.preview_textbox.configure(state="disabled")
            self.tab_view.set("Data Preview")

    def clear_preview(self):
         """Clears the data preview text box."""
         # (This method remains unchanged)
         if hasattr(self, 'preview_textbox'):
             try: self.preview_textbox.configure(state="normal"); self.preview_textbox.delete("1.0", "end"); self.preview_textbox.configure(state="disabled")
             except Exception: pass

    def clear_results(self):
        """Clears all analysis result displays (text boxes and graphs)."""
        # (This method remains unchanged)
        textboxes = [self.summary_textbox, self.subjects_textbox]
        for tb in textboxes:
             if hasattr(self, tb.winfo_name()):
                 try: tb.configure(state="normal"); tb.delete("1.0", "end"); tb.configure(state="disabled")
                 except Exception: pass
        if hasattr(self, 'graphs_frame'):
            for widget in self.graphs_frame.winfo_children(): widget.destroy()
        self._create_placeholder_graph_label()
        if hasattr(self, 'plots'):
            for fig in self.plots.values():
                 if fig is not None: plt.close(fig)
        self.plots = {}
        self.analysis_results = {}

    def run_analysis(self):
        """Triggers data analysis, displays text results, and generates plots."""
        # (This method remains unchanged)
        if self.data_frame is None: messagebox.showwarning("No Data", "Please load a data file first."); return

        self._update_status("Analyzing data... Please wait.")
        self.clear_results()

        try:
            self.analysis_results = analyzer.analyze_data(self.data_frame)
            analysis_error = self.analysis_results.get('error')
            if analysis_error:
                messagebox.showerror("Analysis Error", f"Failed to complete analysis:\n{analysis_error}")
                self._update_status("Analysis Failed.")
                self.report_button.configure(state="disabled")
                self.display_summary(); self.display_subject_details() # Show partial results
                self._create_placeholder_graph_label("Analysis failed, plots cannot be generated.")
                return

            self.display_summary(); self.display_subject_details() # Display text results first

            self._update_status("Analysis complete. Generating plots...")
            plot_success = self.generate_and_display_plots()

            if plot_success: self._update_status("Analysis & Plotting Complete.")
            else: self._update_status("Analysis complete, but plot generation failed/incomplete.")
            self.report_button.configure(state="normal") # Enable report even if plots fail
            self.tab_view.set("Summary") # Go back to summary after run

        except Exception as e:
            messagebox.showerror("Unexpected Error", f"An unexpected error occurred during analysis/plotting:\n{e}")
            self._update_status("Analysis/Plotting Failed Unexpectedly.")
            self.report_button.configure(state="disabled")
            self._create_placeholder_graph_label("Error occurred, plots cannot be generated.")
            traceback.print_exc()

    def display_summary(self):
        """Formats and displays the summary results, including overall failing students."""
        # (This method remains unchanged from the previous version)
        if not hasattr(self, 'summary_textbox'): return
        self.summary_textbox.configure(state="normal")
        self.summary_textbox.delete("1.0", "end")
        if not self.analysis_results: self.summary_textbox.insert("1.0", "No analysis results available."); self.summary_textbox.configure(state="disabled"); return
        num_students = self.analysis_results.get('num_students', 'N/A'); subjects = self.analysis_results.get('subject_names', []); identifier_col = self.analysis_results.get('identifier_col', 'Identifier')
        summary_text = f"Overall Analysis Summary:\n=========================\n\n"; summary_text += f"Total Students Processed: {num_students}\nIdentifier Column: '{identifier_col}'\n"; summary_text += f"Subjects Found ({len(subjects)}): {', '.join(subjects) if subjects else 'None'}\n\n"
        overall_toppers = self.analysis_results.get('overall_topper', []); total_possible = self.analysis_results.get('total_possible_marks', None)
        summary_text += "Overall Topper(s):\n------------------\n"
        if overall_toppers:
            for topper in overall_toppers: name = topper.get('name', 'N/A'); total_marks = topper.get('total_marks', 'N/A'); summary_text += f"- Name: {name}\n  Total Marks: {total_marks}";
            if 'percentage' in topper: summary_text += f" ({topper['percentage']}%)"
            elif total_possible and isinstance(total_marks, (int, float)) and total_possible > 0:
                     try: percentage = round((float(total_marks) / total_possible) * 100, 2); summary_text += f" ({percentage}%)"
                     except: pass
            summary_text += "\n"
            if total_possible: summary_text += f"\n(Based on a maximum possible score of {total_possible})\n"
        elif self.analysis_results.get('error') and "No students with valid scores" in self.analysis_results['error']: summary_text += "(Could not determine: requires valid scores in all subjects)\n"
        else: summary_text += "(None found or data insufficient)\n"
        summary_text += "\n\n"
        failing_students = self.analysis_results.get('failing_students', [])
        summary_text += "Students Below 40% Overall:\n---------------------------\n"
        if failing_students:
            summary_text += f"(Found {len(failing_students)} students)\n"
            for i, student in enumerate(failing_students): name = student.get('name', 'N/A'); percentage = student.get('percentage', 'N/A'); summary_text += f"- {name} ({percentage}%)\n"
        else:
            total_marks_series = self.analysis_results.get('total_marks_series', None)
            if total_marks_series is not None and total_marks_series.dropna().empty and self.analysis_results.get('num_students', 0) > 0 : summary_text += "(Cannot determine: No students had valid scores in all subjects)\n"
            else: summary_text += "(None - All students with complete scores are >= 40%)\n"
        self.summary_textbox.insert("1.0", summary_text)
        self.summary_textbox.configure(state="disabled")


    def display_subject_details(self):
        """Formats and displays subject-wise statistics, toppers, and fail count."""
        # <<< THIS METHOD IS UPDATED >>>
        if not hasattr(self, 'subjects_textbox'): return
        self.subjects_textbox.configure(state="normal")
        self.subjects_textbox.delete("1.0", "end")

        if not self.analysis_results:
             self.subjects_textbox.insert("1.0", "No analysis results available.")
             self.subjects_textbox.configure(state="disabled")
             return

        subjects = self.analysis_results.get('subject_names', [])
        subject_stats = self.analysis_results.get('subject_stats', {})
        subject_toppers = self.analysis_results.get('subject_toppers', {})

        details_text = "Subject-Wise Details:\n"
        details_text += "=====================\n\n"

        if not subjects:
            details_text += "No subjects found or analyzed.\n"
        else:
            # Define alignment width (adjust as needed)
            label_width = 12
            value_width = 8

            for subject in subjects:
                details_text += f"--- {subject} ---\n"

                # Statistics
                stats = subject_stats.get(subject, {})
                details_text += "  Statistics:\n"
                count = stats.get('count', 0)
                fail_count = stats.get('fail_count', 'N/A') # Get fail count

                # Format stats with alignment
                details_text += f"    {'Count:':<{label_width}}{str(count if count >= 0 else 'N/A'):>{value_width}}\n"
                details_text += f"    {'Fail (< 40):':<{label_width}}{str(fail_count):>{value_width}}\n" # Display fail count
                details_text += f"    {'Average:':<{label_width}}{str(stats.get('mean', 'N/A')):>{value_width}}\n"
                details_text += f"    {'Median:':<{label_width}}{str(stats.get('median', 'N/A')):>{value_width}}\n"
                details_text += f"    {'Highest:':<{label_width}}{str(stats.get('max', 'N/A')):>{value_width}}\n"
                details_text += f"    {'Lowest:':<{label_width}}{str(stats.get('min', 'N/A')):>{value_width}}\n"
                details_text += f"    {'Std Dev:':<{label_width}}{str(stats.get('std_dev', 'N/A')):>{value_width}}\n"


                # Subject Topper(s)
                toppers = subject_toppers.get(subject, [])
                details_text += "  Topper(s):\n"
                if toppers:
                    for topper in toppers:
                        name = topper.get('name', 'N/A'); score = topper.get('score', 'N/A')
                        details_text += f"    - {name} ({score})\n"
                elif count == 0:
                    details_text += "    (No valid scores found)\n"
                else:
                    details_text += "    (No topper data)\n" # Or "(Could not determine)"

                details_text += "\n" # Add space between subjects

        self.subjects_textbox.insert("1.0", details_text)
        self.subjects_textbox.configure(state="disabled")
        # <<< END OF UPDATED METHOD >>>


    def generate_and_display_plots(self) -> bool:
        """Generates plots using the plotter module and embeds them in the Graphs tab. Returns True on success, False otherwise."""
        # (This method remains unchanged)
        if not hasattr(self, 'graphs_frame'): return False
        for widget in self.graphs_frame.winfo_children(): widget.destroy()
        for fig in self.plots.values():
             if fig is not None: plt.close(fig)
        self.plots = {}
        plots_generated_successfully = 0; total_plots_attempted = 0
        if self.data_frame is None or not self.analysis_results: self._create_placeholder_graph_label("Cannot generate plots: Missing data or analysis results."); return False
        df = self.data_frame; results = self.analysis_results; subjects = results.get('subject_names', []); stats = results.get('subject_stats', {}); total_marks = results.get('total_marks_series', None); total_possible = results.get('total_possible_marks', None)
        appearance_mode = ctk.get_appearance_mode(); plot_theme = 'dark' if appearance_mode == "Dark" else 'light'
        plot_row = 0

        def embed_plot(fig, name):
            nonlocal plot_row, plots_generated_successfully
            if fig:
                 self.plots[name] = fig
                 try: canvas = FigureCanvasTkAgg(fig, master=self.graphs_frame); canvas_widget = canvas.get_tk_widget(); canvas_widget.grid(row=plot_row, column=0, padx=10, pady=15, sticky="ew"); canvas.draw(); plot_row += 1; plots_generated_successfully += 1
                 except Exception as embed_err: print(f"Error embedding plot '{name}': {embed_err}"); traceback.print_exc(); error_label = ctk.CTkLabel(self.graphs_frame, text=f"Error embedding plot: {name}", text_color="orange"); error_label.grid(row=plot_row, column=0, padx=10, pady=5, sticky="w"); plot_row += 1; plt.close(fig); self.plots.pop(name, None)
            else: fail_label = ctk.CTkLabel(self.graphs_frame, text=f"Could not generate plot: {name}", text_color="gray"); fail_label.grid(row=plot_row, column=0, padx=10, pady=5, sticky="w"); plot_row += 1

        total_plots_attempted += 1
        try: fig_avg = plotter.plot_average_marks_per_subject(stats, theme=plot_theme); embed_plot(fig_avg, 'average_marks')
        except Exception as e: print(f"EXCEPTION during plot_average_marks call: {e}"); traceback.print_exc(); embed_plot(None, 'average_marks')
        total_plots_attempted += 1
        if total_marks is not None and not total_marks.dropna().empty:
            try: fig_overall = plotter.plot_overall_score_distribution(total_marks, total_possible_marks=total_possible, theme=plot_theme); embed_plot(fig_overall, 'overall_distribution')
            except Exception as e: print(f"EXCEPTION during plot_overall_score call: {e}"); traceback.print_exc(); embed_plot(None, 'overall_distribution')
        else: skip_label = ctk.CTkLabel(self.graphs_frame, text="Overall Distribution plot skipped (Insufficient Data).", text_color="gray"); skip_label.grid(row=plot_row, column=0, padx=10, pady=5, sticky="w"); plot_row += 1
        if subjects:
             separator_label = ctk.CTkLabel(self.graphs_frame, text="Subject Distributions:", font=ctk.CTkFont(weight="bold")); separator_label.grid(row=plot_row, column=0, padx=10, pady=(20, 5), sticky="w"); plot_row += 1
             for subject in subjects: 
                total_plots_attempted += 1; plot_name = f'distribution_{subject.replace(" ", "_").lower()}'; 
                try: fig_subj = plotter.plot_subject_distribution(df, subject, theme=plot_theme); embed_plot(fig_subj, plot_name)
                except Exception as e: print(f"EXCEPTION during plot_subject_distribution call for {subject}: {e}"); traceback.print_exc(); embed_plot(None, plot_name)

        if plot_row == 0: self._create_placeholder_graph_label("No plots could be generated."); return False
        elif plots_generated_successfully == 0: self._create_placeholder_graph_label("Plot generation failed for all graphs."); return False
        print(f"Plot generation finished. {plots_generated_successfully}/{total_plots_attempted} plots successfully embedded.")
        self.tab_view.set("Graphs")
        return True


    def generate_report(self):
        """Generates and saves a PDF report using the reporting module."""
        # (This method remains unchanged)
        if not self.analysis_results or self.analysis_results.get('error'): messagebox.showwarning("Analysis Incomplete", "Please run the analysis successfully first."); return
        if not self.plots:
             if not messagebox.askyesno("No Plots Found", "No plots were generated or stored.\nGenerate report without plots?"): self._update_status("Report generation cancelled (no plots)."); return
             else: print("Proceeding with report generation without plots.")
        save_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf"), ("All files", "*.*")], title="Save PDF Report As", initialdir="reports", initialfile="ScoreSight_Analysis_Report.pdf")
        if not save_path: self._update_status("Report generation cancelled."); return
        report_dir = os.path.dirname(save_path)
        if not os.path.exists(report_dir):
             try: os.makedirs(report_dir)
             except OSError as e: messagebox.showerror("Directory Error", f"Could not create reports directory:\n{report_dir}\nError: {e}"); self._update_status("Report generation failed (directory error)."); return
        self._update_status(f"Generating PDF report... Please wait.")
        try:
            success = generator.create_pdf_report(analysis_results=self.analysis_results, plots=self.plots, output_filename=save_path)
            if success: messagebox.showinfo("Success", f"PDF Report saved successfully to:\n{save_path}"); self._update_status("Report Generated Successfully.")
                # Optional: open directory
            else: messagebox.showerror("Error", "Failed to generate PDF report. See console/logs."); self._update_status("Report Generation Failed.")
        except ImportError as imp_err:
             if 'reportlab' in str(imp_err): messagebox.showerror("Missing Library", "Report generation requires 'reportlab'.\nInstall it: pip install reportlab"); self._update_status("Report Gen Failed (Missing 'reportlab').")
             else: messagebox.showerror("Import Error", f"Report gen failed: {imp_err}"); self._update_status("Report Gen Failed (Import Error).")
        except Exception as e: messagebox.showerror("Report Error", f"Unexpected error during report generation:\n{e}"); self._update_status("Report Gen Failed (Unexpected Error)."); traceback.print_exc()