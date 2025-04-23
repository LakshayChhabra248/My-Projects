# scoresight/reporting/generator.py

import io
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, PageBreak, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
from reportlab.lib.units import inch, cm
from reportlab.lib import colors
import matplotlib.pyplot as plt # Keep import for type hint and potentially closing figs if needed
import pandas as pd # Keep import for type hint if needed
from datetime import datetime
import traceback # For detailed error logging

# --- Helper to save Matplotlib Figure to BytesIO ---
def save_plot_to_bytes(figure: plt.Figure) -> io.BytesIO | None:
    """Saves a Matplotlib figure to a BytesIO buffer."""
    if figure is None: return None
    try: buf = io.BytesIO(); figure.savefig(buf, format='png', dpi=150, bbox_inches='tight'); buf.seek(0); return buf
    except Exception as e: print(f"Error saving plot to bytes: {e}"); return None

# --- Report Generation Function ---
def create_pdf_report(analysis_results: dict, plots: dict, output_filename: str):
    """
    Generates a PDF report summarizing the analysis results and including plots.
    """
    try:
        doc = SimpleDocTemplate(output_filename, pagesize=(8.5*inch, 11*inch), leftMargin=0.75*inch, rightMargin=0.75*inch, topMargin=0.75*inch, bottomMargin=0.75*inch)
        styles = getSampleStyleSheet(); story = []

        # --- Define Custom Styles ---
        title_style = ParagraphStyle(name='TitleStyle', parent=styles['h1'], alignment=TA_CENTER, fontSize=18, spaceAfter=0.2*inch)
        heading_style = ParagraphStyle(name='HeadingStyle', parent=styles['h2'], fontSize=14, spaceAfter=0.15*inch, spaceBefore=0.1*inch)
        subheading_style = ParagraphStyle(name='SubHeadingStyle', parent=styles['h3'], fontSize=11, spaceAfter=0.1*inch, spaceBefore=0.1*inch, textColor=colors.darkslateblue)
        normal_style = styles['Normal']; normal_style.spaceAfter = 6

        # --- Report Header ---
        story.append(Paragraph("ScoreSight Analysis Report", title_style)); story.append(Paragraph(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", styles['Normal'])); story.append(Spacer(1, 0.3*inch))

        # --- Analysis Summary Section ---
        story.append(Paragraph("Overall Summary", heading_style))
        num_students = analysis_results.get('num_students', 'N/A'); subjects = analysis_results.get('subject_names', []); identifier_col = analysis_results.get('identifier_col', 'N/A'); total_possible = analysis_results.get('total_possible_marks', None)
        summary_data = [['Total Students Processed:', str(num_students)], ['Identifier Column:', f"'{identifier_col}'"], ['Subjects Found:', f"{len(subjects)} ({', '.join(subjects) if subjects else 'None'})"]]
        summary_table = Table(summary_data, colWidths=[2*inch, 5*inch]); summary_table.setStyle(TableStyle([('ALIGN', (0,0), (-1,-1), 'LEFT'), ('FONTNAME', (0,0), (0,-1), 'Helvetica-Bold'), ('BOTTOMPADDING', (0,0), (-1,-1), 6), ('TOPPADDING', (0,0), (-1,-1), 6), ('VALIGN', (0, 0), (-1, -1), 'TOP')])); story.append(summary_table); story.append(Spacer(1, 0.1*inch))
        overall_toppers = analysis_results.get('overall_topper', [])
        story.append(Paragraph("Overall Topper(s):", subheading_style))
        if overall_toppers:
            topper_text = ""
            for topper in overall_toppers: 
                name = topper.get('name', 'N/A'); total_marks = topper.get('total_marks', 'N/A'); topper_text += f"- {name} (Total: {total_marks}"
                if 'percentage' in topper: topper_text += f", {topper['percentage']}%)<br/>"
                elif total_possible and isinstance(total_marks, (int, float)) and total_possible > 0:
                    try: percentage = round((float(total_marks) / total_possible) * 100, 2); topper_text += f", {percentage}%)<br/>"
                    except: topper_text += ")<br/>"
                else: topper_text += ")<br/>"
            if total_possible: topper_text += f"<br/>(Max Possible Total Score: {total_possible})"
            story.append(Paragraph(topper_text, normal_style))
        else: story.append(Paragraph("No overall topper identified (may require valid scores in all subjects).", normal_style))
        story.append(Spacer(1, 0.2*inch))

        # --- Failing Students Section ---
        failing_students = analysis_results.get('failing_students', [])
        story.append(Paragraph("Students Below 40% Overall:", subheading_style))
        if failing_students:
            fail_text = f"Total Count: {len(failing_students)}<br/><br/>"; limit = 100
            for i, student in enumerate(failing_students):
                if i >= limit: fail_text += f"... and {len(failing_students) - limit} more.<br/>"; break
                name = student.get('name', 'N/A'); percentage = student.get('percentage', 'N/A'); fail_text += f"- {name} ({percentage}%)<br/>"
            story.append(Paragraph(fail_text, normal_style))
        else:
            total_marks_series = analysis_results.get('total_marks_series', None); num_students_processed = analysis_results.get('num_students', 0)
            if total_marks_series is not None and total_marks_series.dropna().empty and num_students_processed > 0: story.append(Paragraph("(Cannot determine: No students had valid scores in all subjects)", normal_style))
            else: story.append(Paragraph("(None - All students with complete scores scored 40% or above)", normal_style))
        story.append(Spacer(1, 0.2*inch))

        # --- Subject Details Section --- <<< THIS SECTION IS UPDATED >>>
        story.append(PageBreak())
        story.append(Paragraph("Subject-Wise Details", heading_style))
        subject_stats = analysis_results.get('subject_stats', {})
        subject_toppers = analysis_results.get('subject_toppers', {})
        # subjects list was already retrieved earlier for the summary

        if not subjects: story.append(Paragraph("No subject data available.", normal_style))
        else:
            for subject in subjects:
                story.append(Paragraph(f"--- {subject} ---", subheading_style))
                # Stats Table
                stats = subject_stats.get(subject, {})
                # Add 'Fail Count (< 40)' row to stats_data
                stats_data = [
                    ['Statistic', 'Value'],
                    ['Count', str(stats.get('count', 'N/A'))],
                    ['Fail Count (< 40)', str(stats.get('fail_count', 'N/A'))], # Added Fail Count
                    ['Average', str(stats.get('mean', 'N/A'))],
                    ['Median', str(stats.get('median', 'N/A'))],
                    ['Highest', str(stats.get('max', 'N/A'))],
                    ['Lowest', str(stats.get('min', 'N/A'))],
                    ['Std. Dev.', str(stats.get('std_dev', 'N/A'))],
                ]
                stats_table = Table(stats_data, colWidths=[1.8*inch, 1.5*inch]) # Adjusted width slightly
                stats_table.setStyle(TableStyle([
                    ('ALIGN', (0,0), (-1,-1), 'LEFT'),
                    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'), # Header bold
                    ('FONTNAME', (0,1), (0,-1), 'Helvetica-Bold'), # Labels bold
                    ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
                    ('BACKGROUND', (0,0), (-1,0), colors.lightgrey), # Header background
                    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
                    ('TOPPADDING', (0,0), (-1,-1), 4),
                    ('VALIGN', (0,0), (-1,-1), 'TOP')
                ]))
                story.append(stats_table)
                story.append(Spacer(1, 0.1*inch))
                # Toppers List
                toppers = subject_toppers.get(subject, []); story.append(Paragraph("<b>Topper(s):</b>", normal_style))
                if toppers:
                    topper_list_text = ""
                    for topper in toppers: topper_list_text += f"- {topper.get('name', 'N/A')} ({topper.get('score', 'N/A')})<br/>"
                    story.append(Paragraph(topper_list_text, normal_style))
                elif stats.get('count', 0) == 0: story.append(Paragraph("(No valid scores found)", normal_style))
                else: story.append(Paragraph("(No topper data)", normal_style))
                story.append(Spacer(1, 0.2*inch)) # Space between subjects
        # <<< END OF UPDATED SECTION >>>

        # --- Graphs Section ---
        story.append(PageBreak()); story.append(Paragraph("Result Visualizations", heading_style))
        if not plots: story.append(Paragraph("No plots were generated or available.", normal_style))
        else:
            available_width_pts = 7 * inch; available_height_pts = 9 * inch
            plot_order = ['average_marks', 'overall_distribution']; plot_order.extend(sorted([k for k in plots.keys() if k.startswith('distribution_')]))
            for plot_name in plot_order:
                fig = plots.get(plot_name)
                if fig:
                    if plot_name == 'average_marks': plot_title = "Average Marks per Subject"
                    elif plot_name == 'overall_distribution': plot_title = "Overall Score Distribution"
                    elif plot_name.startswith('distribution_'): subj_name = plot_name.replace('distribution_', '').replace('_', ' ').title(); plot_title = f"Distribution for {subj_name}"
                    else: plot_title = plot_name.replace('_', ' ').title()
                    story.append(Paragraph(f"{plot_title}:", subheading_style))
                    img_buffer = save_plot_to_bytes(fig)
                    if img_buffer:
                        try:
                            img = Image(img_buffer); img_width_pts = img.imageWidth; img_height_pts = img.imageHeight
                            if img_width_pts <= 0 or img_height_pts <= 0: print(f"Warning: Invalid dimensions for plot {plot_name}. Skipping."); continue
                            scale_w = available_width_pts / img_width_pts; scale_h = available_height_pts / img_height_pts; scale = min(scale_w, scale_h, 1.0)
                            img.drawWidth = img_width_pts * scale; img.drawHeight = img_height_pts * scale
                            story.append(img); story.append(Spacer(1, 0.2 * inch))
                        except Exception as img_err: print(f"Error processing/adding image {plot_name}: {img_err}"); story.append(Paragraph(f"(Error embedding plot: {plot_name} - {img_err})", normal_style))
                    else: story.append(Paragraph(f"(Could not save plot data to buffer: {plot_name})", normal_style))
                else: story.append(Paragraph(f"(Invalid or missing plot data for: {plot_name})", normal_style))

        # --- Build the PDF ---
        doc.build(story)
        print(f"PDF report generated successfully: {output_filename}")
        return True

    except Exception as e:
        print(f"FATAL Error during PDF report generation: {e}")
        traceback.print_exc()
        return False