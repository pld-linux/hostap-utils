Summary:	HostAP utils
Summary(es):	Herramientas HostAP
Summary(pl):	Narzêdzia dla HostAP
Name:		hostap-utils
Version:	0.2.4
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://hostap.epitest.fi/releases/%{name}-%{version}.tar.gz
# Source0-md5:	774a892131b2e51599d39aab7722c7d9
URL:		http://hostap.epitest.fi/
Requires:	kernel-net-hostap >= 0.1.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tools for HostAP and WLAN.

%description -l es
Unas herramientas para HostAP y WLAN.

%description -l pl
Narzêdzia dla HostAP i sieci bezprzewodowych.

%prep
%setup -q

%build
%{__make}
# TODO: optflags

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/sbin

install hostap_{crypt_conf,diag,io_debug,rid} $RPM_BUILD_ROOT/sbin
install prism2_{param,srec} $RPM_BUILD_ROOT/sbin
install split_combined_hex $RPM_BUILD_ROOT/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /sbin/hostap_*
%attr(755,root,root) /sbin/prism2_*
%attr(755,root,root) /sbin/split_combined_hex
