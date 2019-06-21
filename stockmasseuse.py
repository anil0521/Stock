import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import Transformations as algos
import os

class StockMassuse():

    def __init__(self,window):

        self.window = window
        window.title("Stock Masseuse")
        window.geometry("1000x700")

        canvas = tk.Canvas(window, width=1800, height=1400)
        canvas.pack()

        global IP_Folder
        global OP_Folder

        IP_Folder = tk.StringVar()
        OP_Folder = tk.StringVar()
        self.mvavg_window_values = []

        tk.Label(window, text="Input Folder :").place(x=62, y=60)
        #print('after label')
        tk.Entry(window, textvariable=IP_Folder).place(x=140, y=60)
        tk.Button(window, text="Browse",command=self.input_folder).place(x=280, y=55)

        tk.Label(window, text="Output Folder :").place(x=50, y=90)
        tk.Entry(window, textvariable=OP_Folder).place(x=140, y=90)
        tk.Button(window, text="Browse",command=self.output_folder).place(x=280, y=85)

        canvas.create_line(30, 120, 800, 120, fill='grey')

        self.dataset_radio_button = tk.IntVar()
        self.Raw_rdbtn = tk.Radiobutton(window, text="Raw / EOD Download Type", variable=self.dataset_radio_button, value=1)
        self.Raw_rdbtn.place(x=50, y=140)

        self.Square_rdbtn = tk.Radiobutton(window, text="Square Root", variable=self.dataset_radio_button, value=2)
        self.Square_rdbtn.place(x=450, y=140)

        canvas.create_line(30, 170, 800, 170, fill='grey')

        self.spinbox_val = tk.StringVar()
        self.spinbox = tk.Spinbox(window,textvariable=self.spinbox_val, from_=0, to=252,state="disabled")
        self.spinbox.place(x=490, y=180)

        self.sma_ema_radio_button = tk.IntVar()
        self.Sma_rdbtn = tk.Radiobutton(window, text="SMA", variable=self.sma_ema_radio_button, value=1,state="disabled")
        self.Sma_rdbtn.place(x=150, y=320)

        self.Ema_rdbtn = tk.Radiobutton(window, text="EMA", variable=self.sma_ema_radio_button, value=2,state="disabled")
        self.Ema_rdbtn.place(x=340, y=320)

        self.chk2 = tk.IntVar()
        self.chk2_btn = tk.Checkbutton(window, text="2", variable=self.chk2, command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk2_btn.place(x=90,y=220)

        self.chk3 = tk.IntVar()
        self.chk3_btn = tk.Checkbutton(window, text="3", variable=self.chk3,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk3_btn.place(x=190, y=220)

        self.chk4 = tk.IntVar()
        self.chk4_btn = tk.Checkbutton(window, text="4", variable=self.chk4,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk4_btn.place(x=290, y=220)

        self.chk5 = tk.IntVar()
        self.chk5_btn = tk.Checkbutton(window, text="5", variable=self.chk5,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk5_btn.place(x=390, y=220)

        self.chk10 = tk.IntVar()
        self.chk10_btn = tk.Checkbutton(window, text="10", variable=self.chk10,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk10_btn.place(x=490,y=220)

        self.chk15 = tk.IntVar()
        self.chk15_btn = tk.Checkbutton(window, text="15", variable=self.chk15,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk15_btn.place(x=90, y=250)

        self.chk20 = tk.IntVar()
        self.chk20_btn = tk.Checkbutton(window, text="20", variable=self.chk20,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk20_btn.place(x=190, y=250)

        self.chk30 = tk.IntVar()
        self.chk30_btn = tk.Checkbutton(window, text="30", variable=self.chk30,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk30_btn.place(x=290, y=250)

        self.chk40 = tk.IntVar()
        self.chk40_btn = tk.Checkbutton(window, text="40", variable=self.chk40,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk40_btn.place(x=390, y=250)

        self.chk50 = tk.IntVar()
        self.chk50_btn = tk.Checkbutton(window, text="50", variable=self.chk50,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk50_btn.place(x=490, y=250)

        self.chk60 = tk.IntVar()
        self.chk60_btn = tk.Checkbutton(window, text="60", variable=self.chk60,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk60_btn.place(x=90, y=280)

        self.chk100 = tk.IntVar()
        self.chk100_btn = tk.Checkbutton(window, text="100", variable=self.chk100,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk100_btn.place(x=190, y=280)

        self.chk120 = tk.IntVar()
        self.chk120_btn = tk.Checkbutton(window, text="120", variable=self.chk120,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk120_btn.place(x=290, y=280)

        self.chk200 = tk.IntVar()
        self.chk200_btn = tk.Checkbutton(window, text="200", variable=self.chk200,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk200_btn.place(x=390, y=280)

        self.chk252 = tk.IntVar()
        self.chk252_btn = tk.Checkbutton(window, text="252", variable=self.chk252,command=self.get_mvavg_window_values, onvalue=1,offvalue=0, state="disabled")
        self.chk252_btn.place(x=490, y=280)

        canvas.create_line(30, 350, 800, 350, fill='grey')

        self.kernel_label = tk.Label(window, text="Kernel")
        self.kernel_label.place(x=50, y=380)

        self.Kernel_radio_button = tk.IntVar()
        self.Cosine_rdbtn = tk.Radiobutton(window, text="COSINE", variable=self.Kernel_radio_button, value=1)
        self.Cosine_rdbtn.place(x=220, y=380)

        self.Epanechnikov_rdbtn = tk.Radiobutton(window, text="EPANECHNIKOV", variable=self.Kernel_radio_button, value=2)
        self.Epanechnikov_rdbtn.place(x=380, y=380)

        canvas.create_line(30, 420, 800, 420, fill='grey')

        self.check_daily_returns = tk.IntVar()
        self.Daily_rtn_chk_btn = tk.Checkbutton(window, text="Daily Returns", variable=self.check_daily_returns, onvalue=1,offvalue=0)
        self.Daily_rtn_chk_btn.place(x=50, y=440)

        self.check_log_daily_returns = tk.IntVar()
        self.Log_daily_rtn_chk_btn = tk.Checkbutton(window, text="Log Daily Returns", variable=self.check_log_daily_returns,onvalue=1, offvalue=0)
        self.Log_daily_rtn_chk_btn.place(x=250, y=440)

        self.check_fft_real = tk.IntVar()
        self.fft_real_chk_btn = tk.Checkbutton(window, text="FFT Real", variable=self.check_fft_real, onvalue=1,offvalue=0)
        self.fft_real_chk_btn.place(x=50, y=470)

        self.check_fft_imaginary = tk.IntVar()
        self.fft_imaginary_chk_btn = tk.Checkbutton(window, text="FFT Imaginary", variable=self.check_fft_imaginary, onvalue=1,offvalue=0)
        self.fft_imaginary_chk_btn.place(x=250, y=470)

        canvas.create_line(30, 500, 800, 500, fill='grey')

        self.check_save = tk.IntVar()
        self.save_as_chk_btn = tk.Checkbutton(window, text="Save as txt", variable=self.check_save, onvalue=1, offvalue=0)
        self.save_as_chk_btn.place(x=30, y=530)

        #self.run_btn = tk.StringVar()
        self.run_script_btn = tk.Button(window, text="Run Script",command=self.validate_run_script, width=20)
        self.run_script_btn.place(x=650, y=530)

        self.mvavg_chk_button = tk.IntVar()
        self.mvavg_rdbtn = tk.Checkbutton(window, text="Moving Average Compressed", variable=self.mvavg_chk_button,
                                          onvalue=1, command=lambda :self.enable_mvavg_chkboxes())
        self.mvavg_rdbtn.place(x=50, y=180)


    def enable_mvavg_chkboxes(self):
        if self.mvavg_chk_button.get() == 1:

            self.chk2_btn.config(state="normal")
            self.chk3_btn.config(state="normal")
            self.chk4_btn.config(state="normal")
            self.chk5_btn.config(state="normal")
            self.chk10_btn.config(state="normal")
            self.chk15_btn.config(state="normal")
            self.chk20_btn.config(state="normal")
            self.chk30_btn.config(state="normal")
            self.chk40_btn.config(state="normal")
            self.chk50_btn.config(state="normal")
            self.chk60_btn.config(state="normal")
            self.chk100_btn.config(state="normal")
            self.chk120_btn.config(state="normal")
            self.chk200_btn.config(state="normal")
            self.chk252_btn.config(state="normal")
            self.Sma_rdbtn.config(state="normal")
            self.Ema_rdbtn.config(state="normal")
            self.spinbox.config(state="normal")
        else:
            self.chk2_btn.config(state="disabled")
            self.chk2.set(0)
            self.chk3_btn.config(state="disabled")
            self.chk3.set(0)
            self.chk4_btn.config(state="disabled")
            self.chk4.set(0)
            self.chk5_btn.config(state="disabled")
            self.chk5.set(0)
            self.chk10_btn.config(state="disabled")
            self.chk10.set(0)
            self.chk15_btn.config(state="disabled")
            self.chk15.set(0)
            self.chk20_btn.config(state="disabled")
            self.chk20.set(0)
            self.chk30_btn.config(state="disabled")
            self.chk30.set(0)
            self.chk40_btn.config(state="disabled")
            self.chk40.set(0)
            self.chk50_btn.config(state="disabled")
            self.chk50.set(0)
            self.chk60_btn.config(state="disabled")
            self.chk60.set(0)
            self.chk100_btn.config(state="disabled")
            self.chk100.set(0)
            self.chk120_btn.config(state="disabled")
            self.chk120.set(0)
            self.chk200_btn.config(state="disabled")
            self.chk200.set(0)
            self.chk252_btn.config(state="disabled")
            self.chk252.set(0)
            self.Sma_rdbtn.config(state="disabled")
            self.Ema_rdbtn.config(state="disabled")
            self.sma_ema_radio_button.set(0)
            self.spinbox.config(state="disabled")
            self.spinbox_val.set(0)

    def get_mvavg_window_values(self):
        if self.chk2.get() == 1:
            if 2 not in self.mvavg_window_values:
                self.mvavg_window_values.append(2)
        else:
            if 2 in self.mvavg_window_values:
                self.mvavg_window_values.remove(2)
        if self.chk3.get() == 1:
            if 3 not in self.mvavg_window_values:
                self.mvavg_window_values.append(3)
        else:
            if 3 in self.mvavg_window_values:
                self.mvavg_window_values.remove(3)
        if self.chk4.get() == 1:
            if 4 not in self.mvavg_window_values:
                self.mvavg_window_values.append(4)
        else:
            if 4 in self.mvavg_window_values:
                self.mvavg_window_values.remove(4)
        if self.chk5.get() == 1:
            if 5 not in self.mvavg_window_values:
                self.mvavg_window_values.append(5)
        else:
            if 5 in self.mvavg_window_values:
                self.mvavg_window_values.remove(5)
        if self.chk10.get() == 1:
            if 10 not in self.mvavg_window_values:
                self.mvavg_window_values.append(10)
        else:
            if 10 in self.mvavg_window_values:
                self.mvavg_window_values.remove(10)
        if self.chk15.get() == 1:
            if 15 not in self.mvavg_window_values:
                self.mvavg_window_values.append(15)
        else:
            if 15 in self.mvavg_window_values:
                self.mvavg_window_values.remove(15)
        if self.chk20.get() == 1:
            if 20 not in self.mvavg_window_values:
                self.mvavg_window_values.append(20)
        else:
            if 20 in self.mvavg_window_values:
                self.mvavg_window_values.remove(20)
        if self.chk30.get() == 1:
            if 30 not in self.mvavg_window_values:
                self.mvavg_window_values.append(30)
        else:
            if 30 in self.mvavg_window_values:
                self.mvavg_window_values.remove(30)
        if self.chk40.get() == 1:
            if 40 not in self.mvavg_window_values:
                self.mvavg_window_values.append(40)
        else:
            if 40 in self.mvavg_window_values:
                self.mvavg_window_values.remove(40)
        if self.chk50.get() == 1:
            if 50 not in self.mvavg_window_values:
                self.mvavg_window_values.append(50)
        else:
            if 50 in self.mvavg_window_values:
                self.mvavg_window_values.remove(50)

        if self.chk60.get() == 1:
            if 60 not in self.mvavg_window_values:
                self.mvavg_window_values.append(60)
        else:
            if 60 in self.mvavg_window_values:
                self.mvavg_window_values.remove(60)
        if self.chk100.get() == 1:
            if 100 not in self.mvavg_window_values:
                self.mvavg_window_values.append(100)
        else:
            if 100 in self.mvavg_window_values:
                self.mvavg_window_values.remove(100)
        if self.chk120.get() == 1:
            if 120 not in self.mvavg_window_values:
                self.mvavg_window_values.append(120)
        else:
            if 120 in self.mvavg_window_values:
                self.mvavg_window_values.remove(120)
        if self.chk200.get() == 1:
            if 200 not in self.mvavg_window_values:
                self.mvavg_window_values.append(200)
        else:
            if 200 in self.mvavg_window_values:
                self.mvavg_window_values.remove(200)
        if self.chk252.get() == 1:
            if 252 not in self.mvavg_window_values:
                self.mvavg_window_values.append(252)
        else:
            if 252 in self.mvavg_window_values:
                self.mvavg_window_values.remove(252)

        print(self.mvavg_window_values)


    def input_folder(self):
        IP_Folder.set(filedialog.askdirectory())

    def output_folder(self):
        OP_Folder.set(filedialog.askdirectory())




    def validate_run_script(self):
        if (not IP_Folder.get() and not OP_Folder.get()) or (not IP_Folder.get() and  OP_Folder.get() ) :
            messagebox.showwarning(message="Please select Source data folder")
        elif IP_Folder.get() and not OP_Folder.get():
            #messagebox.askquestion(title='Info', message="Do you want to continue without Destination data folder")
            result = messagebox.askyesno(title='Info', message="Do you want to continue without Destination data folder")
            if result:
                #print(result)
                OP_Folder.set(IP_Folder.get())
        elif not self.dataset_radio_button.get():
            messagebox.showwarning(message="Please select Dataset")
        #elif not self.mvavg_radio_button.get():
        #    messagebox.showwarning(message="Please select Moving Average")
        elif self.mvavg_radio_button.get() == 1 and not self.sma_ema_radio_button.get():
            messagebox.showwarning(message="Please select Moving Average type")
        else:
            self.generate_datasets()

    def create_folder(self,folder_name):
        if not os.path.exists(folder_name):
            os.mkdir(folder_name)


    def generate_datasets(self):
        self.ip_data_folder = IP_Folder.get()
        self.op_data_folder = OP_Folder.get()
        #
        #op_mvavg_data_folder = OP_Folder.get()+'\\MovingAverage'
        if self.dataset_radio_button == 2:
            self.op_sqrt_data_folder = self.op_data_folder+'\\SquareRoot'
            self.create_folder(self.op_sqrt_data_folder)
            algos.square_root(self.ip_data_folder,self.op_sqrt_data_folder)




root = tk.Tk()
my_gui = StockMassuse(root)
root.mainloop()