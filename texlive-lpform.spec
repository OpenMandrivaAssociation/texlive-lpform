Name:		texlive-lpform
Version:	36918
Release:	1
Summary:	Typesetting linear programming formulations and sets of equations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/lpform
License:	lppl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lpform.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lpform.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is designed to aid the author writing linear
programming formulations, one restriction at a time. With the
package, one can easily label equations, formulations can span
multiple pages and several elements of the layout (such as
spacing, texts and equation tags) are also customizable.
Besides linear programming formulations, this package can also
be used to display any series of aligned equations with easy
labeling/referencing and other customization options.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/lpform
%doc %{_texmfdistdir}/doc/generic/lpform

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
