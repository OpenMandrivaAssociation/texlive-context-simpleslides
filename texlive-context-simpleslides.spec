%global tl_name context-simpleslides
%global tl_revision 67070

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A module for preparing presentations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/context/contrib/context-simpleslides
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-simpleslides.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/context-simpleslides.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(context)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This ConTeXt module provides an easy-to-use interface for creating
presentations for use with a digital projector. The presentations are
not interactive (no buttons, hyperlinks or navigational tools such as
tables of contents). Graphics may be mixed with the text of slides. The
module provides several predefined styles, designed for academic
presentation. Most styles are configurable, and it is easy to design new
styles.

