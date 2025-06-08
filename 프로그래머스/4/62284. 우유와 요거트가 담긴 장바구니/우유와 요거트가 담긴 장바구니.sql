-- 코드를 입력하세요

# with y as (
# select cart_id
# from cart_products
# where name='Yogurt'
# group by cart_id
# )

# with m as (
# select cart_id
# from cart_products
# where name='Milk'
# group by cart_id
# )

select y.cart_id
from (select cart_id
from cart_products
where name='Yogurt'
group by cart_id) as y
join 
(select cart_id
from cart_products
where name='Milk'
group by cart_id) as m
on
y.cart_id = m.cart_id

order by y.cart_id    

