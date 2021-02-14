import pandas
import matplotlib.pyplot as plt

headers = ['CATEGORY', 'CATEGORY_COUNT', 'PERCENTAGE']
content = pandas.read_csv("../Results/RealEstatesPerPriceCategory.csv", names=headers)
reorder_list = ["manje od 49 999", "izmedju 50 000 i 99 999", "izmedju 100 000 i 149 999", "izmedju 150 000 i 199 999", "vise od 200 000"]
content["CATEGORY"] = pandas.Categorical(content["CATEGORY"], reorder_list)
content = content.sort_values(["CATEGORY"])

print(content)
content.plot(x="CATEGORY", y=["CATEGORY_COUNT"], kind="bar")
plt.tick_params(axis="x", labelsize=8, rotation=45)
plt.show()


content.plot(x="CATEGORY", y=["PERCENTAGE"], kind="bar")
plt.tick_params(axis="x", labelsize=8, rotation=45)
plt.show()