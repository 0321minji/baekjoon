-- 코드를 작성해주세요
select distinct id, email, first_name, last_name
from skillcodes sc , developers d
where sc.code&d.skill_code>0 and sc.name in ('Python','C#')
order by id