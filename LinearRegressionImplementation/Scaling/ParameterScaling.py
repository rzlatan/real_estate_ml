class ParameterScaling:
    location_cost = {
        "Vračar": 0.1,
        "Čukarica": 0.9,
        "Rakovica opština":0.95,
        "Zvezdara opština": 0.5,
        "Stari Grad opština": 0.05,
        "Neimar": 0.3,
        "Obrenovac opština": 1.0,
        "Palilula": 0.65,
        "Zemun opština": 0.75,
        "Savski Venac": 0.15,
        "Voždovac opština": 0.45,
        "Palilula opština": 0.65,
        "Zemun": 0.75,
        "Novi Beograd": 0.25,
        "Savamala": 0.05,
        "Bežanijski Blokovi": 0.8,
        "Blok 34": 0.7,
        "Blok 11": 0.75,
        "Konjarnik": 0.65,
        "Dorćol": 0.05,
        "Grocka opština": 1.0,
        "Čukarica opština": 0.9,
        "Medaković": 0.7,
        "Vidikovac": 0.9,
        "Bežanijska kosa": 0.7,
        "Voždovac": 0.45,
        "Mladenovac opština": 1.0,
        "Kosančićev Venac": 0.02,
        "Padinska Skela": 1.0,
        "Beograd centar": 0.1,
        "Mirijevo": 0.5,
        "Beograd": 0.5,
        "Terazije": 0.05,
        "Donji Dorćol": 0.05,
        "Karaburma": 0.6
    }

    @staticmethod
    def get_location_cost(location):
        if location is None or location == 'NULL' or location == '':
            return 0.5
        return 1 - ParameterScaling.location_cost[location]

    min_year = 1923.0
    max_year = 2021.0

    @staticmethod
    def get_year_built_cost(year_built):
        if year_built is None or year_built == 'NULL' or year_built == '':
            return 0.5
        val = float(year_built)

        return (ParameterScaling.max_year - val) / (ParameterScaling.max_year - ParameterScaling.min_year)

    min_square_footage = 16;
    max_square_footage = 150;

    @staticmethod
    def get_square_footage_cost(square_footage):
        if square_footage is None or square_footage == 'NULL' or square_footage == '':
            return 0.5
        val = float(square_footage)

        if val > 150:
            return 1
        return (val - ParameterScaling.min_square_footage) / (ParameterScaling.max_square_footage - ParameterScaling.min_square_footage)

    min_room_count = 0.5
    max_room_count = 5

    @staticmethod
    def get_room_count_cost(room_count):
        if room_count is None or room_count == 'NULL' or room_count == '':
            return 0.5
        val = float(room_count)

        if val > 5:
            return 1
        return (val - ParameterScaling.min_room_count) / (ParameterScaling.max_room_count - ParameterScaling.min_room_count)

    min_floor = 1
    max_floor = 15

    @staticmethod
    def get_floor_cost(floor):
        if floor is None or floor == 'NULL' or floor == '':
            return 0.5
        val = float(floor)

        if val > 15:
            return 1

        return (val - ParameterScaling.min_floor) / (ParameterScaling.max_floor - ParameterScaling.min_floor)
