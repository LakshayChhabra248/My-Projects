# CSV Analyzer - A Simple Tool for Exploratory Data Analysis
- This Python application provides a user-friendly interface to explore CSV data and identify potential trends or insights. It allows you to:

    * Load a CSV file.
    * Select a main feature for analysis.
    * Choose additional features to compare against the main feature.
    * Generate a basic verdict based on the top results.
## Features:

### Intuitive GUI: 
The tkinter library creates a straightforward interface with buttons, dropdowns, listboxes, and a text widget for displaying results.
### Easy data exploration: 
Load and analyze CSV data with minimal effort.
### Multiple feature selection: 
Choose additional features to compare with the main feature.
## Requirements:

* Python 3.x (tested with 3.x)
* pandas library (pip install pandas)
* tkinter library (included in standard Python installation)
### Installation:

1. Clone this repository or download the code files.

2. Open a terminal or command prompt and navigate to the project directory.

3. Install the required library if it's not already installed:   

    ```pip install pandas```

## Usage:

* Run the script using:

    `python main.py`


* Click the "Load CSV" button and select your CSV file.

* Choose a main feature from the dropdown menu.

* Select additional features for comparison using Ctrl + Click (multiple selection).

* Click the "Analyze" button to perform the analysis.

The results will be displayed in the text box, including the top 5 rows sorted by the selected features and a basic verdict based on the top option.