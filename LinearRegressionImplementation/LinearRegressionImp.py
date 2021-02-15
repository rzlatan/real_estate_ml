import csv


class LinearRegressionImp:

    w_0 = 1
    w_location = 1
    w_square_footage = 1
    w_room_count = 1
    w_year_built =1
    w_floor = 1

    # Learning rate choosen between 1 and 10^-6. 0.1 usually works good for regular cases
    #
    alpha = 0.1

    # Stop the learning when parameter value change for each parameter mets predefined value
    #
    goal_met_value = 0.01

    train_set_file_path = "Data/train_dataset_scaled.csv"
    headers = {
        "Location": 0,
        "Square footage": 1,
        "Floor": 2,
        "Room count": 3,
        "Year built": 4,
        "Price": 5
    }

    @staticmethod
    def data_frame():
        data = []
        with open(file=LinearRegressionImp.train_set_file_path, mode="r", encoding="utf8") as source_file:
            reader = csv.reader(source_file)
            data = list(reader)
        return data

    @staticmethod
    def init_parameters():
        LinearRegressionImp.init_location()
        LinearRegressionImp.init_square_footage()
        LinearRegressionImp.init_room_count()
        LinearRegressionImp.init_year_built()
        LinearRegressionImp.init_floor()
        LinearRegressionImp.init_w0()

    @staticmethod
    def init_location():
        mean_location = LinearRegressionImp.mean("Location")
        mean_price = LinearRegressionImp.mean("Price")

        # Calculating parameter initial value as:
        # sum((xi - mean_x) * (yi - ymean)) / sum((xi - xmean)^2)
        #
        dividend = 0
        divisor = 0

        with open(file=LinearRegressionImp.train_set_file_path, mode="r", encoding="utf8") as source_file:
            reader = csv.reader(source_file)
            for row in reader:
                dividend += (float(row[LinearRegressionImp.headers["Location"]]) - mean_location) * (float(row[LinearRegressionImp.headers["Price"]]) - mean_price)
                divisor += (float(row[LinearRegressionImp.headers["Location"]]) - mean_location) * (float(row[LinearRegressionImp.headers["Location"]]) - mean_location)

        LinearRegressionImp.w_location = dividend / divisor

    @staticmethod
    def init_square_footage():
        mean_square_footage = LinearRegressionImp.mean("Square footage")
        mean_price = LinearRegressionImp.mean("Price")

        # Calculating parameter initial value as:
        # sum((xi - mean_x) * (yi - ymean)) / sum((xi - xmean)^2)
        #
        dividend = 0
        divisor = 0

        with open(file=LinearRegressionImp.train_set_file_path, mode="r", encoding="utf8") as source_file:
            reader = csv.reader(source_file)
            for row in reader:
                dividend += (float(row[LinearRegressionImp.headers["Square footage"]]) - mean_square_footage) * (float(row[LinearRegressionImp.headers["Price"]]) - mean_price)
                divisor += (float(row[LinearRegressionImp.headers["Square footage"]]) - mean_square_footage) * (float(row[LinearRegressionImp.headers["Square footage"]]) - mean_square_footage)

        LinearRegressionImp.w_square_footage = dividend / divisor


    @staticmethod
    def init_room_count():
        mean_room_count = LinearRegressionImp.mean("Room count")
        mean_price = LinearRegressionImp.mean("Price")

        # Calculating parameter initial value as:
        # sum((xi - mean_x) * (yi - ymean)) / sum((xi - xmean)^2)
        #
        dividend = 0
        divisor = 0

        with open(file=LinearRegressionImp.train_set_file_path, mode="r", encoding="utf8") as source_file:
            reader = csv.reader(source_file)
            for row in reader:
                dividend += (float(row[LinearRegressionImp.headers["Room count"]]) - mean_room_count) * (float(row[LinearRegressionImp.headers["Price"]]) - mean_price)
                divisor += (float(row[LinearRegressionImp.headers["Room count"]]) - mean_room_count) * (float(row[LinearRegressionImp.headers["Room count"]]) - mean_room_count)

        LinearRegressionImp.w_room_count = dividend / divisor

    @staticmethod
    def init_year_built():
        mean_year_built = LinearRegressionImp.mean("Year built")
        mean_price = LinearRegressionImp.mean("Price")

        # Calculating parameter initial value as:
        # sum((xi - mean_x) * (yi - ymean)) / sum((xi - xmean)^2)
        #
        dividend = 0
        divisor = 0

        with open(file=LinearRegressionImp.train_set_file_path, mode="r", encoding="utf8") as source_file:
            reader = csv.reader(source_file)
            for row in reader:
                dividend += (float(row[LinearRegressionImp.headers["Year built"]]) - mean_year_built) * (float(row[LinearRegressionImp.headers["Price"]]) - mean_price)
                divisor += (float(row[LinearRegressionImp.headers["Year built"]]) - mean_year_built) * (float(row[LinearRegressionImp.headers["Year built"]]) - mean_year_built)

        LinearRegressionImp.w_year_built = dividend / divisor

    @staticmethod
    def init_floor():
        mean_floor = LinearRegressionImp.mean("Floor")
        mean_price = LinearRegressionImp.mean("Price")

        # Calculating parameter initial value as:
        # sum((xi - mean_x) * (yi - ymean)) / sum((xi - xmean)^2)
        #
        dividend = 0
        divisor = 0

        with open(file=LinearRegressionImp.train_set_file_path, mode="r", encoding="utf8") as source_file:
            reader = csv.reader(source_file)
            for row in reader:
                dividend += (float(row[LinearRegressionImp.headers["Floor"]]) - mean_floor) * (float(row[LinearRegressionImp.headers["Price"]]) - mean_price)
                divisor += (float(row[LinearRegressionImp.headers["Floor"]]) - mean_floor) * (float(row[LinearRegressionImp.headers["Floor"]]) - mean_floor)

        LinearRegressionImp.w_floor = dividend / divisor

    @staticmethod
    def init_w0():
        mean_y = LinearRegressionImp.mean("Price")
        LinearRegressionImp.w_0 = mean_y -\
            ((LinearRegressionImp.w_location * LinearRegressionImp.mean("Location") +\
              LinearRegressionImp.w_square_footage * LinearRegressionImp.mean("Square footage") +\
              LinearRegressionImp.w_floor * LinearRegressionImp.mean("Floor")) +\
              LinearRegressionImp.w_room_count * LinearRegressionImp.mean("Room count") +\
              LinearRegressionImp.w_year_built * LinearRegressionImp.mean("Year built"))\
              / 5.0


    @staticmethod
    def mean(param):
        val = 0
        cnt = 0
        with open(file=LinearRegressionImp.train_set_file_path, mode="r", encoding="utf8") as source_file:
            reader = csv.reader(source_file)
            for row in reader:
                val += float(row[LinearRegressionImp.headers[param]])
                cnt += 1
        return val/cnt

    @staticmethod
    def h_x(location, square_footage, room_count, year_built, floor):
        return LinearRegressionImp.w_0 +\
               LinearRegressionImp.w_location * location +\
               LinearRegressionImp.w_square_footage * square_footage +\
               LinearRegressionImp.w_room_count * room_count +\
               LinearRegressionImp.w_year_built * year_built +\
               LinearRegressionImp.w_floor * floor

    @staticmethod
    def dJdwO(data_frame):
        m = float(len(data_frame))
        sum = 0.0
        for row in data_frame:
            location = float(row[LinearRegressionImp.headers["Location"]])
            square_footage = float(row[LinearRegressionImp.headers["Square footage"]])
            floor = float(row[LinearRegressionImp.headers["Floor"]])
            year_built = float(row[LinearRegressionImp.headers["Year built"]])
            room_count = float(row[LinearRegressionImp.headers["Room count"]])
            y = float(row[LinearRegressionImp.headers["Price"]])
            sum += LinearRegressionImp.h_x(location, square_footage, room_count, year_built, floor) - y

        return sum / m

    @staticmethod
    def dJdw_param(data_frame, param):
        m = float(len(data_frame))
        sum = 0.0
        for row in data_frame:
            location = float(row[LinearRegressionImp.headers["Location"]])
            square_footage = float(row[LinearRegressionImp.headers["Square footage"]])
            floor = float(row[LinearRegressionImp.headers["Floor"]])
            year_built = float(row[LinearRegressionImp.headers["Year built"]])
            room_count = float(row[LinearRegressionImp.headers["Room count"]])
            y = float(row[LinearRegressionImp.headers["Price"]])
            sum += (LinearRegressionImp.h_x(location, square_footage, room_count, year_built, floor) - y) * float(row[LinearRegressionImp.headers[param]])

        return sum / m

    @staticmethod
    def stop_goal_met(d_wo, d_location, d_square_footage, d_floor, d_room_count, d_year_built):
        print("Goal - " + str(LinearRegressionImp.goal_met_value))
        print("Delta w0 " + str(d_wo))
        print("Delta location " + str(d_location))
        print("Delta square footage " + str(d_square_footage))
        print("Delta floor " + str(d_floor))
        print("Delta room count " + str(d_room_count))
        print("Delta year built " + str(d_year_built))

        target = LinearRegressionImp.goal_met_value
        return abs(d_wo) < target and abs(d_location) < target and abs(d_room_count) < target and abs(d_floor) < target and abs(d_year_built) < target and abs(d_square_footage) < target

    @staticmethod
    def train():
        goal_met = False
        df = LinearRegressionImp.data_frame()

        while not goal_met:
            delta_w0 = LinearRegressionImp.alpha * LinearRegressionImp.dJdwO(df)
            delta_location = LinearRegressionImp.alpha * LinearRegressionImp.dJdw_param(df, "Location")
            delta_square_footage = LinearRegressionImp.alpha * LinearRegressionImp.dJdw_param(df, "Square footage")
            delta_floor = LinearRegressionImp.alpha * LinearRegressionImp.dJdw_param(df, "Floor")
            delta_room_count = LinearRegressionImp.alpha * LinearRegressionImp.dJdw_param(df, "Room count")
            delta_year_built = LinearRegressionImp.alpha * LinearRegressionImp.dJdw_param(df, "Year built")

            LinearRegressionImp.w_0 = LinearRegressionImp.w_0 - delta_w0
            LinearRegressionImp.w_location = LinearRegressionImp.w_location - delta_location
            LinearRegressionImp.w_square_footage = LinearRegressionImp.w_square_footage - delta_square_footage
            LinearRegressionImp.w_floor = LinearRegressionImp.w_floor - delta_floor
            LinearRegressionImp.w_room_count = LinearRegressionImp.w_room_count - delta_room_count
            LinearRegressionImp.w_year_built = LinearRegressionImp.w_year_built - delta_year_built

            if LinearRegressionImp.stop_goal_met(delta_w0, delta_location, delta_square_footage, delta_floor, delta_room_count, delta_year_built):
                goal_met = True
