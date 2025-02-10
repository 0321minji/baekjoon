-- 코드를 작성해주세요

# 내림차순으로 정렬했을 때 0~25% 등수/ 26~50% / 51~75% / 76 ~ 100%
# 데이터의 수는 4의 배수 -> count(*)를 한 뒤에 1/4 씩 기준으로

# select  case when r <=count(*)*1/4 then "low"
#     else "critical"
#     end as colony_name
# select id, 
#     # case when r <= count(*)*1/4 then "low"
#     # when r<=count(*)*2/4 then "medium"
#     # else "critical"
#     # end as colony_name
# from (select id, rank() over (order by size_of_colony) r from ecoli_data) ecoli
# order by id

select id, 
    case when r <=0.25 then "LOW"
    when r<=0.5 then "MEDIUM"
    when r<=0.75 then "HIGH"
    else "CRITICAL"
    end as colony_name
from (select id, percent_rank() over (order by size_of_colony) r from ecoli_data) ranking
order by id