SELECT re.CATEGORY, COUNT(1) AS CATEGORY_COUNT, COUNT(1) / sre.TOTAL_COUNT AS PERCENTAGE FROM
(
    SELECT CASE
        WHEN PRICE < 49999 THEN 'manje od 49 999'
        WHEN PRICE BETWEEN 50000 AND 99999 THEN 'izmedju 50 000 i 99 999'
        WHEN PRICE BETWEEN 100000 AND 149999 THEN 'izmedju 100 000 i 149 999'
        WHEN PRICE BETWEEN 150000 AND 199999 THEN 'izmedju 150 000 i 199 999'
        ELSE 'vise od 200 000'
    END AS CATEGORY
    FROM real_estate_tbl
    WHERE PRICE IS NOT NULL AND OFFER_TYPE = 'prodaja'
) re
CROSS JOIN (
    SELECT COUNT(*) AS TOTAL_COUNT FROM real_estate_tbl
    WHERE OFFER_TYPE = 'prodaja' AND PRICE IS NOT NULL
) sre
GROUP BY re.CATEGORY, sre.TOTAL_COUNT