import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import pandas as pd
from csv_analyzer.core.data_processor import load_csv_data
from csv_analyzer.core.analysis import perform_analysis, perform_aggregation
from csv_analyzer.core.verdict_generator import generate_verdict
from threading import Thread

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("CSV Analyzer")
        self.df = None
        self.processing = False # to prevent multiple analysis runs

        self._setup_ui()

    def _setup_ui(self):
         # Load Button
        load_btn = tk.Button(self, text="Load CSV", command=self.load_csv)
        load_btn.pack(pady=10)

        # CSV options Frame
        csv_options_frame = ttk.LabelFrame(self, text="CSV Options")
        csv_options_frame.pack(padx=10, pady=5, fill=tk.X)
        
        # Delimiter Label and input
        delimiter_label = ttk.Label(csv_options_frame, text="Delimiter:")
        delimiter_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.delimiter_entry = ttk.Entry(csv_options_frame, width=5)
        self.delimiter_entry.insert(0, ',')  # Default delimiter
        self.delimiter_entry.grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)

        # Encoding Label and input
        encoding_label = ttk.Label(csv_options_frame, text="Encoding:")
        encoding_label.grid(row=0, column=2, sticky=tk.W, padx=5, pady=2)
        self.encoding_entry = ttk.Entry(csv_options_frame, width=10)
        self.encoding_entry.insert(0, 'utf-8')
        self.encoding_entry.grid(row=0, column=3, sticky=tk.W, padx=5, pady=2)


        # Main feature Dropdown
        main_label = tk.Label(self, text="Select the main feature:")
        main_label.pack(pady=5)
        self.main_dropdown = ttk.Combobox(self)
        self.main_dropdown.pack(pady=10)

        # Feature listbox
        feature_label = tk.Label(self, text="Select features for analysis (Ctrl + Click to select multiple):")
        feature_label.pack(pady=5)
        self.feature_listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)
        self.feature_listbox.pack(pady=10)
        
        # Analysis Options Frame
        analysis_options_frame = ttk.LabelFrame(self, text="Analysis Options")
        analysis_options_frame.pack(padx=10, pady=5, fill=tk.X)

        #Aggregation label and dropdown
        agg_label = ttk.Label(analysis_options_frame, text="Aggregation (optional):")
        agg_label.grid(row=0, column=0, sticky=tk.W, padx=5, pady=2)
        self.agg_dropdown = ttk.Combobox(analysis_options_frame, values=["", "mean", "median", "sum"])
        self.agg_dropdown.grid(row=0, column=1, sticky=tk.W, padx=5, pady=2)
        
        # Top N entry field
        top_n_label = ttk.Label(analysis_options_frame, text="Top N Results:")
        top_n_label.grid(row=0, column=2, sticky=tk.W, padx=5, pady=2)
        self.top_n_entry = ttk.Entry(analysis_options_frame, width=5)
        self.top_n_entry.insert(0, "5")  # Default Top N
        self.top_n_entry.grid(row=0, column=3, sticky=tk.W, padx=5, pady=2)
        
        # Analyze Button
        analyze_btn = tk.Button(self, text="Analyze", command=self._analyze_thread)
        analyze_btn.pack(pady=10)
        
        # Result Treeview
        self.result_tree = ttk.Treeview(self, show="headings", height=10)
        self.result_tree.pack(pady=10, fill=tk.BOTH, expand=True)

        # Vertical scrollbar for treeview
        tree_scroll_y = ttk.Scrollbar(self, orient="vertical", command=self.result_tree.yview)
        tree_scroll_y.pack(side=tk.RIGHT, fill=tk.Y)
        self.result_tree.configure(yscrollcommand=tree_scroll_y.set)

        # Verdict Label
        self.verdict_label = ttk.Label(self, text="Verdict: ", font=("Arial", 12, "bold"))
        self.verdict_label.pack(pady=5)
        
        # Result Text area
        self.result_text = tk.Text(self, wrap=tk.WORD, width=80, height=10)
        self.result_text.pack(pady=10)

        # Progress bar
        self.progressbar = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=300, mode='indeterminate')
        self.progressbar.pack(pady=5)
    
    def _start_progress(self):
            self.progressbar.start()
    
    def _stop_progress(self):
        self.progressbar.stop()
        self.progressbar.pack_forget()

    def _analyze_thread(self):
      if not self.processing:
        self.processing = True
        self._start_progress()
        analysis_thread = Thread(target=self.analyze)
        analysis_thread.start()


    def load_csv(self):
      try:
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if file_path:
            delimiter = self.delimiter_entry.get()
            encoding = self.encoding_entry.get()
            self.df = load_csv_data(file_path, delimiter=delimiter, encoding=encoding)
            self._populate_dropdowns(self.df.columns)
      except FileNotFoundError as e:
        self._show_error(str(e))
      except Exception as e:
        self._show_error(f"An error occured loading csv data: {e}")
        

    def _populate_dropdowns(self, columns):
      self.feature_listbox.delete(0, tk.END)
      self.main_dropdown['values'] = list(columns)
      for column in columns:
          self.feature_listbox.insert(tk.END, column)

    def analyze(self):
      try:
        if self.df is None:
          self._show_error("No CSV file loaded. Please load one first.")
          return

        selected_features = list(self.feature_listbox.curselection())
        selected_features = [self.feature_listbox.get(i) for i in selected_features]
        main_feature = self.main_dropdown.get()
        selected_features = [feature for feature in selected_features if feature]  # Filter out empty selections
        
        if not selected_features:
             self._show_error("Please select at least one feature for analysis.")
             return

        try:
          top_n = int(self.top_n_entry.get())
        except ValueError:
           self._show_error("Top N must be a valid integer.")
           return
        
        agg_type = self.agg_dropdown.get()
        
        if agg_type:
          result = perform_aggregation(self.df, main_feature, selected_features, top_n, agg_type)
        else:
          result = perform_analysis(self.df, main_feature, selected_features, top_n)

        verdict = generate_verdict(result)

        # Clear previous results
        self.result_text.delete(1.0, tk.END)
        self._populate_treeview(result)
        # Update the verdict label
        self.verdict_label.config(text="Verdict: " + verdict)
      except KeyError as e:
         self._show_error(f"Selected column '{e}' not found in dataframe columns")
      except Exception as e:
          self._show_error(f"An error occurred during analysis: {e}")
      finally:
         self.processing = False
         self._stop_progress()


    def _populate_treeview(self, df):
        #Clear previous data from tree
        for item in self.result_tree.get_children():
          self.result_tree.delete(item)

        if df.empty:
           return
        
        self.result_tree["columns"] = list(df.columns)

        for col in df.columns:
            self.result_tree.heading(col, text=col)
            self.result_tree.column(col, width=100)

        for index, row in df.iterrows():
            self.result_tree.insert("", tk.END, values=list(row))
        
    def _show_error(self, message):
      self.result_text.delete(1.0, tk.END)
      self.result_text.insert(tk.END, f"Error: {message}\n")

if __name__ == '__main__':
    app = MainWindow()
    app.mainloop()