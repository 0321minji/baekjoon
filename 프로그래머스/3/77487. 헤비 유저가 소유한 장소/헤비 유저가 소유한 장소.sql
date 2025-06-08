-- 코드를 입력하세요
# select * from
# places
# where host_id in 
# (
# SELECT host_id, count
# from places
# group by host_id
# )
-- window 함수?
select id, name, host_id
from(
    select * , count(*) over(partition by host_id) as cnt
    from places
) tb
where cnt>=2
order by id