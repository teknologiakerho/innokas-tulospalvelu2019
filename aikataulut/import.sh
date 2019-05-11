#!/bin/bash

for dname in "$@"
do
	for fname in $dname/*.tsv
	do
		block=$(basename $fname .tsv)
		echo ">>> Import $block from $fname"
		rsx import -y $block $fname
	done
done
