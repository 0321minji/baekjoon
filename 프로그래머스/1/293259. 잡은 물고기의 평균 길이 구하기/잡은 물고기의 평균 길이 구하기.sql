-- 코드를 작성해주세요
# null -> 10

# select round(avg(length),2) average_length
# from (select ifnull(length,10) length
#       from fish_info) info
      
select round(avg(ifnull(length,10)),2) average_length
from fish_info