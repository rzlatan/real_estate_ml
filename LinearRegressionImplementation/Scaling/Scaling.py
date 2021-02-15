from ParameterScaling import ParameterScaling
import csv

test_dataset_file_path = '../Data/test_dataset_without_scaling.csv'
train_dataset_file_path = '../Data/train_dataset_without_scaling.csv'

target_test_dataset = '../Data/test_dataset_scaled.csv'
target_train_dataset = '../Data/train_dataset_scaled.csv'

price_scaling_factor = 1000

headers = {
    "MUNICIPALITY": 4,
    "SQUARE_FOOTAGE": 5,
    "ROOM_COUNT": 16,
    "YEAR_BUILT": 6,
    "FLOOR": 9,
    "PRICE": 18
}

train_dataset_before_scaling_file = open(train_dataset_file_path, encoding="utf8")
train_dataset_before_scaling = csv.reader(train_dataset_before_scaling_file)

with open(target_train_dataset, mode='w', newline='', encoding='utf8') as train_file:
    writer = csv.writer(train_file)

    for row in train_dataset_before_scaling:
        location_scaled = ParameterScaling.get_location_cost(row[headers["MUNICIPALITY"]])
        square_footage_scaled = ParameterScaling.get_square_footage_cost(row[headers["SQUARE_FOOTAGE"]])
        floor_scaled = ParameterScaling.get_floor_cost(row[headers["FLOOR"]])
        room_count_scaled = ParameterScaling.get_room_count_cost(row[headers["ROOM_COUNT"]])
        year_built_scaled = ParameterScaling.get_year_built_cost(row[headers["YEAR_BUILT"]])
        price = float(row[headers["PRICE"]]) / price_scaling_factor

        scaled_row = [location_scaled, square_footage_scaled, floor_scaled, room_count_scaled, year_built_scaled, price]
        print(scaled_row)
        writer.writerow(scaled_row)


test_dataset_before_scaling_file = open(test_dataset_file_path, encoding="utf8")
test_dataset_before_scaling = csv.reader(test_dataset_before_scaling_file)

with open(target_test_dataset, mode='w', newline='', encoding='utf8') as test_file:
    writer = csv.writer(test_file)

    for row in test_dataset_before_scaling:
        location_scaled = ParameterScaling.get_location_cost(row[headers["MUNICIPALITY"]])
        square_footage_scaled = ParameterScaling.get_square_footage_cost(row[headers["SQUARE_FOOTAGE"]])
        floor_scaled = ParameterScaling.get_floor_cost(row[headers["FLOOR"]])
        room_count_scaled = ParameterScaling.get_room_count_cost(row[headers["ROOM_COUNT"]])
        year_built_scaled = ParameterScaling.get_year_built_cost(row[headers["YEAR_BUILT"]])
        price = float(row[headers["PRICE"]]) / price_scaling_factor


        scaled_row = [location_scaled, square_footage_scaled, floor_scaled, room_count_scaled, year_built_scaled, price]
        print(scaled_row)
        writer.writerow(scaled_row)