-- 코드를 작성해주세요

select item_id, item_name, rarity
from item_info info
where item_id not in (select distinct parent_item_id from item_tree
                      where parent_item_id is not null)
order by item_id desc
# 업그레이드 불가한 아이템 출력
# parent.parent_item_id 가 없어야됨