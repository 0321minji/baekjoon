-- 코드를 INT작성해주세요
select count(*) FISH_COUNT,  month(time) as MONTH
from fish_info
group by month
order by month