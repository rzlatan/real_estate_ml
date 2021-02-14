import pandas
import matplotlib.pyplot as plt

headers = ['Opstina', 'Broj nekretnina']
content = pandas.read_csv("../Results/BelgradeMunicipalitiesWithMostRealEstates.csv", names=headers)

print(content)
content.plot.bar(x='Opstina', y='Broj nekretnina')
plt.tick_params(axis="x", labelsize=8, rotation=45)
plt.show()
