%define rel	0.3

Summary:	HostAP utils
Summary(es):	Herramientas HostAP
Summary(pl):	Narzedzia HostAP
Name:		hostap-utils
Version:	0.1.0
Release:	%{rel}
License:	GPL
Group:		Applications/System
Source0:	http://hostap.epitest.fi/releases/%{name}-%{version}.tar.gz
URL:		http://hostap.epitest.fi/
BuildRequires:	%{kgcc_package}
BuildRequires:	rpmbuild(macros) >= 1.118
BuildRequires:	kernel-headers
Requires:	kernel-net-hostap
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for HostAP and WLAN.

%description -l es
Unas herramientas para HostAP y WLAN.

%description -l pl
Narzedzia dla HostAP i sieci bezprzewodowych.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/sbin
#hostap utils
install hostap_{crypt_conf,diag,io_debug,rid} $RPM_BUILD_ROOT/sbin
install prism2_{param,srec} $RPM_BUILD_ROOT/sbin
install split_combined_hex $RPM_BUILD_ROOT/sbin

%post

%preun

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/hostap_*
%attr(755,root,root) /sbin/prism2_*
%attr(755,root,root) /sbin/split_combined_hex
