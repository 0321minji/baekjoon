-- 코드를 작성해주세요
# 리프 찾는 거
select parent.item_id, parent.item_name, rarity
from item_info parent
left join item_tree child
on parent.item_id=child.parent_item_id
where ISNULL(child.item_id)
order by parent.item_id desc