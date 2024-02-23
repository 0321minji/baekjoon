-- 코드를 작성해주세요
with fr as (select sum(code) as front
            from skillcodes where category like 'Front%' )  
, temp as (
select case when d.skill_code&fr.front>0
                and d.skill_code&(select code from skillcodes where name='Python')>0
               then 'A'
               when d.skill_code&(select code from skillcodes where name='C#')>0
               then 'B'
               when d.skill_code&fr.front>0 then 'C'
               else null end as grade , id , email
from developers d, fr)
select *
from temp
where grade is not null
order by grade, id