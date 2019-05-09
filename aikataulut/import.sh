#!/bin/bash

for fname in rescue/tsv/*.tsv tanssi/tsv/*.tsv
do
	block=$(basename $fname .tsv)
	echo ">>> Import $block from $fname"
	rsx import -y $block $fname
done
