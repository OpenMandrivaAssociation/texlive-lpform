%global tl_name lpform
%global tl_revision 36918

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Typesetting linear programming formulations and sets of equations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/lpform
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lpform.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lpform.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is designed to aid the author writing linear programming
formulations, one restriction at a time. With the package, one can
easily label equations, formulations can span multiple pages and several
elements of the layout (such as spacing, texts and equation tags) are
also customizable. Besides linear programming formulations, this package
can also be used to display any series of aligned equations with easy
labeling/referencing and other customization options.

