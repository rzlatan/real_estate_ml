import pandas
import matplotlib.pyplot as plt

headers = ['Izdavanje', 'Prodaja', 'Grad', 'Procentualni odnos', "Ukupno nekretnina"]
content = pandas.read_csv("../Results/SellingVsRentingRatioForTop8Cities.csv", names=headers)


print(content)
content.plot(x="Grad", y=["Izdavanje", "Prodaja", "Procentualni odnos"], kind="bar")
plt.tick_params(axis="x", labelsize=8, rotation=45)
plt.show()
