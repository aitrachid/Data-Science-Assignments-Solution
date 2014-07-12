.mode csv
.output result.csv
select count(*) from frequency where term ='parliament';
.output stdout
