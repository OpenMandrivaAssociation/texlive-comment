Name:		texlive-comment
Version:	41927
Release:	2
Summary:	Selectively include/excludes portions of text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/comment
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comment.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comment.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/comment
%doc %{_texmfdistdir}/doc/latex/comment

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
