-- 코드를 작성해주세요
select year(DIFFERENTIATION_DATE) as year, max(size_of_colony) over (partition by year(DIFFERENTIATION_DATE)) - size_of_colony as YEAR_DEV, id
from ecoli_data
order by year,year_dev