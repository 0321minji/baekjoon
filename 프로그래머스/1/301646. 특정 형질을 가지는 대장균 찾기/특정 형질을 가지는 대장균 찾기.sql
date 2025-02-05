-- 코드를 작성해주세요

select count(*) as 'COUNT'
from ecoli_data
where genotype&2=0 and (genotype&4!=0 or genotype&1 !=0)
# 비트연산자
# 100 4 or 101 5 or 001 1
# 10 안가지고 (1 또는 100) 가지고