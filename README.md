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
  (And improve these instructions with the packages you needed!)
