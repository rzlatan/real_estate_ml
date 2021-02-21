from LinearRegressionImp import LinearRegressionImp
from Scaling import ParameterScaling
import csv
import math


LinearRegressionImp.init_parameters()
print("Estimated initial parameters:")
print("W_0: " + str(LinearRegressionImp.w_0))
print("W_location: " + str(LinearRegressionImp.w_location))
print("W_square_footage: " + str(LinearRegressionImp.w_square_footage))
print("W_room_count: " + str(LinearRegressionImp.w_room_count))
print("W_floor: " + str(LinearRegressionImp.w_floor))
print("W_year_built: " + str(LinearRegressionImp.w_year_built))

LinearRegressionImp.train()

print("Estimated parameters:")
print("W_0: " + str(LinearRegressionImp.w_0))
print("W_location: " + str(LinearRegressionImp.w_location))
print("W_square_footage: " + str(LinearRegressionImp.w_square_footage))
print("W_room_count: " + str(LinearRegressionImp.w_room_count))
print("W_floor: " + str(LinearRegressionImp.w_floor))
print("W_year_built: " + str(LinearRegressionImp.w_year_built))

m = 0
RMSE = 0
MAE = 0

with open("Data/test_dataset_scaled.csv", mode='r', encoding='utf8') as test_file:
    reader = csv.reader(test_file)
    for row in reader:
        location = float(row[LinearRegressionImp.headers["Location"]])
        square_footage = float(row[LinearRegressionImp.headers["Square footage"]])
        room_count = float(row[LinearRegressionImp.headers["Room count"]])
        floor = float(row[LinearRegressionImp.headers["Floor"]])
        year_built = float(row[LinearRegressionImp.headers["Year built"]])
        price = float(row[LinearRegressionImp.headers["Price"]]) * 1000.0

        h_x = LinearRegressionImp.h_x(location, square_footage, room_count, year_built, floor) * 1000.0
        print("Estimated price: " + str(h_x) + ", Real price: " + str(price) + ", Miss " + str(h_x - price))

        RMSE += pow(h_x - price, 2)
        MAE += abs(h_x - price)
        m += 1


RMSE = math.sqrt(RMSE * 1.0 / m)
MAE = MAE * 1.0 / m
print("Root mean squared error: " + str(RMSE))
print("Mean absolute error: " + str(MAE))

