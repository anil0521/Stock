import tkinter as tk
from tkinter import filedialog
class StockMassuse():

    def __init__(self,window):

        self.window = window
        window.title("Stock Masseuse")
        window.geometry("1000x700")

        canvas = tk.Canvas(window, width=1800, height=1400)
        canvas.pack()

        global IP_Folder
        global OP_Folder

        IP_Folder = None
        OP_Folder = None

        tk.Label(window, text="Input Folder :").place(x=62, y=60)
        #print('after label')
        tk.Entry(window, textvariable=IP_Folder).place(x=140, y=60)
        tk.Button(window, text="Browse").place(x=280, y=55)

        tk.Label(window, text="Output Folder :").place(x=50, y=90)
        tk.Entry(window, textvariable=OP_Folder).place(x=140, y=90)
        tk.Button(window, text="Browse").place(x=280, y=85)

        canvas.create_line(30, 120, 800, 120, fill='grey')

        self.dataset_radio_button = tk.IntVar()
        self.Raw_rdbtn = tk.Radiobutton(window, text="Raw / EOD Download Type", variable=self.dataset_radio_button, value=1)
        self.Raw_rdbtn.place(x=50, y=140)

        self.Square_rdbtn = tk.Radiobutton(window, text="Square Root", variable=self.dataset_radio_button, value=2)
        self.Square_rdbtn.place(x=450, y=140)

        canvas.create_line(30, 170, 800, 170, fill='grey')
        self.mvavg_radio_button = tk.IntVar()
        self.mvavg_rdbtn = tk.Radiobutton(window, text="Moving Average Compressed", variable=self.mvavg_radio_button, value=1)
        self.mvavg_rdbtn.place(x=50,y=180)

        self.spinbox = tk.Spinbox(window, from_=0, to=252)
        self.spinbox.place(x=490, y=180)

        self.sma_ema_radio_button = tk.IntVar()
        self.Sma_rdbtn = tk.Radiobutton(window, text="SMA", variable=self.sma_ema_radio_button, value=1)
        self.Sma_rdbtn.place(x=150, y=320)

        self.Ema_rdbtn = tk.Radiobutton(window, text="EMA", variable=self.sma_ema_radio_button, value=2)
        self.Ema_rdbtn.place(x=340, y=320)

        self.chk2 = tk.IntVar()
        self.chk2_btn = tk.Checkbutton(window, text="2", variable=self.chk2, onvalue=1, offvalue=0, state="disabled")
        self.chk2_btn.place(x=90,y=220)

        self.chk3 = tk.IntVar()
        self.chk3_btn = tk.Checkbutton(window, text="3", variable=self.chk3, onvalue=1, offvalue=0, state="disabled")
        self.chk3_btn.place(x=190, y=220)

        self.chk4 = tk.IntVar()
        self.chk4_btn = tk.Checkbutton(window, text="4", variable=self.chk4, onvalue=1, offvalue=0, state="disabled")
        self.chk4_btn.place(x=290, y=220)

        chk5 = tk.IntVar()
        chk5_btn = tk.Checkbutton(window, text="5", variable=chk5, onvalue=1, offvalue=0, state="disabled")
        chk5_btn.place(x=390, y=220)

        self.chk10 = tk.IntVar()
        self.chk10_btn = tk.Checkbutton(window, text="10", variable=self.chk10, onvalue=1, offvalue=0, state="disabled")
        self.chk10_btn.place(x=490,y=220)

        self.chk15 = tk.IntVar()
        self.chk15_btn = tk.Checkbutton(window, text="15", variable=self.chk15, onvalue=1, offvalue=0, state="disabled")
        self.chk15_btn.place(x=90, y=250)

        self.chk20 = tk.IntVar()
        self.chk20_btn = tk.Checkbutton(window, text="20", variable=self.chk20, onvalue=1, offvalue=0, state="disabled")
        self.chk20_btn.place(x=190, y=250)

        self.chk30 = tk.IntVar()
        self.chk30_btn = tk.Checkbutton(window, text="30", variable=self.chk30, onvalue=1, offvalue=0, state="disabled")
        self.chk30_btn.place(x=290, y=250)

        self.chk40 = tk.IntVar()
        self.chk40_btn = tk.Checkbutton(window, text="40", variable=self.chk40, onvalue=1, offvalue=0, state="disabled")
        self.chk40_btn.place(x=390, y=250)

        self.chk50 = tk.IntVar()
        self.chk50_btn = tk.Checkbutton(window, text="50", variable=self.chk50, onvalue=1, offvalue=0, state="disabled")
        self.chk50_btn.place(x=490, y=250)

        self.chk60 = tk.IntVar()
        self.chk60_btn = tk.Checkbutton(window, text="60", variable=self.chk60, onvalue=1, offvalue=0, state="disabled")
        self.chk60_btn.place(x=90, y=280)

        self.chk100 = tk.IntVar()
        self.chk100_btn = tk.Checkbutton(window, text="100", variable=self.chk100, onvalue=1, offvalue=0, state="disabled")
        self.chk100_btn.place(x=190, y=280)

        self.chk120 = tk.IntVar()
        self.chk120_btn = tk.Checkbutton(window, text="120", variable=self.chk120, onvalue=1, offvalue=0, state="disabled")
        self.chk120_btn.place(x=290, y=280)

        self.chk200 = tk.IntVar()
        self.chk200_btn = tk.Checkbutton(window, text="200", variable=self.chk200, onvalue=1, offvalue=0, state="disabled")
        self.chk200_btn.place(x=390, y=280)

        self.chk252 = tk.IntVar()
        self.chk252_btn = tk.Checkbutton(window, text="252", variable=self.chk252, onvalue=1, offvalue=0, state="disabled")
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
        self.fft_imaginary_chk_btn = tk.Checkbutton(window, text="FFT Real", variable=self.check_fft_imaginary, onvalue=1,offvalue=0)
        self.fft_imaginary_chk_btn.place(x=250, y=470)

        canvas.create_line(30, 500, 800, 500, fill='grey')

        self.check_save = tk.IntVar()
        self.save_as_chk_btn = tk.Checkbutton(window, text="Save as txt", variable=self.check_save, onvalue=1, offvalue=0)
        self.save_as_chk_btn.place(x=30, y=530)

        self.run_script_btn = tk.Button(window, text="Run Script", width=20)
        self.run_script_btn.place(x=650, y=530)


root = tk.Tk()
my_gui = StockMassuse(root)
root.mainloop()