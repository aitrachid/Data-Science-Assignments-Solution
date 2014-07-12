.mode csv
.output result.csv
select cell
from
(
select row1 as row,col2 as col,sum(prod) as cell from
(
select A.row_num as row1,A.col_num as col1,B.row_num as row2,B.col_num as col2 ,A.value*B.value as prod
from
A
cross join
B
where A.col_num=B.row_num
order by A.row_num,B.col_num
)q1
group by row1,col2
)q2
where row=2 and col=3
;
.output stdou