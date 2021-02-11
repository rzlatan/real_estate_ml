class RealEstate:
    def __init__(self,
                 object_type,
                 offer_type,
                 city,
                 municipality,
                 square_footage,
                 year_built,
                 construction_state,
                 land_area,
                 floor,
                 heating_system,
                 equipment_state,
                 has_elevator,
                 has_garage,
                 has_parking,
                 registration_state,
                 room_count,
                 bathroom_count,
                 price,
                 description):
        self.object_type = object_type
        self.offer_type = offer_type
        self.city = city
        self.municipality = municipality
        self.square_footage = square_footage
        self.year_built = year_built
        self.construction_state = construction_state
        self.land_area = land_area
        self.floor = floor
        self.heating_system = heating_system
        self.equipment_state = equipment_state
        self.has_elevator = has_elevator
        self.has_garage = has_garage
        self.has_parking = has_parking
        self.registration_state = registration_state
        self.room_count = room_count
        self.bathroom_count = bathroom_count
        self.price = price
        self.description = description

    def __init__(self):
        self.object_type = None
        self.offer_type = None
        self.city = None
        self.municipality = None
        self.square_footage = None
        self.year_built = None
        self.construction_state = None
        self.land_area = None
        self.floor = None
        self.heating_system = None
        self.equipment_state = None
        self.has_elevator = None
        self.has_garage = None
        self.has_parking = None
        self.registration_state = None
        self.room_count = None
        self.bathroom_count = None
        self.price = None
        self.description = None

    def set_object_type(self, object_type):
        self.object_type = object_type

    def get_object_type(self):
        return self.object_type

    def set_offer_type(self, offer_type):
        self.offer_type = offer_type

    def get_offer_type(self):
        return self.offer_type

    def set_city(self, city):
        self.city = city

    def get_city(self):
        return self.city

    def set_municipality(self, municipality):
        self.municipality = municipality

    def get_municipality(self):
        return self.municipality

    def set_square_footage(self, square_footage):
        self.square_footage = square_footage

    def get_square_footage(self):
        return self.square_footage

    def set_year_built(self, year_built):
        self.year_built = year_built

    def get_year_built(self):
        return self.year_built

    def set_construction_state(self, construction_state):
        self.construction_state = construction_state

    def get_is_new_construction(self):
        return self.construction_state

    def set_land_area (self, land_area):
        self.land_area = land_area

    def get_land_area(self):
        return self.land_area

    def set_floor(self, floor):
        self.floor = floor

    def get_floor(self):
        return self.floor

    def set_heating_system(self, heating_system):
        self.heating_system = heating_system

    def get_heating_system(self):
        return self.heating_system

    def set_equipment_state(self, equipment_state):
        self.equipment_state = equipment_state

    def get_equipment_state(self):
        return self.equipment_state

    def set_has_elevator(self, has_elevator):
        self.has_elevator = has_elevator

    def get_has_elevator(self):
        return self.has_elevator

    def set_has_garage(self, has_garage):
        self.has_garage = has_garage

    def get_has_garage(self):
        return self.has_garage

    def set_has_parking(self, has_parking):
        return self.has_parking

    def set_registration_state(self, registration_state):
        self.registration_state = registration_state

    def get_registration_state(self):
        return self.registration_state

    def set_room_count(self, room_count):
        self.room_count = room_count

    def get_room_count(self):
        return self.room_count

    def set_bathroom_count(self, bathroom_count):
        self.bathroom_count = bathroom_count

    def get_bathroom_count(self):
        return self.bathroom_count

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
