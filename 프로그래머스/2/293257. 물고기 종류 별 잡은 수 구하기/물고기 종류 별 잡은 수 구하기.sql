-- 코드를 작성해주세요
select count(*) as FISH_COUNT, fish_name
from fish_name_info name join fish_info fish
on name.fish_type= fish.fish_type
group by fish_name
order by FISH_COUNT desc
