import pandas
import matplotlib.pyplot as plt

headers = ['Kategorija', 'Broj stanova']
content = pandas.read_csv("../Results/FlatsBySquareFootage.csv", names=headers)
reorder_list = ["do 35", "od 35 do 50", "od 50 do 65", "od 65 do 80", "od 80 do 95", "od 95 do 110", "od 110 do 140", "141 i vise"]
content["Kategorija"] = pandas.Categorical(content["Kategorija"], reorder_list)
content = content.sort_values(["Kategorija"])

print(content)
content.plot.bar(x='Kategorija', y='Broj stanova')
plt.tick_params(axis="x", labelsize=8, rotation=45)
plt.show()
