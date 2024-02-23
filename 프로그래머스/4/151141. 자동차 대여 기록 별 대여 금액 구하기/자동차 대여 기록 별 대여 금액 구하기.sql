-- 코드를 입력하세요
with truck as (select daily_fee, history_id,datediff(end_date,start_date)+1 as d
                from car_rental_company_car c 
                join car_rental_company_rental_history h on c.car_id=h.car_id
            where car_type='트럭')
, dr as (            
select duration_type, discount_rate 
from car_rental_company_discount_plan p
where car_type='트럭'
order by duration_type)

select history_id,round(daily_fee*(d)*(100-ifnull(discount_rate,0))/100) as fee
from (select *,case when d>=90 then '90일 이상'
               when d>=30 then '30일 이상'
               when d>=7 then '7일 이상'
               else null end as dt from truck t) as tt
left outer join dr on tt.dt=dr.duration_type
order by fee desc, history_id desc
