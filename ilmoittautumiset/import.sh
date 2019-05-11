#!/bin/sh
sqlite3 $1 <<EOF
.mode tabs
.import teams.tsv teams
EOF
