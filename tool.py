import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os





# Import your existing Python script
from script import process_folder

def select_input_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        input_folder_entry.delete(0, tk.END)
        input_folder_entry.insert(0, folder_path)

def select_output_folder():
    output_folder = filedialog.askdirectory()
    if output_folder:
        output_folder_entry.delete(0, tk.END)
        output_folder_entry.insert(0, output_folder)

def run_tool():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    if input_folder and output_folder:
        output_file = os.path.join(output_folder, 'output.csv')
        process_folder(input_folder, output_file)
        messagebox.showinfo('Success', 'GPS data extraction completed successfully!')
    else:
        messagebox.showerror('Error', 'Please select both input and output folders.')

# Create the main window
root = tk.Tk()
root.title('NISHANTH GPS DATA EXTRACTION TOOL ')

# Create and pack widgets for input folder
input_folder_label = tk.Label(root, text='Input Folder:')
input_folder_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

input_folder_entry = tk.Entry(root, width=50)
input_folder_entry.grid(row=0, column=1, padx=5, pady=5)

browse_input_button = tk.Button(root, text='Browse', command=select_input_folder)
browse_input_button.grid(row=0, column=2, padx=5, pady=5)

# Create and pack widgets for output folder
output_folder_label = tk.Label(root, text='Output Folder:')
output_folder_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

output_folder_entry = tk.Entry(root, width=50)
output_folder_entry.grid(row=1, column=1, padx=5, pady=5)

browse_output_button = tk.Button(root, text='Browse', command=select_output_folder)
browse_output_button.grid(row=1, column=2, padx=5, pady=5)

# Create and pack "Run" button
run_button = tk.Button(root, text='Run', command=run_tool)
run_button.grid(row=2, column=1, padx=5, pady=10)

# Run the application
root.mainloop()
