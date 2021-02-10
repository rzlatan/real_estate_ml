from query_generator import QueryGenerator
from real_estate_model import RealEstate

real_estate = RealEstate()

real_estate.set_city("Belgrade")
real_estate.set_offer_type("Prodaja")
real_estate.set_is_registered(True)
real_estate.set_price(100.10)

query = QueryGenerator.insert_real_estate_query(real_estate)

print(query)