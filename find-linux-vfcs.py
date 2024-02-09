import pandas as pd

bigvul = pd.read_csv("file/path/csv-bigvul", low_memory=False)
linux = bigvul[bigvul["project"] == 'linux']
linux.to_excel("D:/Área de Trabalho/linux.xlsx", sheet_name="linux", index=False)
