.mode csv
.output result.csv

select count(*)
from
(
select docid ,count (distinct term)from
(
select docid,term
from frequency 
where term='transactions' or term='world'
)
group by docid
having count(distinct term)>1
)
;
.output stdou