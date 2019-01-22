all: $(addsuffix /handout.pdf,$(wildcard */))

%/handout.pdf: %/handout.tex tutorial.cls
	cd $* && lualatex handout.tex
