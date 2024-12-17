# CSV Analyzer - A Simple Tool for Exploratory Data Analysis

This Python application provides a user-friendly interface to explore CSV data and identify potential trends or insights. It allows you to:

*   Load a CSV file with customizable delimiter and encoding.
*   Select a main feature for analysis.
*   Choose additional features to compare against the main feature.
*   Generate a basic verdict based on the top results.
*   View the analysis results in a sortable table.
*  Perform aggregation (mean, median, sum) on the main feature grouped by selected features.
* Configure the number of top results to show.

## Features:

### Intuitive GUI:
The `tkinter` library creates a straightforward interface with buttons, dropdowns, listboxes, labels, treeview and a text widget for displaying results.

### Easy Data Exploration:
Load and analyze CSV data with minimal effort.

### Customizable CSV Loading:
Specify the delimiter and encoding for your CSV file.

### Multiple Feature Selection:
Choose multiple additional features to compare with the main feature using `Ctrl + Click`.

### Enhanced Analysis:
Perform aggregations (mean, median, sum) and retrieve the top N results.

### Table View Output:
View the analysis results in an interactive and sortable table format.

### Clear Verdict:
A verdict is prominently displayed on the screen based on the analysis.

## Requirements:

*   Python 3.x (tested with 3.x)
*   `pandas` library (`pip install pandas`)
*   `tkinter` library (included in standard Python installation)

### Installation:

1.  Clone this repository or download the code files.
2.  Open a terminal or command prompt and navigate to the project directory.
3.  Install the required library if it's not already installed:

    ```bash
    pip install pandas
    ```

## Usage:

*   Run the script using:

    ```bash
    python main.py
    ```

*   Click the "Load CSV" button and select your CSV file. Only `.csv` files can be selected.
*   Specify the delimiter and encoding options if your CSV file is not standard.
*   Choose a main feature from the "Select the main feature:" dropdown menu.
*   Select additional features for comparison using `Ctrl + Click` (multiple selection) in "Select features for analysis" list box.
*   Choose an optional aggregation from the "Aggregation (optional)" dropdown if needed.
*  Enter the number of top rows needed in "Top N Results:" field.
*   Click the "Analyze" button to perform the analysis.

The results will be displayed in a table view, including the top N rows sorted by the selected features, and a verdict will be prominently displayed. An optional error text area will display any errors that may occur.

