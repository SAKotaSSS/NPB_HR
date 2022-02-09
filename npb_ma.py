import pandas as pd
import glob

csv_files = glob.glob('C:/Users/こたろ～/PycharmProjects/npb_hr/*.csv')
li = []
print(csv_files)
for f in csv_files:
    li.append(pd.read_csv(f))

print(li)
dd = pd.concat(li, ignore_index=True)
dd.to_csv("npb_h.csv", index=False)