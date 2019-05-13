AS1 = $(addprefix tsv/as1/, $(foreach n, 1 2 3 4 5 6 7 8, xs.as1.$(n).tsv))
AS2 = $(addprefix tsv/as2/, $(foreach n, 1 2 3 4, xs.as2.$(n).tsv))
SS = $(addprefix tsv/ss/, $(foreach n, 1 2 3, xs.ss.$(n).tsv))
JS = $(addprefix tsv/js/, $(foreach n, 1 2, xs.js.$(n).tsv))

.PHONY: clean as1 as2 ss js
default: as1 as2 ss js

as1: tsv/as1 $(AS1)
as2: tsv/as2 $(AS2)
ss: tsv/ss $(SS)
js: tsv/js $(JS)

tsv/as1 tsv/as2 tsv/ss tsv/js:
	mkdir $@

clean:
	$(RM) $(AS1) $(AS2) $(SS) $(JS)

tsv/as1/xs.as1.1.tsv: template/12_1.tsv
tsv/as1/xs.as1.2.tsv: template/11_1.tsv
tsv/as1/xs.as1.3.tsv: template/11_1.tsv
tsv/as1/xs.as1.4.tsv: template/11_1.tsv
tsv/as1/xs.as1.5.tsv: template/11_1.tsv
tsv/as1/xs.as1.6.tsv: template/11_1.tsv
tsv/as1/xs.as1.7.tsv: template/11_1.tsv
tsv/as1/xs.as1.8.tsv: template/11_1.tsv

tsv/%.tsv: rename/%.txt
	pttt -i $(word 2, $^) rename $< verify > $@
