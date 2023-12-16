-- 코드를 입력하세요
SELECT concat("/home/grep/src/", F.board_id , "/" ,F.file_id ,F.file_name , F.file_ext) as file_path
from used_goods_board as B 
inner join used_goods_file as F
on B.board_id = F.board_id
WHERE B.views = (SELECT MAX(views) FROM used_goods_board)
order by F.file_id desc
