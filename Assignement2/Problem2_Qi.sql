.mode csv
.output result.csv


select  sum(prod)
from
(
select f1.docid as doc1,f1.term as term1,f2.docid as doc2,f2.term as term2,f1.count*f2.count as prod
where f1.term=f2.term 
and f1.docid<f2.docid
and f1.docid='10080_txt_crude' and f2.docid='17035_txt_earn'
)q1
;


.output stdou




