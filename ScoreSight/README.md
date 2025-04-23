# ✨ ScoreSight ✨

**Analyze student performance, visualize results, and generate insightful reports with ease.**

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
<!-- Optional: Add badges for build status, code coverage etc. if you set them up -->

<!-- Optional: Add a Logo or Banner Here -->
<!-- <p align="center">
  <img src="path/to/your/logo.png" alt="ScoreSight Logo" width="200"/>
</p> -->

ScoreSight is a desktop application built with Python and CustomTkinter designed to help teachers and academic staff quickly analyze student results from CSV or Excel files. It provides key performance indicators, subject-wise breakdowns, visualizations, and generates a downloadable PDF report.

---

## 🚀 Key Features

*   **📁 Load Data Easily:** Import student marks directly from `.csv` or `.xlsx` files.
*   **🥇 Identify Top Performers:**
    *   Find the Overall Topper(s) based on total marks.
    *   Find Topper(s) for each individual subject.
*   **📊 Detailed Statistics:**
    *   Calculate Mean, Median, Min, Max, and Standard Deviation for each subject.
    *   Count the number of students evaluated per subject.
    *   **NEW:** Count students scoring below a defined threshold (e.g., 40) in each subject.
*   **📉 Performance Overview:**
    *   Identify students scoring below 40% overall.
*   **📈 Visualize Results:**
    *   Generate histograms showing the overall score distribution.
    *   Generate histograms for mark distribution within each subject.
    *   Display a bar chart comparing average marks across subjects.
*   **📄 Downloadable PDF Reports:** Generate a comprehensive PDF report containing:
    *   Overall Summary (Toppers, Overall Failing Students)
    *   Detailed Subject Statistics (including subject-wise fail counts)
    *   Embedded visualizations (graphs).
*   **🎨 Attractive & Themeable GUI:** Modern user interface built with CustomTkinter, supporting Light/Dark/System themes.

---

## 📸 Screenshots


**Main Window (Light Theme):**
![ScoreSight Main Window Light](<assets/screenshot_main_light.png>)

**Graphs Tab (Dark Theme):**
![ScoreSight Graphs Dark](<assets/screenshot_graphs_dark.png>)

**Generated PDF Report Snippets:**
![ScoreSight PDF Report](<assets/screenshot_pdf_1.png>)
![ScoreSight PDF Report](<assets/screenshot_pdf_2.png>)
![ScoreSight PDF Report](<assets/screenshot_pdf_3.png>)

---

## 🛠️ Technology Stack

*   **Language:** Python 3.9+
*   **GUI:** CustomTkinter
*   **Data Handling:** Pandas, NumPy
*   **Plotting:** Matplotlib, Seaborn
*   **PDF Generation:** ReportLab
*   **Excel Reading:** openpyxl (required by Pandas)

---

## 📁 Folder Structure


```plaintext
ScoreSight/
├── scoresight/ # Main source code package
│ ├── init.py
│ ├── main.py # Application entry point
│ ├── gui/ # GUI code
│ │ ├── init.py
│ │ └── app_window.py # Main application window class
│ ├── analysis/ # Data analysis & plotting logic
│ │ ├── init.py
│ │ └── analyzer.py # Calculation functions
│ │ └── plotter.py # Graph generation functions
│ ├── reporting/ # Report generation logic
│ │ ├── init.py
│ │ └── generator.py # PDF creation functions
│ └── utils/ # Utility functions (Optional)
│ └── init.py
├── tests/ # Unit tests (Optional)
│ └── init.py
├── assets/ # Icons, images (Optional)
├── data/ # Input CSV/Excel files (ignored by Git)
│ └── .gitignore
├── reports/ # Output reports (ignored by Git)
│ └── .gitignore
├── requirements.txt # Project dependencies
├── README.md # This file
└── .gitignore # Git ignore rules
```


## ⚙️ Setup and Installation

Follow these steps to set up and run ScoreSight on your local machine:

1.  **Clone the Repository:**
    ```bash
    git clone https://github.com/LakshayChhabra248/My-Projects/tree/main/ScoreSight
    cd ScoreSight
    ```

2.  **Create a Virtual Environment:** (Recommended)
    *   This isolates project dependencies.
    ```bash
    python -m venv venv
    ```

3.  **Activate the Virtual Environment:**
    *   **Windows (cmd/powershell):**
        ```bash
        .\venv\Scripts\activate
        ```
    *   **macOS/Linux (bash/zsh):**
        ```bash
        source venv/bin/activate
        ```

4.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

---

## ▶️ Usage

1.  **Activate Virtual Environment:** Make sure your virtual environment (`venv`) is activated (see step 3 above).
2.  **Run the Application:**
    ```bash
    python scoresight/main.py
    ```
3.  **Load Data:** Click the "Load Data File" button and select your `.csv` or `.xlsx` file containing student results. (See Input Format below).
4.  **Analyze:** Once the data is loaded, click the "Run Analysis" button.
5.  **View Results:** Explore the different tabs:
    *   **Summary:** Shows overall toppers and students failing overall (<40%).
    *   **Subject Details:** Provides statistics (including fail count) and toppers for each subject.
    *   **Graphs:** Displays visualizations of the results.
    *   **Data Preview:** Shows the first few rows of the loaded data.
6.  **Generate Report:** Click the "Generate PDF Report" button. Choose a location and filename to save the report. The default location is the `reports/` folder.
7.  **Change Theme:** Use the dropdown menu in the sidebar to switch between Light, Dark, and System appearance modes.

---

## 📄 Input File Format

ScoreSight expects input files (`.csv` or `.xlsx`) with the following structure:

*   **Header Row:** The first row should contain column headers.
*   **First Column:** Must be the **Student Identifier** (e.g., 'StudentID', 'Name', 'RollNo'). This column is used to identify students in the results.
*   **Subsequent Columns:** Each column after the first should represent a **Subject**, with the corresponding **numeric marks** for each student in the rows below.
*   **Data Types:** Marks should be numeric. Non-numeric values will be ignored or treated as errors during calculations.

**Example:**

| StudentID | Name    | Math | Physics | Chemistry |
| :-------- | :------ | :--- | :------ | :-------- |
| S001      | Alice   | 85   | 90      | 78        |
| S002      | Bob     | 92   | 88      | 95        |
| S003      | Charlie | 76   | 82      | 80        |
| ...       | ...     | ...  | ...     | ...       |

*(Note: The current version uses the *first column* as the identifier, regardless of its header name.)*

---

## 📤 Output

The primary output is a **PDF Report** (`ScoreSight_Analysis_Report.pdf` by default) saved in the `reports/` directory. This report includes:

1.  Overall Summary (Total Students, Subjects)
2.  Overall Topper(s) List
3.  List of Students Below 40% Overall
4.  Subject-wise Details:
    *   Statistics Table (Count, Fail Count < 40, Mean, Median, Min, Max, Std Dev)
    *   Subject Topper(s) List
5.  Embedded Graphs:
    *   Average Marks per Subject (Bar Chart)
    *   Overall Score Distribution (Histogram)
    *   Marks Distribution per Subject (Histograms)

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details (or add a `LICENSE` file with the MIT text).

---

## 🙌 Acknowledgements (Optional)

*   Mention your teacher if appropriate.
*   Any libraries or resources you found particularly helpful.

---

## 📞 Contact 

Name - Lakshay Chhabra

Email: <lakshaychhabra248@gmail.com>

Project Link: <https://github.com/LakshChhabra248/My-Projects/tree/main/ScoreSight>

---
