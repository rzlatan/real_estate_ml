SELECT re.SQUARE_FOOTAGE_RANGE, COUNT(*)
FROM (
        SELECT CASE
                    WHEN SQUARE_FOOTAGE BETWEEN 0 AND 35 THEN 'do 35'
                    WHEN SQUARE_FOOTAGE BETWEEN 36 AND 50 THEN 'od 35 do 50'
                    WHEN SQUARE_FOOTAGE BETWEEN 51 AND 65 THEN 'od 50 do 65'
                    WHEN SQUARE_FOOTAGE BETWEEN 66 AND 80 THEN 'od 65 do 80'
                    WHEN SQUARE_FOOTAGE BETWEEN 81 AND 95 THEN 'od 80 do 95'
                    WHEN SQUARE_FOOTAGE BETWEEN 95 AND 110 THEN 'od 95 do 110'
                    WHEN SQUARE_FOOTAGE BETWEEN 111 AND 140 THEN 'od 110 do 140'
                    ELSE '141 i vise'
        END
        AS SQUARE_FOOTAGE_RANGE
        FROM real_estate_tbl
        WHERE OBJECT_TYPE = 'stan' AND OFFER_TYPE='prodaja'
     ) re
GROUP BY SQUARE_FOOTAGE_RANGE