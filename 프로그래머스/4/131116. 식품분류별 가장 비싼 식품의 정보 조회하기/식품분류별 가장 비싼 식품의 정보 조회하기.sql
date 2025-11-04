-- 코드를 입력하세요
SELECT category, price as MAX_PRICE, product_name
FROM food_product
where (price,category) in (SELECT MAX(PRICE), CATEGORY
      FROM FOOD_PRODUCT
      WHERE CATEGORY IN ("과자","국","김치","식용유")
      GROUP BY CATEGORY)
order by max_price desc