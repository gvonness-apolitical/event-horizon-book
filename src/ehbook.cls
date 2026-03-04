%% ehbook.cls — Document class for Event Horizon: A Computational Journey
%% into Black Hole Physics
%%
%% Requires LuaLaTeX for fontspec/unicode-math support.
%%
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ehbook}[2025/01/01 Event Horizon book class]

% ---------- Base class ----------
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{memoir}}
\ProcessOptions\relax
\LoadClass[11pt,twoside,openright]{memoir}

% ---------- Essential packages ----------
\RequirePackage{etoolbox}
\RequirePackage{xcolor}
\RequirePackage{graphicx}
\RequirePackage{tikz}

% ---------- Page geometry ----------
% 7" x 10" stock, generous outer margin for margin notes
\setstocksize{10in}{7in}
\settrimmedsize{\stockheight}{\stockwidth}{*}
\setlrmarginsandblock{22mm}{52mm}{*}
\setulmarginsandblock{24mm}{28mm}{*}
\setmarginnotes{3mm}{42mm}{4mm}
\checkandfixthelayout

% ---------- Fonts (LuaLaTeX) ----------
\RequirePackage{fontspec}
\RequirePackage{unicode-math}

\setmainfont{STIX Two Text}[
  Numbers     = OldStyle,
  Ligatures   = TeX,
]
\setmathfont{STIX Two Math}
\setsansfont{Source Sans Pro}[
  Ligatures   = TeX,
  Scale       = MatchLowercase,
]
\setmonofont{Source Code Pro}[
  Scale       = MatchLowercase,
]

% ---------- Microtype ----------
\RequirePackage{microtype}

% ---------- Color palette — "Accretion Disk" ----------
\definecolor{EHAccretionGold}{RGB}{196,142,54}
\definecolor{EHJetBlue}{RGB}{64,102,153}
\definecolor{EHHorizonCrimson}{RGB}{158,48,44}
\definecolor{EHMarginGray}{RGB}{110,108,118}

% ---------- Hyperlinks ----------
\RequirePackage[
  colorlinks  = true,
  linkcolor   = EHJetBlue,
  citecolor   = EHJetBlue,
  urlcolor    = EHJetBlue,
  bookmarksnumbered = true,
]{hyperref}

% ---------- Cross-referencing ----------
\RequirePackage[nameinlink,noabbrev,capitalise]{cleveref}

% ---------- Bibliography ----------
\RequirePackage[
  backend     = biber,
  style       = numeric-comp,
  sorting     = nyt,
  maxbibnames = 6,
  giveninits  = true,
  doi         = true,
  isbn        = false,
  url         = false,
]{biblatex}

% ---------- Tables and figures ----------
\RequirePackage{booktabs}
\RequirePackage{caption}
\captionsetup{font=small, labelfont=bf, labelsep=period}

% ---------- Units ----------
\RequirePackage{siunitx}

% ---------- Code listings ----------
\RequirePackage{listings}
\lstset{
  basicstyle   = \small\ttfamily,
  keywordstyle = \color{EHJetBlue}\bfseries,
  commentstyle = \color{EHMarginGray}\itshape,
  stringstyle  = \color{EHHorizonCrimson},
  numbers      = left,
  numberstyle  = \tiny\color{EHMarginGray},
  numbersep    = 6pt,
  frame        = leftline,
  framerule    = 1pt,
  rulecolor    = \color{EHAccretionGold},
  breaklines   = true,
  tabsize      = 4,
  showstringspaces = false,
}
\lstdefinelanguage{Rust}{
  morekeywords = {fn,let,mut,pub,struct,enum,impl,trait,use,mod,crate,self,
                  Self,super,const,static,type,where,as,ref,return,if,else,
                  match,for,while,loop,break,continue,move,async,await,
                  unsafe,extern,true,false,in},
  morecomment  = [l]{//},
  morecomment  = [s]{/*}{*/},
  morestring   = [b]",
  sensitive    = true,
}
\lstdefinelanguage{Haskell}{
  morekeywords = {module,where,import,data,type,newtype,class,instance,
                  deriving,let,in,case,of,if,then,else,do,return},
  morecomment  = [l]{--},
  morecomment  = [s]{\{-}{-\}},
  morestring   = [b]",
  sensitive    = true,
}

% ---------- Margin notes ----------
\RequirePackage{marginnote}
\RequirePackage{marginfix}          % prevent \marginpar overflow at page bottom
\renewcommand*{\marginfont}{\footnotesize\color{EHMarginGray}}

% Margin note types — use \marginpar (handled by marginfix) for page-aware
% placement; fall back to \marginnote only where \marginpar is unavailable.
% Physics insight (jet blue accent)
\newcommand{\physnote}[1]{%
  \marginpar{\textcolor{EHJetBlue}{\rule{12pt}{1pt}}\\[2pt]%
  {\footnotesize\color{EHMarginGray}#1}}%
}

% Implementation detail (gold accent)
\newcommand{\implnote}[1]{%
  \marginpar{\textcolor{EHAccretionGold}{\rule{12pt}{1pt}}\\[2pt]%
  {\footnotesize\color{EHMarginGray}#1}}%
}

% Historical context (crimson accent)
\newcommand{\histnote}[1]{%
  \marginpar{\textcolor{EHHorizonCrimson}{\rule{12pt}{1pt}}\\[2pt]%
  {\footnotesize\color{EHMarginGray}#1}}%
}

% Cross-reference note (gray accent)
\newcommand{\xrefnote}[1]{%
  \marginpar{\textcolor{EHMarginGray}{\rule{12pt}{1pt}}\\[2pt]%
  {\footnotesize\color{EHMarginGray}#1}}%
}

% Warning/pitfall note (crimson, bold rule)
\newcommand{\warnnote}[1]{%
  \marginpar{\textcolor{EHHorizonCrimson}{\rule{12pt}{2pt}}\\[2pt]%
  {\footnotesize\bfseries\color{EHHorizonCrimson}#1}}%
}

% ---------- Theorem environments ----------
% memoir provides amsthm-like functionality; undefine \proof to avoid clash
\let\proof\relax
\let\endproof\relax
\RequirePackage{amsthm}
\RequirePackage{mdframed}
\RequirePackage{thmtools}

\declaretheoremstyle[
  headfont     = \bfseries\sffamily\color{EHJetBlue},
  bodyfont     = \normalfont,
  spaceabove   = 8pt,
  spacebelow   = 8pt,
  mdframed     = {
    linewidth   = 2pt,
    rightline   = false,
    topline     = false,
    bottomline  = false,
    linecolor   = EHJetBlue,
    innerleftmargin  = 8pt,
    innerrightmargin = 8pt,
    innertopmargin   = 6pt,
    innerbottommargin = 6pt,
  },
]{ehtheorem}

\declaretheoremstyle[
  headfont     = \bfseries\sffamily\color{EHAccretionGold},
  bodyfont     = \normalfont,
  spaceabove   = 8pt,
  spacebelow   = 8pt,
  mdframed     = {
    linewidth   = 2pt,
    rightline   = false,
    topline     = false,
    bottomline  = false,
    linecolor   = EHAccretionGold,
    innerleftmargin  = 8pt,
    innerrightmargin = 8pt,
    innertopmargin   = 6pt,
    innerbottommargin = 6pt,
  },
]{ehdefinition}

\declaretheorem[style=ehtheorem,  numberwithin=chapter, name=Theorem]{theorem}
\declaretheorem[style=ehtheorem,  numberwithin=chapter, name=Lemma]{lemma}
\declaretheorem[style=ehtheorem,  numberwithin=chapter, name=Proposition]{proposition}
\declaretheorem[style=ehdefinition, numberwithin=chapter, name=Definition]{definition}

% ---------- Chapter style ----------
\makechapterstyle{eventhorizon}{%
  \renewcommand*{\printchaptername}{%
    \noindent\rule{\linewidth}{0.4pt}\par\vskip4pt
    {\sffamily\small\scshape\color{EHMarginGray}%
    \MakeUppercase{\@chapapp}}\par\vskip2pt
  }%
  \renewcommand*{\printchapternum}{%
    {\fontsize{60}{60}\selectfont\sffamily\bfseries%
    \color{EHAccretionGold}\thechapter}\par\vskip8pt
  }%
  \renewcommand*{\printchaptertitle}[1]{%
    {\Huge\sffamily\bfseries ##1}\par\vskip6pt
    \noindent\rule{\linewidth}{0.4pt}\par
  }%
  \renewcommand*{\afterchapternum}{}%
  \renewcommand*{\afterchaptertitle}{\vskip 20pt}%
}
\chapterstyle{eventhorizon}

% Chapter epigraph
\newcommand{\chapterepigraph}[2]{%
  \vskip 6pt
  \begin{flushright}
  \begin{minipage}{0.65\textwidth}
    \small\itshape #1
    \par\vskip 4pt
    \normalfont\small --- #2
  \end{minipage}
  \end{flushright}
  \vskip 12pt
}

% Full-width chapter image
\newcommand{\chapterimage}[2][]{%
  \vskip 12pt
  \noindent\includegraphics[width=\textwidth, #1]{#2}%
  \vskip 12pt
}

% ---------- Part style ----------
\renewcommand{\partnamefont}{\sffamily\Large\scshape\color{EHMarginGray}}
\renewcommand{\partnumfont}{\sffamily\fontsize{72}{72}\selectfont\bfseries\color{EHAccretionGold}}
\renewcommand{\parttitlefont}{\sffamily\Huge\bfseries\color{black}}
\renewcommand{\beforepartskip}{\null\vfil}
\renewcommand{\midpartskip}{\par\vskip 10pt\noindent\rule{0.5\textwidth}{1pt}\par\vskip 10pt}
\renewcommand{\afterpartskip}{\vfil\newpage}

% ---------- Headers and footers ----------
\makepagestyle{ehbook}
\makeevenhead{ehbook}{\thepage}{}{\small\itshape\leftmark}
\makeoddhead{ehbook}{\small\itshape\rightmark}{}{\thepage}
\makeevenfoot{ehbook}{}{}{}
\makeoddfoot{ehbook}{}{}{}
\makepsmarks{ehbook}{%
  \nouppercaseheads
  \createmark{chapter}{left}{shownumber}{\@chapapp\ }{. \ }
  \createmark{section}{right}{shownumber}{}{. \ }
}
\pagestyle{ehbook}

% Plain style for chapter openings
\makeevenfoot{plain}{}{}{}
\makeoddfoot{plain}{}{}{}

% ---------- Section formatting ----------
\setsecheadstyle{\Large\sffamily\bfseries\color{black}}
\setsubsecheadstyle{\large\sffamily\bfseries\color{black}}
\setsubsubsecheadstyle{\normalsize\sffamily\bfseries\color{black}}

% ---------- TikZ libraries ----------
\usetikzlibrary{calc,arrows.meta,decorations.markings,positioning}

% ---------- Miscellaneous ----------
\setcounter{tocdepth}{2}
\setcounter{secnumdepth}{3}

\endinput
