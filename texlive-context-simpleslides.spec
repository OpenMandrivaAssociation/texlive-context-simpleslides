# revision 28300
# category ConTeXt
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-context-simpleslides
Version:	20131012
Release:	4
Summary:	TeXLive context-simpleslides package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-simpleslides.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-simpleslides.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-context

%description
TeXLive context-simpleslides package.

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
%{_texmfdistdir}/tex/context/third/simpleslides/simpleslides-s-FuzzyTopic.tex
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
%{_texmfdistdir}/tex/context/third/simpleslides/t-slidesvisualcounter.tex
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
