import pandas as pd
import tkinter as tk
from tkinter import filedialog, ttk

def load_csv():
    global df
    file_path = filedialog.askopenfilename()
    if file_path:
        df = pd.read_csv(file_path)
        populate_dropdowns(df.columns)

def populate_dropdowns(columns):
    feature_listbox.delete(0, tk.END)
    main_dropdown['values'] = list(columns)
    for column in columns:
        feature_listbox.insert(tk.END, column)

def analyze():
    selected_features = list(feature_listbox.curselection())
    selected_features = [feature_listbox.get(i) for i in selected_features]
    main_feature = main_dropdown.get()
    selected_features = [feature for feature in selected_features if feature]  # Filter out empty selections

    result = df[[main_feature] + selected_features].sort_values(by=selected_features, ascending=False).head(5)
    
    verdict = generate_verdict(result)
    
    # Clear previous results
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Top 5 results based on selected features:\n")
    result_text.insert(tk.END, result.to_string(index=False))
    result_text.insert(tk.END, "\n\nVerdict:\n" + verdict)

def generate_verdict(result):
    # Placeholder logic for generating a verdict
    # You can replace this with more sophisticated analysis
    if result.empty:
        return "No results to analyze."
    else:
        return f"Based on the analysis, the top option is: {result.iloc[0][0]}"

root = tk.Tk()
root.title("CSV Analyzer")

load_btn = tk.Button(root, text="Load CSV", command=load_csv)
load_btn.pack(pady=10)

main_label = tk.Label(root, text="Select the main feature:")
main_label.pack(pady=5)

main_dropdown = ttk.Combobox(root)
main_dropdown.pack(pady=10)

feature_label = tk.Label(root, text="Select features for analysis (Ctrl + Click to select multiple):")
feature_label.pack(pady=5)

feature_listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
feature_listbox.pack(pady=10)

analyze_btn = tk.Button(root, text="Analyze", command=analyze)
analyze_btn.pack(pady=10)

# Text widget to display the results
result_text = tk.Text(root, wrap=tk.WORD, width=80, height=20)
result_text.pack(pady=10)

root.mainloop()
