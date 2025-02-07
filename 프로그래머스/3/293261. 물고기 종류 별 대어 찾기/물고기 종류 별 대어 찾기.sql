# select *
# from fish_info info join fish_name_info name
# on info.fish_type = name.fish_type
# group by fish_name
# having max(length)
## window 함수..?

## 종류별 대어
select id, fish_name, length 
from fish_info info join fish_name_info name on info.fish_type = name.fish_type
where (info.fish_type, length)
in (select fish_type, max(length) as length
    from fish_info 
    group by fish_type)
order by id