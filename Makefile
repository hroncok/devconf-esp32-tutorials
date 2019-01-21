all: $(addsuffix /handout.pdf,$(wildcard */))

%/handout.pdf: %/handout.tex
	cd $* && lualatex handout.tex
