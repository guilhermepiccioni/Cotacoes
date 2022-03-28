import pandas as pd
import os

current_path = os.getcwd()
files = os.listdir(current_path)

file_xlsx = [file for file in files if file[-4:] == 'xlsx']

df = pd.DataFrame()

for file in file_xlsx:
    data = pd.read_excel(file)
    print(f"\n{data}")
