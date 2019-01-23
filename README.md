Handouts for ESP32 hacking tasks.

Beware that this is not very well documented.
To make PDFs:

* `dnf install lualatex`
* `cd` to the cloned repo
* `make` to generate PDFs
  (or `cd basic; lualatex handout.tex` to generate just one)
* If LaTeX complains about not having `somepackage`,
  do `dnf install 'tex(somepackage.sty)'`.
  Repeat until successful.
  
  Packages needed at some point:
  
      dnf install lualatex 'tex(luainputenc.sty)' 'tex(ctablestack.sty)' 'tex(english.ldf)' 'tex(fouriernc.sty)' \
                  'tex(tgpagella.sty)' 'tex(microtype.sty)' 'tex(pgfplots.sty)' 'tex(siunitx.sty)' \
                  'tex(titling.sty)' 'tex(titlesec.sty)' 'tex(wrapfig.sty)' texlive-collection-fontsrecommended
