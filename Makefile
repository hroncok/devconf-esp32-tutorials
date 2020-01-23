all: $(addsuffix .pdf,$(basename $(wildcard */handout.tex)))

%/handout.pdf: %/handout.tex tutorial.cls
	cd $* && lualatex handout.tex
