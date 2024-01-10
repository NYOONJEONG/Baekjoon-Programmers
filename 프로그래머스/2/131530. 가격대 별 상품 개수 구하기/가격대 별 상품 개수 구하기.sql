-- 코드를 입력하세요
SELECT 
case when price<10000 then '0'
when price<20000 and price>=10000 then '10000'
when price<30000 and price>=20000 then '20000'
when price<40000 and price>=30000 then '30000'
when price<50000 and price>=40000 then '40000'
when price<60000 and price>=50000 then '50000'
when price<70000 and price>=60000 then '60000'
when price<80000 and price>=70000 then '70000'
when price<90000 and price>=80000 then '80000'
else '90000'
end as price_group, count(*) as products
from product
group by price_group 
order by price_group