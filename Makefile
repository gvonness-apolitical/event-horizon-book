.PHONY: all clean watch

all:
	latexmk -cd src/book.tex
	@xattr -d com.apple.quarantine build/book.pdf 2>/dev/null || true

clean:
	latexmk -cd -C src/book.tex
	rm -rf build/

watch:
	latexmk -cd -pvc src/book.tex
