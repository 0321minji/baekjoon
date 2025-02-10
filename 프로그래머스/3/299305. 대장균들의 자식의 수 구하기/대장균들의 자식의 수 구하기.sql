-- 코드를 작성해주세요
# select *
# from ecoli_data
# where (select parent_id, count(*)from ecoli_data group by parent_id)
select ecoli.id, ifnull(child,0) child_count
from ecoli_data ecoli left outer join (
    select parent_id, count(*) child
    from ecoli_data 
    group by parent_id
    having parent_id is not null) data
on ecoli.id = data.parent_id