-- 코드를 INT작성해주세요
select count(*) FISH_COUNT,  convert(date_format(time,"%c"),UNSIGNED) as month
from fish_info
group by convert(date_format(time,"%c"),UNSIGNED)
order by month 