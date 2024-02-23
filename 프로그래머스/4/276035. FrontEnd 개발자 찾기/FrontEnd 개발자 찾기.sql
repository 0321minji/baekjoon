-- 코드를 작성해주세요
# select distinct id, email, first_name, last_name
# from skillcodes sc join developers d on sc.code&d.skill_code>0
# where sc.category='Front End'
# order by id
with front as (select sum(code) as fr from skillcodes where category like 'Front%')

select id, email, first_name, last_name
from developers join front on developers.skill_code&front.fr>0
order by id