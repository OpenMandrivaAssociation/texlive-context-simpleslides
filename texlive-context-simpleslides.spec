Name:		texlive-context-simpleslides
Version:	63903
Release:	2
Summary:	TeXLive context-simpleslides package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-simpleslides.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/context-simpleslides.doc.r%{version}.tar.xz
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
%{_texmfdistdir}/scripts/context/lua/third/simpleslides
%{_texmfdistdir}/tex/context/interface/third/t-simpleslides.xml
%{_texmfdistdir}/tex/context/third/simpleslides
%doc %{_texmfdistdir}/doc/context/third/simpleslides

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar scripts tex doc %{buildroot}%{_texmfdistdir}
