SELECT re.DECADE, COUNT(*) FROM
(
    SELECT CASE
        WHEN YEAR_BUILT BETWEEN 0 AND 1949 THEN 'Pre 1950'
        WHEN YEAR_BUILT BETWEEN 1950 AND 1959 THEN 'Od 1950 do 1960'
        WHEN YEAR_BUILT BETWEEN 1960 AND 1969 THEN 'Od 1960 do 1969'
        WHEN YEAR_BUILT BETWEEN 1970 AND 1979 THEN 'Od 1970 do 1979'
        WHEN YEAR_BUILT BETWEEN 1980 AND 1989 THEN 'Od 1980 do 1989'
        WHEN YEAR_BUILT BETWEEN 1990 AND 1999 THEN 'Od 1990 do 1999'
        WHEN YEAR_BUILT BETWEEN 2000 AND 2009 THEN 'Od 2000 do 2009'
        WHEN YEAR_BUILT BETWEEN 2010 AND 2019 THEN 'Od 2010 do 2019'
        ELSE 'Posle 2020'
    END AS DECADE
    FROM real_estate_tbl
    WHERE YEAR_BUILT IS NOT NULL
) re
GROUP BY re.DECADE