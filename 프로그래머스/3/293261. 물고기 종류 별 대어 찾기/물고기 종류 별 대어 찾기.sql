-- 코드를 작성해주세요

select id, fish_name,length
from (
    select id,fish_type,length, row_number() over (partition by fish_type order by length desc) as rn
    from fish_info
) as t
join fish_name_info as name
on t.fish_type=name.fish_type
where t.rn=1
order by id;