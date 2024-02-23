-- 코드를 작성해주세요
select distinct id, email, first_name, last_name
from skillcodes sc join developers d on sc.code&d.skill_code>0
where sc.category='Front End'
order by id