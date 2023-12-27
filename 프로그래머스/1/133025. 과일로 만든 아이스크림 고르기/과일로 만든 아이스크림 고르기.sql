-- 코드를 입력하세요
SELECT F.flavor 
from first_half as F
inner join ICECREAM_INFO as I
on F.flavor = I.flavor
where F.total_order > 3000 and I.INGREDIENT_TYPE = 'fruit_based'
order by F.total_order desc