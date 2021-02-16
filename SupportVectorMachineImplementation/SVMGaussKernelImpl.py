import csv
from sklearn.svm import SVC
from sklearn.metrics import classification_report

headers = {
    "Location": 0,
    "Square footage": 1,
    "Floor count": 2,
    "Room count": 3,
    "Year built": 4,
    "Satisfaction": 5
}

train_file_path = "Data\\train_dataset_scaled.csv"
file = open(train_file_path, encoding="utf8")
data = csv.reader(file)


train_y_data = []
train_x_data = []

for row in data:
    train_x_data.append([row[headers["Location"]], row[headers["Square footage"]], row[headers["Floor count"]], row[headers["Room count"]], row[headers["Year built"]]])
    train_y_data.append(row[headers["Satisfaction"]])


classifier = SVC(kernel='rbf')
classifier.fit(train_x_data, train_y_data)

test_file_path = "Data\\test_dataset_scaled.csv"
test_file = open(test_file_path, encoding="utf8")
test_data = csv.reader(test_file)

test_x_data = []
test_y_data = []

for row in test_data:
    test_x_data.append([row[headers["Location"]], row[headers["Square footage"]], row[headers["Floor count"]], row[headers["Room count"]], row[headers["Year built"]]])
    test_y_data.append(row[headers["Satisfaction"]])

y_predicted = classifier.predict(test_x_data)

correct = 0
wrong = 0

for i in range(len(y_predicted)):
    if y_predicted[i] == test_y_data[i]:
        correct += 1
    else:
        wrong += 1

print("Correct predictions: " + str(correct) + "(" + str(correct * 100.0 / (correct + wrong)) + "%)")
print("Wrong predictions: " + str(wrong) + "(" + str(wrong * 100.0 / (correct + wrong)) + "%)")
print("")
print(classification_report(test_y_data, y_predicted))
