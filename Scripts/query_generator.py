from real_estate_model import RealEstate

class QueryGenerator:

    @staticmethod
    def insert_real_estate_query(real_estate: RealEstate):
        values = []
        statement = "INSERT INTO `real_estate_tbl`("

        if real_estate.object_type is not None:
            values.append("'" + real_estate.object_type +"'")
            statement += "`OBJECT_TYPE`"

        if real_estate.offer_type is not None:
            values.append("'" + real_estate.offer_type + "'")
            statement += ",`OFFER_TYPE`"

        if real_estate.city is not None:
            values.append("'" + real_estate.city + "'")
            statement += ",`CITY`"

        if real_estate.municipality is not None:
            values.append("'" + real_estate.municipality + "'")
            statement += ", `MUNICIPALITY`"

        if real_estate.square_footage is not None:
            values.append(real_estate.square_footage)
            statement += ", `SQUARE_FOOTAGE`"

        if real_estate.year_built is not None:
            values.append(real_estate.year_built)
            statement += ", `YEAR_BUILT`"

        if real_estate.is_new_construction is not None:
            values.append(real_estate.is_new_construction)
            statement += ", 'IS_NEW_CONSTRUCTION'"

        if real_estate.land_area is not None:
            values.append(real_estate.land_area)
            statement += ", `LAND_AREA`"

        if real_estate.floor is not None:
            values.append(real_estate.floor)
            statement += ", `FLOOR`"

        if real_estate.is_registered is not None:
            values.append(real_estate.is_registered)
            statement += ", `IS_REGISTERED`"

        if real_estate.room_count is not None:
            values.append(real_estate.room_count)
            statement += ", `ROOM_COUNT`"

        if real_estate.bathroom_count is not None:
            values.append(real_estate.bathroom_count)
            statement += ", `BATHROOM_COUNT`"

        if real_estate.price is not None:
            values.append(real_estate.price)
            statement += ", `PRICE`"

        if real_estate.description is not None:
            values.append("'" + real_estate.description + "'")
            statement += ", `DESCRIPTION`"

        statement  += ") VALUES ("
        for value in values[:-1]:
            statement += value + ", "

        statement += values[-1] + ")"

        return statement

