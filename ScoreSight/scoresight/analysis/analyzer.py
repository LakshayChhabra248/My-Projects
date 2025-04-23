# scoresight/analysis/analyzer.py
import pandas as pd
import numpy as np

def get_subject_names(df: pd.DataFrame) -> list:
    """
    Identifies subject columns (assumes all columns after the first are subjects).

    Args:
        df: The input pandas DataFrame.

    Returns:
        A list of subject column names. Returns an empty list if df is None or has < 2 columns.
    """
    if df is None or len(df.columns) < 2:
        return []
    # Assume the first column is the identifier, the rest are subjects
    return df.columns[1:].tolist()

def calculate_total_marks(df: pd.DataFrame, subjects: list) -> pd.Series:
    """
    Calculates the total marks for each student across the specified subjects.
    Handles non-numeric data by coercing to NaN, then sums valid numbers.

    Args:
        df: The input pandas DataFrame.
        subjects: A list of subject column names to sum.

    Returns:
        A pandas Series containing the total marks for each student.
        Returns an empty Series if df is None, subjects list is empty, or columns don't exist.
    """
    if df is None or not subjects:
        return pd.Series(dtype=float)

    try:
        # Select only the specified subject columns
        subjects_df = df[subjects]
        # Ensure all subject columns are treated as numeric, turning errors into NaN
        numeric_subjects_df = subjects_df.apply(pd.to_numeric, errors='coerce')
        # Sum across rows (axis=1), setting total to NaN if *any* subject score is NaN
        total_marks = numeric_subjects_df.sum(axis=1, skipna=False)
        return total_marks
    except KeyError:
        # Log the error if needed, but prevent crashing
        print(f"Error calculating total marks: One or more subject columns not found in DataFrame: {subjects}")
        return pd.Series(dtype=float)
    except Exception as e:
        print(f"Error calculating total marks: {e}")
        return pd.Series(dtype=float)

def find_overall_topper(df: pd.DataFrame, identifier_col: str, total_marks_series: pd.Series, total_possible_marks: float = None) -> list:
    """
    Finds the student(s) with the highest total marks FROM THE PROVIDED SERIES.
    The DataFrame (df) is used only to get the identifier (e.g., name).
    It assumes total_marks_series corresponds index-wise to df.

    Args:
        df: The input pandas DataFrame (used for identifiers).
        identifier_col: The name of the column containing student identifiers (e.g., 'Name').
        total_marks_series: A pandas Series with total marks per student (index should align with df).
                            This series should ideally contain NaN for students with incomplete scores.
        total_possible_marks: The maximum possible total score (optional, for percentage calculation).

    Returns:
        A list of dictionaries, where each dictionary represents a topper
        (handling ties). Each dictionary contains 'name', 'total_marks',
        and optionally 'percentage'. Returns an empty list on error or if no data/no valid totals.
    """
    # Check inputs
    if df is None or total_marks_series is None or total_marks_series.empty or identifier_col not in df.columns:
        # print("Warning: Invalid input for find_overall_topper.") # Keep logs minimal
        return []
    # Ensure indices match
    if not df.index.equals(total_marks_series.index):
         print("Error: DataFrame index and total_marks_series index do not match in find_overall_topper.")
         return []

    try:
        # Drop NaN values from the total marks series before finding the max
        valid_total_marks = total_marks_series.dropna()
        if valid_total_marks.empty:
            # print("No valid total scores found to determine overall topper.")
            return [] # No students had a valid total score

        max_total_marks = valid_total_marks.max()

        # Find the index positions in the *original* series where the score equals the max
        topper_indices = total_marks_series[total_marks_series == max_total_marks].index

        # Use these indices to get the corresponding rows from the original DataFrame
        toppers_df = df.loc[topper_indices]

        results = []
        for index, row in toppers_df.iterrows():
            topper_info = {
                'name': row[identifier_col],
                'total_marks': max_total_marks # Use the definitive max score found
            }
            if total_possible_marks and total_possible_marks > 0:
                try:
                    # Ensure max_total_marks is float for division
                    percentage = round((float(max_total_marks) / total_possible_marks) * 100, 2)
                    topper_info['percentage'] = percentage
                except ValueError: # Handle case where max_total_marks isn't convertible to float
                    pass
            results.append(topper_info)

        return results
    except Exception as e:
        print(f"Error finding overall topper: {e}")
        return []


def find_subject_toppers(df: pd.DataFrame, identifier_col: str, subjects: list) -> dict:
    """
    Finds the top scoring student(s) for each subject. Handles non-numeric scores.

    Args:
        df: The input pandas DataFrame.
        identifier_col: The name of the column containing student identifiers.
        subjects: A list of subject column names.

    Returns:
        A dictionary where keys are subject names and values are lists of
        dictionaries. Each inner dictionary represents a topper for that subject
        (handling ties) and contains 'name' and 'score'.
        Returns an empty dict on error.
    """
    if df is None or not subjects or identifier_col not in df.columns:
        return {}

    subject_toppers_dict = {}
    try:
        for subject in subjects:
            if subject not in df.columns:
                print(f"Warning: Subject column '{subject}' not found for toppers. Skipping.")
                subject_toppers_dict[subject] = []
                continue

            # Convert to numeric for this subject, coercing errors
            numeric_scores = pd.to_numeric(df[subject], errors='coerce')

            # Drop NaNs to find the maximum valid score
            valid_scores = numeric_scores.dropna()
            if valid_scores.empty:
                 # print(f"Warning: No valid scores for subject '{subject}'. Skipping topper calculation.")
                 subject_toppers_dict[subject] = []
                 continue

            max_score = valid_scores.max()

            # Find indices in the *original* numeric_scores series where score matches max
            topper_indices = numeric_scores[numeric_scores == max_score].index

            # Get the corresponding rows from the original DataFrame using these indices
            toppers_df = df.loc[topper_indices]

            toppers_list = []
            for index, row in toppers_df.iterrows():
                toppers_list.append({
                    'name': row[identifier_col],
                    'score': max_score # Use the actual max score found
                })
            subject_toppers_dict[subject] = toppers_list

        return subject_toppers_dict
    except Exception as e:
        print(f"Error finding subject toppers: {e}")
        return {}


def calculate_subject_stats(df: pd.DataFrame, subjects: list) -> dict:
    """
    Calculates basic statistics for each subject, including fail count (< 40).
    Handles non-numeric data gracefully using pandas functions.

    Args:
        df: The input pandas DataFrame.
        subjects: A list of subject column names.

    Returns:
        A dictionary where keys are subject names and values are dictionaries
        containing the statistics ('mean', 'median', 'min', 'max', 'count',
        'std_dev', 'fail_count'). Returns an empty dict on error.
    """
    if df is None or not subjects:
        return {}

    subject_stats_dict = {}
    FAIL_THRESHOLD = 40 # Define the failing threshold

    try:
        for subject in subjects:
            if subject not in df.columns:
                # print(f"Warning: Subject column '{subject}' not found for stats. Skipping.")
                subject_stats_dict[subject] = {}
                continue

            # Convert to numeric, coercing errors.
            numeric_scores = pd.to_numeric(df[subject], errors='coerce')

            # Calculate standard stats, automatically ignoring NaNs
            count = int(numeric_scores.count()) # Count of non-NaN scores

            # --- Calculate Fail Count ---
            fail_count = 0
            if count > 0:
                # Count where score is less than the threshold (only on valid scores)
                fail_count = int(numeric_scores[numeric_scores < FAIL_THRESHOLD].count())
            # --- End Fail Count Calculation ---

            stats = {
                'count': count,
                'mean': round(numeric_scores.mean(), 2) if count > 0 else 'N/A',
                'median': round(numeric_scores.median(), 2) if count > 0 else 'N/A',
                'min': round(numeric_scores.min(), 2) if count > 0 else 'N/A',
                'max': round(numeric_scores.max(), 2) if count > 0 else 'N/A',
                'std_dev': round(numeric_scores.std(), 2) if count > 1 else 'N/A',
                'fail_count': fail_count if count >= 0 else 'N/A' # Store the fail count (use >=0 to show 0 if count=0)
            }
            subject_stats_dict[subject] = stats
        return subject_stats_dict
    except Exception as e:
        print(f"Error calculating subject stats: {e}")
        return {}

# --- Main Orchestration Function ---
def analyze_data(df: pd.DataFrame) -> dict:
    """
    Performs the complete analysis of the student data DataFrame.
    """
    results = {
        'num_students': 0,
        'identifier_col': None,
        'subject_names': [],
        'total_possible_marks': 0,
        'overall_topper': [],
        'subject_toppers': {},
        'subject_stats': {}, # Will include fail_count from calculate_subject_stats
        'total_marks_series': pd.Series(dtype=float),
        'failing_students': [], # Overall failing students
        'error': None
    }

    if df is None or df.empty:
        results['error'] = "Input data is empty."
        return results

    try:
        results['num_students'] = len(df)
        if len(df.columns) < 2:
             results['error'] = "Insufficient columns (requires identifier and at least one subject)."
             return results

        results['identifier_col'] = df.columns[0]
        subjects = get_subject_names(df)
        results['subject_names'] = subjects

        if not subjects:
            results['error'] = "No subject columns identified."
            return results

        # Work on a copy to ensure original df passed from GUI is untouched
        analysis_df = df.copy()

        # Ensure subject columns are numeric, coerce errors to NaN.
        for col in subjects:
             analysis_df[col] = pd.to_numeric(analysis_df[col], errors='coerce')


        # --- Calculations ---

        # 1. Calculate total marks (will be NaN if any subject score is NaN)
        total_marks = calculate_total_marks(analysis_df, subjects)
        results['total_marks_series'] = total_marks

        # 2. Define Max Possible Score (Assumption: 100 per subject)
        max_marks_per_subject = 100
        total_possible = len(subjects) * max_marks_per_subject
        results['total_possible_marks'] = total_possible

        # 3. Find Overall Topper (uses total_marks series with NaNs)
        results['overall_topper'] = find_overall_topper(analysis_df, results['identifier_col'], total_marks, total_possible)

        # 4. Find Subject Toppers (operates per subject, handles NaNs internally)
        results['subject_toppers'] = find_subject_toppers(analysis_df, results['identifier_col'], subjects)

        # 5. Calculate Subject Stats (includes fail_count)
        results['subject_stats'] = calculate_subject_stats(analysis_df, subjects)

        # 6. Calculate Percentages and Find Overall Failing Students (< 40%)
        failing_students_list = []
        if total_possible > 0:
            valid_total_marks = total_marks.dropna()
            if not valid_total_marks.empty:
                percentages = (valid_total_marks / total_possible) * 100
                failing_indices = percentages[percentages < 40].index

                if not failing_indices.empty:
                    failing_df = analysis_df.loc[failing_indices]
                    for index, row in failing_df.iterrows():
                        calculated_percentage = percentages.loc[index]
                        failing_students_list.append({
                            'name': row[results['identifier_col']],
                            'percentage': round(calculated_percentage, 2)
                        })
                    failing_students_list.sort(key=lambda x: x['percentage'])

        results['failing_students'] = failing_students_list

        # --- Final Checks ---
        # (Add any other relevant checks if needed)

    except Exception as e:
        print(f"An unexpected error occurred during analysis: {e}")
        results['error'] = f"An unexpected error occurred during analysis: {e}"
        results['total_marks_series'] = pd.Series(dtype=float) # Ensure reset on error
        results['failing_students'] = [] # Ensure reset on error
        # Optionally clear other results too
        # results['subject_stats'] = {}
        # results['subject_toppers'] = {}
        # results['overall_topper'] = []

    return results