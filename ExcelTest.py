import pandas as pd
import xlrd

aa = "D:/test/pythonTest.xlsx"
df = pd.DataFrame(pd.read_excel(aa))
df1 = df[['标题','内容']]
print(df1)


