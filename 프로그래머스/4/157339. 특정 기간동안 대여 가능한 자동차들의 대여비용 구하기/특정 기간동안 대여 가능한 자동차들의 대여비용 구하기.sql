SELECT C.CAR_ID AS CAR_ID
     , C.CAR_TYPE AS CAR_TYPE
     , FLOOR(C.DAILY_FEE * 30 * (1 - P.DISCOUNT_RATE/100)) AS FEE
FROM CAR_RENTAL_COMPANY_CAR AS C
    INNER JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN AS P ON C.CAR_TYPE = P.CAR_TYPE
                                                    AND P.DURATION_TYPE = '30일 이상'
                                                    AND C.CAR_TYPE IN ('세단', 'SUV')
    LEFT JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY AS H ON C.CAR_ID = H.CAR_ID
                                                    AND H.END_DATE >= '2022-11-01'
                                                    AND H.START_DATE <= '2022-11-30'
WHERE ROUND(C.DAILY_FEE * 30 * (1 - P.DISCOUNT_RATE/100)) BETWEEN 500000 AND 1999999
  AND H.CAR_ID IS NULL
ORDER BY FEE DESC
       , CAR_TYPE
       , CAR_ID DESC