%global packname  fUtilities
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          2110.78
Release:          2
Summary:          Function Utilities
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/Archive/%{packname}/%{packname}_%{version}.tar.gz
Requires:         R-methods R-MASS 
Requires:         R-tcltk R-RUnit R-akima R-spatial R-foreign 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-MASS
BuildRequires:    R-tcltk R-RUnit R-akima R-spatial R-foreign 

%description
Environment for teaching "Financial Engineering and Computational Finance"

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

# FIXME move to archives but required by R-rattle make check
# Error in set.lcgseed(seed = 65890) : 
#  cannot change value of locked binding for '.lcg.seed'
%if 0
%check
%{_bindir}/R CMD check %{packname}
%endif

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/COPYRIGHT.html
%{rlibdir}/%{packname}/DocCopying.pdf
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/unitTests


%changelog
* Tue Feb 21 2012 Paulo Andrade <pcpa@mandriva.com.br> 2110.78-1
+ Revision: 778315
- Import R-fUtilities
- Import R-fUtilities

