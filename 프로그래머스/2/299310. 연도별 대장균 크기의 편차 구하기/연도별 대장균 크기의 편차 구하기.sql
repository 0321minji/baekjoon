-- 코드를 작성해주세요
# 연도별 가장 큰 대장균
# select YEAR(differentiation_date) as year, max(size_of_colony) as size
# from ecoli_data
# group by YEAR(differentiation_date)

# 편차 구하기
select YEAR(differentiation_date) as year, abs(size_of_colony - size) as year_dev, id 
from ecoli_data ecoli join 
(select YEAR(differentiation_date) as year, max(size_of_colony) as size
from ecoli_data
group by YEAR(differentiation_date)
) dev
on YEAR(ecoli.differentiation_date) = dev.year
order by year, year_dev 