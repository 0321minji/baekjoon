-- 코드를 작성해주세요
select group_concat(distinct quarter(differentiation_date),'Q') quarter, count(*) as ecoli_count
from ecoli_data
group by quarter(differentiation_date)