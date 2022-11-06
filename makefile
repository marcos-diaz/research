default:
	find . -name '*.tex' -exec pdflatex {} \;
	make clean

clean:
	rm -f *.aux
	rm -f *.fdb_latexmk
	rm -f *.fls
	rm -f *.log
	rm -f *.synctex.gz
	rm -f *.dvi

cleanall: clean
	rm -f *.pdf
