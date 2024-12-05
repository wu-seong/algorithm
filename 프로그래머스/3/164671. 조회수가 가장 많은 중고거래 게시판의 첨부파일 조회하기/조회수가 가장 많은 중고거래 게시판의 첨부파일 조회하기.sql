# 게시물 중 조횟수가 가장 높은 것을 식별
# 해당 게시물에 대한
with most_view as(
select board_id
from USED_GOODS_BOARD
order by views desc
limit 1)

select concat('/home/grep/src/', file.board_id, '/', file.file_id, file.file_name, file.file_ext) FILE_PATH
from USED_GOODS_FILE file
join most_view
on most_view.board_id = file.board_id
order by file.file_id desc