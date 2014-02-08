# revision 25389
# category ConTeXt
# catalog-ctan /macros/context/contrib/context-simpleslides
# catalog-date 2012-02-13 08:38:17 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-context-simpleslides
Version:	20120213
Release:	2
Summary:	A module for preparing presentations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/context/contrib/context-simpleslides
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-simpleslides.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-simpleslides.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
This Context module provides an easy-to-use interface for
creating presentations for use with a digital projector. The
presentations are not interactive (no buttons, hyperlinks or
navigational tools such as tables of contents). Graphics may be
mixed with the text of slides. The module provides several
predefined styles, designed for academic presentation. Most
styles are configurable, and it is easy to design new styles.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/scripts/context/lua/third/simpleslides/mtx-simpleslides.lua
%{_texmfdistdir}/tex/context/interface/third/t-simpleslides.xml
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-c-default.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-f-default.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-BigNumber.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-BottomSquares.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-Boxed.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-BoxedTitle.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-Ellipse.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-Embossed.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-Framed.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-FramedTitle.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-HorizontalStripes.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-NarrowStripes.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-PlainCounter.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-RainbowStripe.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-Rounded.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-Shaded.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-SideSquares.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-SideToc.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-Split.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-Sunrise.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-Swoosh.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-ThickStripes.tex
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-default.tex
%{_texmfdistdir}/tex/context/third/simpleslides/t-simpleslides.mkii
%{_texmfdistdir}/tex/context/third/simpleslides/t-simpleslides.mkiv
%{_texmfdistdir}/tex/context/third/simpleslides/t-simpleslides.tex
%doc %{_texmfdistdir}/doc/context/third/simpleslides/example.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/example.tex
%doc %{_texmfdistdir}/doc/context/third/simpleslides/simpleslides.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/simpleslides.tex
%doc %{_texmfdistdir}/doc/context/third/simpleslides/solutions/generic-talk-15min-45min.tex
%doc %{_texmfdistdir}/doc/context/third/simpleslides/solutions/speaker_introduction-2min.tex
%doc %{_texmfdistdir}/doc/context/third/simpleslides/solutions/style-template.tex
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/BigNumber-blue.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/BigNumber-red.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/BottomSquares.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/Boxed.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/Ellipse.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/Embossed.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/Framed-square.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/Framed-stripe.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/FramedTitle.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/HorizontalStripes-blue.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/HorizontalStripes-green.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/HorizontalStripes-red.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/NarrowStripes-blue.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/NarrowStripes-green.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/NarrowStripes-red.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/RainbowStripe.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/Rounded.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/Shaded-blue.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/Shaded-bluered.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/Shaded-green.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/SideSquares.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/SideToc.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/Split.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/Sunrise.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/Swoosh.pdf
%doc %{_texmfdistdir}/doc/context/third/simpleslides/styles/ThickStripes.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Feb 23 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120213-1
+ Revision: 779434
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 20091103-2
+ Revision: 750529
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20091103-1
+ Revision: 718143
- texlive-context-simpleslides
- texlive-context-simpleslides
- texlive-context-simpleslides
- texlive-context-simpleslides
- texlive-context-simpleslides

