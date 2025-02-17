-- 코드를 작성해주세요
select child.id as ID
from ecoli_data child join 
(select child.id as gen2 , parent.id as gen1 
from ecoli_data child join (select * from ecoli_data) parent
on child.parent_id = parent.id
where parent.parent_id is NULL) past
on child.parent_id = past.gen2
order by child.id

# 자기참조를.. 3번을 해서 null 이 아닌걸 찾아야하묘....?