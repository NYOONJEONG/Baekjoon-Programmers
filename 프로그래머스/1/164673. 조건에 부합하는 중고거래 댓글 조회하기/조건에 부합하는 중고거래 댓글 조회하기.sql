-- 코드를 입력하세요
SELECT B.TITLE, R.BOARD_ID,R.REPLY_ID,R.WRITER_ID, 
R.CONTENTS, DATE_FORMAT(R.CREATED_DATE , '20%y-%m-%d') as CREATED_DATE
from used_goods_board B 
    inner join used_goods_reply R
    on B.board_id = R.board_id
    where B.created_date like '_____10___'
order by R.created_date, B.title;