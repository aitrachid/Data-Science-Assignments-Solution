.mode csv
.output result.csv


create view if  not exists dataset as
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
;

select max(score)
from
(
select doc1, sum(prod) as score
from
(
select f1.docid as doc1,f1.term as term1,f2.docid as doc2,f2.term as term2,f1.count*f2.count as prod

from
dataset f1
cross join
dataset f2

where f1.term=f2.term 
-- and f1.docid<f2.docid
and f2.docid='q'
)q1
group by doc1
order by score desc
)q2 
;
.output stdou





