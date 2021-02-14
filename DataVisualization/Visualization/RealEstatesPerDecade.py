import pandas
import matplotlib.pyplot as plt

headers = ['Decenija', 'Broj nekretnina']
content = pandas.read_csv("../Results/RealEstatesPerDecade.csv", names=headers)
reorder_list = ["Pre 1950", "Od 1950 do 1960", "Od 1960 do 1969", "Od 1970 do 1979", "Od 1980 do 1989", "Od 1990 do 1999", "Od 2000 do 2009", "Od 2010 do 2019", "Posle 2020"]
content["Decenija"] = pandas.Categorical(content["Decenija"], reorder_list)
content = content.sort_values(["Decenija"])

print(content)
content.plot.bar(x='Decenija', y='Broj nekretnina')
plt.tick_params(axis="x", labelsize=8, rotation=45)
plt.show()
