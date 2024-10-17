Name:		texlive-kerntest
Version:	15878
Release:	2
Summary:	Print tables and generate control files to adjust kernings
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/kerntest
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kerntest.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kerntest.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/kerntest.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This class makes it easy to generate tables that show many
different kerning pairs of an arbitrary font, usable by LaTeX.
It shows the kerning values that are used in the the font by
default. In addition, this class enables the user to alter the
kernings and to observe the results. Kerning pairs can be
defined for groups of similar glyphs at the same time. An mtx
file is generated automatically. The mtx file may then be
loaded by fontinst to introduce the user-made kernings into the
virtual font for later use in LaTeX.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/kerntest/kerntest.cls
%{_texmfdistdir}/tex/latex/kerntest/ly1mtx.clo
%{_texmfdistdir}/tex/latex/kerntest/ot1mtx.clo
%{_texmfdistdir}/tex/latex/kerntest/t1cmr-1200.fd
%{_texmfdistdir}/tex/latex/kerntest/t1mtx.clo
%{_texmfdistdir}/tex/latex/kerntest/t2amtx.clo
%{_texmfdistdir}/tex/latex/kerntest/t2bmtx.clo
%{_texmfdistdir}/tex/latex/kerntest/ts1mtx.clo
%doc %{_texmfdistdir}/doc/latex/kerntest/ChangeLog
%doc %{_texmfdistdir}/doc/latex/kerntest/README
%doc %{_texmfdistdir}/doc/latex/kerntest/ToDo
%doc %{_texmfdistdir}/doc/latex/kerntest/kerntest.pdf
%doc %{_texmfdistdir}/doc/latex/kerntest/krntst-v.tex
%doc %{_texmfdistdir}/doc/latex/kerntest/ot1-XXX-m-n.tex
%doc %{_texmfdistdir}/doc/latex/kerntest/schoolb.map
%doc %{_texmfdistdir}/doc/latex/kerntest/schoolb1.tex
%doc %{_texmfdistdir}/doc/latex/kerntest/schoolb2.tex
%doc %{_texmfdistdir}/doc/latex/kerntest/t1-9nc-m-n-1.tex
%doc %{_texmfdistdir}/doc/latex/kerntest/t1-9nc-m-n-2.tex
%doc %{_texmfdistdir}/doc/latex/kerntest/t1-XXX-m-n.tex
%doc %{_texmfdistdir}/doc/latex/kerntest/t1-cmr-m-n-1200.tex
%doc %{_texmfdistdir}/doc/latex/kerntest/t1-ptm-bx-n-example.tex
%doc %{_texmfdistdir}/doc/latex/kerntest/t1-ptm-m-n-shortexample.tex
%doc %{_texmfdistdir}/doc/latex/kerntest/t1-ptm-m-n.tex
%doc %{_texmfdistdir}/doc/latex/kerntest/testschoolb.tex
%doc %{_texmfdistdir}/doc/latex/kerntest/ts1-XXX-m-n.tex
#- source
%doc %{_texmfdistdir}/source/latex/kerntest/Makefile
%doc %{_texmfdistdir}/source/latex/kerntest/kerntest.dtx
%doc %{_texmfdistdir}/source/latex/kerntest/kerntest.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
