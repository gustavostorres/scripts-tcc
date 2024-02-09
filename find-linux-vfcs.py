import pandas as pd

bigvul = pd.read_csv("D:/Área de Trabalho/MSR_data_cleaned.csv", low_memory=False)
linux = bigvul[bigvul["project"] == 'linux']
linux.to_excel("D:/Área de Trabalho/linux.xlsx", sheet_name="linux", index=False)