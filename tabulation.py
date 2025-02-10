import pandas as pd
print(pd.__version__) 

# Открываем исходный файл с табуляцией в формте txt
df = pd.read_csv("PLU.txt", delimiter="\t")

# Сохраняем в CSV с запятыми
df.to_csv("PLU.csv", index=False)

print("Файл успешно сохранён в формате CSV!")