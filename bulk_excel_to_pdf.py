import pandas as pd
import numpy as np
import pdfkit
import tkinter as tk
import tkinter.filedialog as file_dialog

def process_sheet(file, sheet=None, num=None):
    if not sheet:
        test_file = pd.read_excel(file)
    else:
        test_file = pd.read_excel(file, sheet_name=sheet)
    test_file = test_file.dropna(axis="columns", how="all")
    test_file = test_file.fillna(value=' ')
    test_file.columns = pd.Series([np.nan if "Unnamed: " in x else x for x in test_file.columns.values]).fillna(value=" ").values.flatten()
    test_file.to_html("test.html")
    pdfkit.from_file("test.html", f"{sheet}.pdf", options={"page-width": '20in',
                                                        "page-height": '15in'})  
    print(f"Converted {file} to PDF -- test{num}.pdf")

def excel_to_pdf(file_names):
    for file_idx, file in enumerate(file_names):
        excelfile = pd.ExcelFile(file)
        for idx, sheet in enumerate(excelfile.sheet_names):
            process_sheet(file, sheet, f"{file_idx}_{idx}")

root = tk.Tk()
files = file_dialog.askopenfilenames(parent=root, title='Choose an Excel file', filetypes=[("Excel Files", ".xlsx")])
excel_to_pdf(files)
