select b.title, b.board_id, r.reply_id, r.writer_id, r.contents, date_format(r.CREATED_DATE, '%Y-%m-%d') from used_goods_board b
join used_goods_reply r
on b.board_id = r.board_id
where b.CREATED_DATE between '2022-10-01' and '2022-10-31'
#where r.CREATED_DATE between '2022-10-01' and '2022-10-31'
order by r.CREATED_DATE, b.title