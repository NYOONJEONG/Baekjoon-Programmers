-- 코드를 입력하세요
SELECT book_id, DATE_FORMAT(published_date, '%Y-%m-%d') AS published_date
from book
where category like '인문' and substring(published_date,1,4)=2021
order by published_date asc