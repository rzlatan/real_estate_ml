SELECT se.OBJECT_TYPE,
       se.OFFER_TYPE,
       se.CITY,
       se.MUNICIPALITY,
       se.SQUARE_FOOTAGE,
       se.YEAR_BUILT,
       se.CONSTRUCTION_STATE,
       se.LAND_AREA,
       se.FLOOR,
       se.HEATING_SYSTEM,
       se.EQUIPMENT_STATE,
       se.HAS_ELEVATOR,
       se.HAS_GARAGE,
       se.HAS_PARKING,
       se.REGISTRATION_STATE,
       se.ROOM_COUNT,
       se.BATHROOM_COUNT,
       se.PRICE,
       se.PRICE * 1.0 / se.SQUARE_FOOTAGE AS AVG_PRICE_PER_M2,
       re.AVERAGE_PRICE AS AVERAGE_PRICE,
       re.AVERAGE_PRICE * 90.0 / 100.0 AS LOWER_LIMIT,
       re.AVERAGE_PRICE * 110.0 / 100.0 AS UPPER_LIMIT,
       se.PRICE * 1.0 / se.SQUARE_FOOTAGE BETWEEN re.AVERAGE_PRICE * 0.90 AND re.AVERAGE_PRICE * 1.10 AS IS_SATISFIED
FROM (
    SELECT AVG(PRICE * 1.0 / SQUARE_FOOTAGE) AS AVERAGE_PRICE, MUNICIPALITY FROM real_estate_tbl
    WHERE CITY = 'Beograd' AND OFFER_TYPE = 'prodaja' AND OBJECT_TYPE = 'stan'
    GROUP BY MUNICIPALITY
) re
, (
    SELECT * FROM real_estate_tbl
    WHERE CITY = 'Beograd' AND OFFER_TYPE = 'prodaja' AND OBJECT_TYPE = 'stan'
) se
WHERE re.MUNICIPALITY = se.MUNICIPALITY