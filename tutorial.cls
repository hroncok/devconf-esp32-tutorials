\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{tutorial}[2018/01/21 HW tutorial]

\LoadClass[a4paper,8pt]{article}

% Language
\usepackage[utf8]{luainputenc}
\usepackage[pdfborder={0 0 0}]{hyperref}  % needs to be early-ish
\usepackage[english]{babel}

% Fonts
\usepackage{fouriernc}
\usepackage{tgpagella}
\usepackage{xcolor}
\usepackage{amssymb}
\usepackage{fontspec}
\setmainfont[Numbers=OldStyle]{TeX Gyre Pagella}

% Page layout
\usepackage[activate=true]{microtype}
\usepackage[a4paper,margin=2cm,top=1cm]{geometry}
\pagestyle{empty}
\parskip=1ex
\parindent=0pt

% Charts & Math
\usepackage{calc}
\usepackage{tikz}
\usepackage{pgfplots}
\usepackage{siunitx}
\usepackage{colortbl}

% Lists (tasks)
\usepackage{enumitem}
\setlist[enumerate,1]{start=0,leftmargin=0pt,labelindent=0pt,itemindent=0pt,resume}

% Headings
\usepackage{titling}
\usepackage{titlesec}
\newfontfamily\headingfont[]{Bree Serif}
\titleformat*{\section}{\large\headingfont}
\titlespacing*{\section}{0pt}{5pt plus 5pt}{0pt}
% Remove section numbers
\let\oldsection\section
\renewcommand\section{\oldsection*} 

% Code listings
\usepackage{listings}
\lstset{
    language=Python,
    basicstyle=\small\ttfamily,
    tabsize=4,
    columns=fixed,
    showstringspaces=false,
    showtabs=false,
    keepspaces,
    keywordstyle=\bfseries,
    firstnumber=last,
    emphstyle=\bfseries,
    showlines=false,
    texcl=true,
    escapebegin=\rmfamily,
    gobble=4,  % All code listings must be indented 4 spaces!
    backgroundcolor=\color{black!10!white},
    frame=single,
    framerule=0pt,
}

% Additional commands
\newenvironment{comment}{\itshape}{}
\newcommand\kbd[1]{\texttt{#1}}
\newcommand\abbr[1]{{\addfontfeature{Numbers=Lining}#1}}

% Title, ` character for inline code
\AtBeginDocument{
    {\headingfont\Large\thetitle}
    \lstMakeShortInline[framerule=1pt]`
}
