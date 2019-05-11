#!/bin/bash
for f in csv/*.csv
do
	dos2unix $f
done

awk -v FS=';' -v OFS='\t' '{print NR,$1,0,$2,""}' csv/*.csv\
	| sort -u -t$'\t' -k2,2\
	> teams.tsv
