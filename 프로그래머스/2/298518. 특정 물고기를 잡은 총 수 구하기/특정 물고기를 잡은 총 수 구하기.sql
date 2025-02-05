-- 코드를 작성해주세요
# fish type으로 join
select count(*) as FISH_COUNT
from fish_info f join fish_name_info n
on f.fish_type=n.fish_type
where n.fish_name='BASS' or n.fish_name='SNAPPER'