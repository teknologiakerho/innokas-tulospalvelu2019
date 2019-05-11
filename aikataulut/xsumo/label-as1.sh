#!/bin/sh
awk -v FS='\t' -v OFS='\t' '{print $1, "A"$3, "T"$4, "T"$5, "J0"}' $@
