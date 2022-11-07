default:
	pdflatex -output-directory multiple_ars/ multiple_ars/multiple_ars.tex
	make clean

clean:
	rm -f **/*.aux
	rm -f **/*.fdb_latexmk
	rm -f **/*.fls
	rm -f **/*.log
	rm -f **/*.synctex.gz
	rm -f **/*.dvi
	rm -f **/*.out

cleanall: clean
	rm -f *.pdf
