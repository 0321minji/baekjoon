-- 코드를 입력하세요
with user as (
SELECT user_id
from user_info
where joined>='2021-01-01' and joined<='2021-12-31')

select YEAR(sales_date) as 'YEAR', MONTH(sales_date) as MONTH, count(distinct user_id) as purchased_users,
round((count(distinct user_id) / (select count(*) from user)),1) as puchased_ratio
from online_sale
where user_id in (select user_id from user)
group by YEAR(sales_date), month(sales_date)
order by YEAR(sales_date), month(sales_date)