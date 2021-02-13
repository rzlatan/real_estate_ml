#----------------------------------------------------------------
# Number of real estates by offer type (rent / sell)
# Results:
#   RealEstateByOfferTypeQueryResult.csv
#
SELECT COUNT(*), OFFER_TYPE FROM real_estate_tbl
GROUP BY OFFER_TYPE

#----------------------------------------------------------------
# Number of real estates per city
# Results:
#   RealEstateCountPerCityQueryResult.csv
#   RealEstateCountPerCityAndObjectTypeQueryResult.csv
#
SELECT COUNT(*) AS REAL_ESTATE_COUNT, CITY  FROM real_estate_tbl
GROUP BY CITY
ORDER BY REAL_ESTATE_COUNT DESC

# Modification:
# Number of real estates per city and object type
#
SELECT COUNT(*) AS REAL_ESTATE_COUNT, OFFER_TYPE, CITY  FROM real_estate_tbl
GROUP BY CITY, OFFER_TYPE
ORDER BY CITY

#----------------------------------------------------------------
# Number of flats and houses which are new constructions
#   Results:
#       NewConstructionsPerObjectType.csv
#
SELECT COUNT(*), OBJECT_TYPE FROM real_estate_tbl
WHERE CONSTRUCTION_STATE LIKE '%novo%'
group by  OBJECT_TYPE

#----------------------------------------------------------------
# Most expensive houses and flats for selling
# Results:
#   MostExpensiveHousesQueryResult.csv
#   MostExpensiveFlatsQueryResult.csv
#
SELECT * FROM real_estate_tbl
WHERE OBJECT_TYPE = 'kuca' AND OFFER_TYPE = 'prodaja'
# WHERE STATE = 'Srbija'
ORDER BY  PRICE DESC
LIMIT 25

# UNION if we want only one query for both query result

SELECT * FROM real_estate_tbl
WHERE OBJECT_TYPE = 'stan' AND  OFFER_TYPE = 'prodaja'
# WHERE STATE = 'Srbija'
ORDER BY  PRICE DESC
LIMIT 25

SELECT * FROM real_estate_tbl
WHERE OBJECT_TYPE = 'vikendica' AND (STATE = 'Srbija' OR STATE = 'Crna Gora')
ORDER BY PRICE DESC
LIMIT 20

#------------------------------------------------------------------
# Most expensive houses and flats in Belgrade for renting
# Results:
#   MostExpensiveHousesForRentingInBelgrade.csv,
#   MostExpensiveFlatsForRentingInBelgrade.csv
#
SELECT * FROM real_estate_tbl
WHERE OBJECT_TYPE = 'kuca' AND OFFER_TYPE = 'izdavanje' AND CITY = 'Beograd'
ORDER BY PRICE DESC
LIMIT 50

# UNION if we want only one query for both results

SELECT * FROM real_estate_tbl
WHERE OBJECT_TYPE = 'stan' AND OFFER_TYPE = 'izdavanje' AND CITY = 'Beograd'
ORDER BY PRICE DESC
LIMIT 50

#--------------------------------------------------------------------
# Real Estates built in 2019. and 2020., ordered by price
# Results:
#   RealEstatesInLastTwoYearsByPriceQueryResult.csv
#
SELECT * FROM real_estate_tbl
WHERE YEAR_BUILT = 2020 OR YEAR_BUILT = 2019
ORDER BY PRICE DESC

#--------------------------------------------------------------------
# Top 10 real estates by room count
# Results:
#   RealEstatesWithMostRooms.csv
#
SELECT * FROM real_estate_tbl
ORDER BY ROOM_COUNT DESC
LIMIT 10

#--------------------------------------------------------------------
# Real estates with more than 3 bathrooms
# Results:
#   RealEstatesWithMostBathrooms.csv
# Fun fact:
#   First one has really 22 bathrooms https://www.4zida.rs/prodaja/kuce/pecinci/oglas/negovana-ljubinkovica/5ec171919a309101d6264749
#
SELECT * FROM real_estate_tbl
WHERE BATHROOM_COUNT > 3
ORDER BY BATHROOM_COUNT DESC

#-------------------------------------------------------------------
# Real estats with specific heating system
# Results:
#   RealEstatsHeatingSystem.csv
#
SELECT * FROM real_estate_tbl
WHERE HEATING_SYSTEM = 'kaljeva peć' # OR HEATING_SYSTEM = 'whatever_else since there are no results for pump and calorimeter'

#-------------------------------------------------------------------
# Houses with pools
# Results:
#   HousesWithPools.csv
#
SELECT * FROM real_estate_tbl
WHERE OBJECT_TYPE = 'kuca' AND LOWER(DESCRIPTION) LIKE '%bazen%'