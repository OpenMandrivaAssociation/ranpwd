Name:           ranpwd
Version:        1.2
Release:        %mkrel 5
Summary:        Program for generating random passwords
License:        GPL
Group:          Text tools
URL:            ftp://ftp.kernel.org/pub/software/utils/admin/ranpwd/
Source0:        ftp://ftp.kernel.org/pub/software/utils/admin/ranpwd/ranpwd-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
The ranpwd program can be used to generate random passwords using the in-kernel
cryptographically secure random number generator.

%prep
%setup -q

%build
%{configure2_5x}
%{make}

%install
%{__rm} -rf %{buildroot}
%{make} install INSTALLROOT=%{buildroot}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc
%attr(0755,root,root) %{_bindir}/ranpwd
%{_mandir}/man1/ranpwd.1*



%changelog
* Tue Sep 08 2009 Thierry Vignaud <tvignaud@mandriva.com> 1.2-5mdv2010.0
+ Revision: 433056
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2-4mdv2009.0
+ Revision: 260043
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 1.2-3mdv2009.0
+ Revision: 247862
- rebuild

* Sun Jan 20 2008 David Walluck <walluck@mandriva.org> 1.2-1mdv2008.1
+ Revision: 155269
- import ranpwd


