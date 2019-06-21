#import tkinter
from tkinter import messagebox
def check_input_output(ip_folder=None,op_folder=None):
    if (ip_folder is None and op_folder is None) or (ip_folder is None and op_folder is not None):
        messagebox.showwarning(message="Please select data folder")
    else:
        messagebox.askquestion(title='Info',message="Shall i proceed without output folder")

def validate_mvavg():
