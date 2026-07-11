%global tl_name comment
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.8
Release:	%{tl_revision}.1
Summary:	Selectively include/exclude portions of text
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/comment
License:	gpl2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/comment.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/comment.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Selectively include/exclude pieces of text, allowing the user to define
new, separately controlled, comment versions. All text between \comment
... \endcomment or \begin{comment} ... \end{comment} is discarded. The
opening and closing commands should appear on a line of their own. No
starting spaces, nothing after it. This environment should work with
arbitrary amounts of comment, and the comment can be arbitrary text.
Other 'comment' environments are defined and selected/deselected with
\includecomment{versiona} and \excludecomment{versionb} These
environments are used as \versiona ... \endversiona or \begin{versiona}
... \end{versiona} with the opening and closing commands again on a line
of their own.

