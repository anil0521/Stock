import pandas as pd
import numpy as np
import os
import glob
import re


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

def get_file_name(file,calc_type):
    pattern = re.compile(r'[A-Z]+')
    data = pattern.match(file)
    file_name = data.group()+'_'+calc_type+'.txt'
    return file_name

def Average(ip_folder,op_folder):
    os.chdir(ip_folder)
    files = glob.glob('*.txt')
    for each_file in files:
        print(each_file)
        df = pd.read_csv(each_file)
        df.columns = ['Symbol','Date','Open','High','Low','Close','Volume']
    #print(df.head(5))
        df['Avg'] = round(df.iloc[:,2:5].mean(axis=1),2)
        df['Open'] = df["Avg"]
        df['High'] = df['Avg']
        df['Low'] = df['Avg']
        df['Close'] = df['Avg']
        del df['Avg']
        #os.chdir(op_folder)
        file_name = get_file_name(each_file,'Avg')
        df.to_csv(op_folder+'\\'+file_name,header=False,index=False)

#Average(r'C:\Users\oc-anils\Desktop\Freelance\Stock_symbol\ascending type',r'C:\Users\oc-anils\Desktop\Freelance\Stock_symbol')
def square_root(ip_folder,op_folder):
    os.chdir(ip_folder)
    files = glob.glob('*.txt')
    for each_file in files:
        print(each_file)
        df = pd.read_csv(each_file)
        df.columns = ['Symbol', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        df['Open'] = round(np.sqrt(df['Open']), 2)
        df['High'] = round(np.sqrt(df['High']), 2)
        df['Low'] = round(np.sqrt(df['Low']), 2)
        df['Close'] = round(np.sqrt(df['Close']), 2)
        #file_name = get_file_name(each_file, 'Sqrt')
        df.to_csv(op_folder + '\\' + each_file, header=False, index=False)



#square_root(r'C:\Users\oc-anils\Desktop\Freelance\Stock_symbol\ascending type',r'C:\Users\oc-anils\Desktop\Freelance\Stock_symbol')

def Log(ip_folder,op_folder):
    os.chdir(ip_folder)
    files = glob.glob('*.txt')
    for each_file in files:
        print(each_file)
        df = pd.read_csv(each_file)
        df.columns = ['Symbol', 'Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        df['Open'] = round(np.log(df['Open']), 2)
        df['High'] = round(np.log(df['High']), 2)
        df['Low'] = round(np.log(df['Low']), 2)
        df['Close'] = round(np.log(df['Close']), 2)
        file_name = get_file_name(each_file, 'log')
        df.to_csv(op_folder + '\\' + file_name, header=False, index=False)

#Log(r'C:\Users\oc-anils\Desktop\Freelance\Stock_symbol\ascending type',r'C:\Users\oc-anils\Desktop\Freelance\Stock_symbol')
