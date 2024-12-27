# 📊 CSV Analyzer - Your Simple Tool for Data Exploration 🔍

This Python application provides an intuitive user interface to explore CSV data and uncover potential trends or insights with ease. It allows you to:

*   Load and parse CSV files effortlessly.
*   Select a primary feature for in-depth analysis.
*   Choose multiple secondary features to compare against the main one.
*   Generate a basic verdict based on the top results.
*   View analysis results in an interactive and sortable table.
*   Perform aggregations (mean, median, sum) on the main feature based on groupings.
*   Configure the number of top results to display.

## ✨ Key Features:

### 💻 Intuitive GUI:
Built with `tkinter`, the interface is straightforward and easy to navigate with buttons, dropdowns, listboxes, labels, treeview and a text widget for displaying results.

### 🚀 Easy Data Exploration:
Load and analyze CSV data with minimal effort using an intuitive GUI.

### ⚙️ Customizable CSV Loading:
Easily specify the delimiter and encoding options for your CSV files.

### 🎛️ Multiple Feature Selection:
Select multiple features for comparison with the primary feature using `Ctrl + Click`.

### 📈 Enhanced Analysis:
Perform aggregations (mean, median, sum) and retrieve the top N results based on the selected features.

### 🗂️ Table View Output:
View the analyzed data in an interactive and sortable table format.

### ✅ Clear Verdict:
A verdict, based on the analysis, is prominently displayed on screen.

## 🛠️ Requirements:

*   Python 3.x (tested with 3.x)
*   `pandas` library (`pip install pandas`)
*   `tkinter` library (included in standard Python installation)

### 📦 Installation:

1.  Clone this repository or download the code files.
2.  Open a terminal or command prompt and navigate to the project directory.
3.  Install the `pandas` library using:
    ```bash
    pip install pandas
    ```

## 🚀 Usage:

1.  Run the script by opening your terminal and executing the following command:
    ```bash
    python main.py
    ```
2.  Click the "Load CSV" button and select your CSV file. Note that only `.csv` files can be loaded.
3.  Specify the delimiter and encoding options if your CSV file does not use standard settings.
4.  Choose a main feature from the "Select the main feature:" dropdown.
5.  Select any additional features for comparison using `Ctrl + Click` in the "Select features for analysis" list box.
6.  Choose an optional aggregation from the "Aggregation (optional)" dropdown, if needed.
7.  Enter the number of top results needed in "Top N Results:" field.
8.  Click the "Analyze" button to perform the analysis.

The results will be displayed in an interactive table, including the top N rows sorted by selected features. A verdict based on your analysis, along with any error messages, will also be displayed.

**Contribute:**

Your contributions are welcome! If you have ideas for new features, improvements, or bug fixes, please feel free to submit a pull request.

**Created By:** Lakshay Chhabra
