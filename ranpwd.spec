Name:           ranpwd
Version:        1.2
Release:        %mkrel 4
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

