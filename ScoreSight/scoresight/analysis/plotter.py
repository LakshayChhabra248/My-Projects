# scoresight/analysis/plotter.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import io # Needed for saving plot to memory

def plot_subject_distribution(df: pd.DataFrame, subject: str, identifier_col: str = None, theme: str = 'dark') -> plt.Figure | None:
    """
    Generates a histogram and KDE plot for the distribution of marks in a specific subject.

    Args:
        df: The pandas DataFrame containing student data.
        subject: The name of the subject column to plot.
        identifier_col: Name of the identifier column (optional, used to drop before plotting).
        theme: 'light' or 'dark' to adjust plot style.

    Returns:
        A matplotlib Figure object containing the plot, or None if the subject is invalid.
    """
    if df is None or subject not in df.columns:
        print(f"Error: Subject '{subject}' not found in DataFrame for plotting.")
        return None

    # Create a copy to avoid modifying original DataFrame
    plot_df = df.copy()

    # Convert subject column to numeric, coercing errors. Plotting functions usually handle NaNs.
    plot_df[subject] = pd.to_numeric(plot_df[subject], errors='coerce')
    valid_scores = plot_df[subject].dropna()

    if valid_scores.empty:
        print(f"No valid numeric data to plot for subject '{subject}'.")
        # Optionally return a figure with just text indicating no data
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.text(0.5, 0.5, f"No valid data for\n{subject}", ha='center', va='center', fontsize=12)
        ax.set_title(f"Distribution for {subject}")
        ax.axis('off') # Hide axes
        return fig # Return the figure with the message

    # Set plot style based on theme
    if theme == 'dark':
        plt.style.use('dark_background')
        # sns.set_theme(style="darkgrid") # Alternative seaborn theme setting
    else:
        plt.style.use('ggplot') # Or another light theme
        # sns.set_theme(style="whitegrid")

    fig, ax = plt.subplots(figsize=(7, 5)) # Create a figure and an axes object

    # Determine appropriate bins, e.g., using Freedman-Diaconis rule or simply Sturges' rule / fixed number
    # Let's use a reasonable fixed number or range-based for simplicity here
    min_score = valid_scores.min()
    max_score = valid_scores.max()
    if pd.isna(min_score) or pd.isna(max_score) or min_score == max_score:
         num_bins = 5 # Default if range is zero or invalid
    else:
         # Aim for bins roughly 5-10 marks wide, but at least 5 bins, max 20
         num_bins = max(5, min(20, int((max_score - min_score) / 7) + 1))


    # Plot histogram using Seaborn (integrates well with Matplotlib axes)
    sns.histplot(data=valid_scores, bins=num_bins, kde=True, ax=ax) # kde=True adds density curve

    ax.set_title(f'Marks Distribution for {subject}', fontsize=14)
    ax.set_xlabel('Marks Obtained', fontsize=12)
    ax.set_ylabel('Number of Students', fontsize=12)
    ax.grid(axis='y', linestyle='--', alpha=0.7) # Add light grid lines

    # Improve layout
    plt.tight_layout()

    return fig # Return the figure object

def plot_overall_score_distribution(total_marks_series: pd.Series, total_possible_marks: float = None, theme: str = 'dark') -> plt.Figure | None:
    """
    Generates a histogram for the distribution of total scores.

    Args:
        total_marks_series: A pandas Series containing total marks for each student.
        total_possible_marks: The maximum possible total score (optional, for axis limits).
        theme: 'light' or 'dark' to adjust plot style.

    Returns:
        A matplotlib Figure object containing the plot, or None if data is invalid.
    """
    if total_marks_series is None or total_marks_series.empty:
        print("Error: No total marks data provided for plotting.")
        return None

    valid_scores = total_marks_series.dropna()

    if valid_scores.empty:
        print("No valid total scores to plot.")
        fig, ax = plt.subplots(figsize=(6, 4))
        ax.text(0.5, 0.5, "No valid total score data", ha='center', va='center', fontsize=12)
        ax.set_title("Overall Score Distribution")
        ax.axis('off')
        return fig

    if theme == 'dark':
        plt.style.use('dark_background')
    else:
        # Use a standard, reliable light style
        plt.style.use('ggplot') # Use a standard, compatible style

    fig, ax = plt.subplots(figsize=(7, 5))

    # Determine bins based on total score range
    min_score = valid_scores.min()
    max_score = valid_scores.max()
    if pd.isna(min_score) or pd.isna(max_score) or min_score == max_score:
        num_bins = 10 # Default bins
    else:
        # Aim for wider bins for total scores
        num_bins = max(8, min(25, int((max_score - min_score) / (total_possible_marks / 20 if total_possible_marks else 20)) + 1))

    sns.histplot(data=valid_scores, bins=num_bins, kde=True, ax=ax)

    ax.set_title('Overall Score Distribution', fontsize=14)
    ax.set_xlabel('Total Marks Obtained', fontsize=12)
    ax.set_ylabel('Number of Students', fontsize=12)
    if total_possible_marks:
        ax.set_xlim(0, total_possible_marks * 1.05) # Set x-axis limit slightly beyond max possible
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    return fig


# scoresight/analysis/plotter.py

def plot_average_marks_per_subject(subject_stats: dict, theme: str = 'dark') -> plt.Figure | None:
    """
    Generates a bar chart showing the average mark for each subject.

    Args:
        subject_stats: Dictionary containing statistics per subject (needs 'mean').
                       Expected format: {'SubjectName': {'mean': value, ...}, ...}
        theme: 'light' or 'dark' to adjust plot style.

    Returns:
        A matplotlib Figure object containing the plot, or None if data is invalid or plotting fails.
    """
    if not subject_stats:
        # Log the error internally if needed, but don't print to console in production
        # print("Error: No subject statistics provided for plotting averages.")
        return None

    subjects = list(subject_stats.keys())
    averages = []
    valid_subjects = []
    for subj in subjects:
        mean_val = subject_stats[subj].get('mean', np.nan) # Use np.nan if mean is missing or 'N/A'
        # Check if the mean value is a valid number
        if isinstance(mean_val, (int, float)) and not pd.isna(mean_val):
            averages.append(mean_val)
            valid_subjects.append(subj)
        # else: # Optional: Log skipped subjects if desired for internal logs
             # print(f"Warning: Skipping subject '{subj}' due to invalid/missing average score: {mean_val}")

    if not valid_subjects:
        # Log this situation if needed
        # print("No valid average scores found to plot.")
        # Return None or a figure indicating no data
        try:
            fig, ax = plt.subplots(figsize=(6, 4))
             # Set style based on theme even for the 'no data' message for consistency
            if theme == 'dark': plt.style.use('dark_background'); color = 'white'
            else: plt.style.use('ggplot'); color = 'black'
            ax.text(0.5, 0.5, "No valid average scores\nto plot", ha='center', va='center', fontsize=12, color=color)
            ax.set_title("Average Marks per Subject", color=color)
            ax.set_facecolor(fig.get_facecolor()) # Match background
            ax.axis('off')
            return fig
        except Exception as empty_plot_err:
            print(f"Error creating 'no data' figure for average marks: {empty_plot_err}")
            return None # Return None if even the placeholder fails

    # Proceed with plotting if valid data exists
    try:
        fig, ax = plt.subplots(figsize=(max(6, len(valid_subjects) * 0.8), 5)) # Adjust width

        # Set plot style based on theme
        if theme == 'dark':
            plt.style.use('dark_background')
            bar_color = 'skyblue'
            edge_color = 'lightblue'
        else:
            plt.style.use('ggplot') # Use ggplot for light theme
            bar_color = 'cornflowerblue'
            edge_color = 'black'

        # Create the bar chart
        bars = ax.bar(valid_subjects, averages, color=bar_color, edgecolor=edge_color)

        # Set titles and labels
        ax.set_title('Average Marks per Subject', fontsize=14)
        ax.set_xlabel('Subject', fontsize=12)
        ax.set_ylabel('Average Mark', fontsize=12)
        ax.set_ylim(0, 105) # Assume max mark is 100, add padding

        # Rotate x-axis tick labels (removed ha='right')
        ax.tick_params(axis='x', rotation=45)

        # Add average values on top of bars
        for bar in bars:
            yval = bar.get_height()
            # Place text slightly above the bar
            ax.text(bar.get_x() + bar.get_width()/2.0, yval + 1, f'{yval:.1f}',
                    va='bottom', ha='center', fontsize=10)

        plt.tight_layout() # Adjust layout
        return fig # Return the generated figure

    except Exception as plot_err:
        # Log the error if plotting fails
        print(f"ERROR during Average Marks plot creation: {plot_err}")
        import traceback
        traceback.print_exc() # Keep traceback for debugging unexpected plot errors
        # Attempt to close the potentially partially created figure if error occurred
        if 'fig' in locals() and fig is not None:
             plt.close(fig)
        return None # Return None to indicate plotting failure
    
# --- Helper to save plot ---
def save_plot_to_bytes(figure: plt.Figure) -> io.BytesIO | None:
    """Saves a Matplotlib figure to a BytesIO buffer."""
    if figure is None:
        return None
    try:
        buf = io.BytesIO()
        figure.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        plt.close(figure) # Close the figure to free memory
        return buf
    except Exception as e:
        print(f"Error saving plot to bytes: {e}")
        plt.close(figure) # Ensure figure is closed even on error
        return None