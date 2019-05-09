TSV_RESCUE = rescue1.1.tsv rescue1.2.tsv rescue1.haast.tsv\
			 rescue2.1.tsv rescue2.2.tsv rescue2.haast.tsv\
			 rescue3.1.tsv rescue3.2.tsv rescue3.haast.tsv

TSV_TANSSI = tanssi.alkeis.esitys.tsv tanssi.alkeis.haast.tsv tanssi.alkeis.harj.tsv\
			 tanssi.jatko.esitys.tsv tanssi.jatko.haast.tsv tanssi.jatko.harj.tsv

TSV = $(addprefix rescue/tsv/, $(TSV_RESCUE)) $(addprefix tanssi/tsv/, $(TSV_TANSSI))

default: $(TSV)

clean:
	$(RM) $(TSV)

rescue/tsv/rescue1.1.tsv: rescue/csv/Pelastus1-2019-suoritus1.csv
rescue/tsv/rescue1.2.tsv: rescue/csv/Pelastus1-2019-suoritus2.csv
rescue/tsv/rescue1.haast.tsv: rescue/csv/Pelastus1-2019-haastattelu.csv
rescue/tsv/rescue2.1.tsv: rescue/csv/Pelastus2-2019-suoritus1.csv
rescue/tsv/rescue2.2.tsv: rescue/csv/Pelastus2-2019-suoritus2.csv
rescue/tsv/rescue2.haast.tsv: rescue/csv/Pelastus2-2019-haastattelu.csv
rescue/tsv/rescue3.1.tsv: rescue/csv/Pelastus3-2019-suoritus1.csv
rescue/tsv/rescue3.2.tsv: rescue/csv/Pelastus3-2019-suoritus2.csv
rescue/tsv/rescue3.haast.tsv: rescue/csv/Pelastus3-2019-haastattelu.csv

tanssi/tsv/tanssi.alkeis.esitys.tsv: tanssi/csv/TanssiAlkeissarja-2019-esitys.csv
tanssi/tsv/tanssi.alkeis.haast.tsv: tanssi/csv/TanssiAlkeissarja-2019-esittely.csv
tanssi/tsv/tanssi.alkeis.harj.tsv: tanssi/csv/TanssiAlkeissarja-2019-lavaharjoittelu.csv
tanssi/tsv/tanssi.jatko.esitys.tsv: tanssi/csv/TanssiJatkosarja-2019-esitys.csv
tanssi/tsv/tanssi.jatko.haast.tsv: tanssi/csv/TanssiJatkosarja-2019-esittely.csv
tanssi/tsv/tanssi.jatko.harj.tsv: tanssi/csv/TanssiJatkosarja-2019-lavaharjoittelu.csv

$(TSV):
	cat $< | dos2unix | awk -v FS=';' -v OFS='\t' '{print $$1,$$4,$$2,$$3}' > $@
