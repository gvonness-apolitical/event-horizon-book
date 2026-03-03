.PHONY: all clean watch

all:
	latexmk -cd src/book.tex

clean:
	latexmk -cd -C src/book.tex
	rm -rf build/

watch:
	latexmk -cd -pvc src/book.tex
