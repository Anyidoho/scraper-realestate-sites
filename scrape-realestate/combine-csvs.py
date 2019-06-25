import os
import pandas as pd


file_list = list()

for file in os.listdir():
    if file.startswith('meqasa_'):
        df = pd.read_csv(file)
        file_list.append(df)

meqasa_all = pd.concat(file_list, axis=0, ignore_index=True)
meqasa_all.to_csv('meqasa_all.csv')


print("**************File Generated Successfully********************")