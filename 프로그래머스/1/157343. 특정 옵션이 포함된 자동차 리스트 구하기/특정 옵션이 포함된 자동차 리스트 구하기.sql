-- 코드를 입력하세요
SELECT CAR_ID, CAR_TYPE, DAILY_FEE, OPTIONS 
from CAR_RENTAL_COMPANY_CAR
where find_in_set('네비게이션', options) != 0
order by car_id desc