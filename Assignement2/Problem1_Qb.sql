.mode csv
.output result.csv
select count(term ) from frequency where docid='10398_txt_earn' and count=1;
.output stdout
