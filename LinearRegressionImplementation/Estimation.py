from LinearRegressionImp import LinearRegressionImp
from Scaling import ParameterScaling
import csv

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

while True:
    location = ParameterScaling.ParameterScaling.get_location_cost(input("Enter location: "))
    square_footage = ParameterScaling.ParameterScaling.get_square_footage_cost(input("Enter square footage: "))
    room_count = ParameterScaling.ParameterScaling.get_room_count_cost(input("Enter room count: "))
    floor = ParameterScaling.ParameterScaling.get_floor_cost(input("Enter floor: "))
    year_built = ParameterScaling.ParameterScaling.get_year_built_cost(input("Enter year built: "))

    h_x = LinearRegressionImp.h_x(location, square_footage, room_count, year_built, floor) * 1000.0
    print("Estimated price: " + str(h_x))