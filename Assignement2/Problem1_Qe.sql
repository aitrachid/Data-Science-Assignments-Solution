.mode csv
.output result.csv
select count(*)
from
(
select docid,sum(frequency.count) 
from frequency 
group by docid 
having sum(frequency.count)>300
)
;
.output stdout
