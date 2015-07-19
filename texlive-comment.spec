# revision 32778
# category Package
# catalog-ctan /macros/latex/contrib/comment
# catalog-date 2014-01-23 22:28:28 +0100
# catalog-license gpl
# catalog-version 3.7
Name:		texlive-comment
Version:	3.7
Release:	5
Summary:	Selectively include/excludes portions of text
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/comment
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comment.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comment.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Selectively include/exclude pieces of text, allowing the user
to define new, separately controlled, comment versions. All
text between \comment ... \endcomment or \begin{comment} ...
\end{comment} is discarded. The opening and closing commands
should appear on a line of their own. No starting spaces,
nothing after it. This environment should work with arbitrary
amounts of comment, and the comment can be arbitrary text.
Other 'comment' environments are defined and
selected/deselected with \includecomment{versiona} and
\excludecoment{versionb} These environments are used as
\versiona ... \endversiona or \begin{versiona} ...
\end{versiona} with the opening and closing commands again on a
line of their own.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/comment/comment.sty
%doc %{_texmfdistdir}/doc/latex/comment/README
%doc %{_texmfdistdir}/doc/latex/comment/comm_latest.tex
%doc %{_texmfdistdir}/doc/latex/comment/comment.pdf
%doc %{_texmfdistdir}/doc/latex/comment/comment.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
