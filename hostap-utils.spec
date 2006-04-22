Summary:	HostAP utils
Summary(es):	Herramientas HostAP
Summary(pl):	Narzêdzia dla HostAP
Name:		hostap-utils
Version:	0.4.7
Release:	1
License:	GPL v2
Group:		Applications/System
Source0:	http://hostap.epitest.fi/releases/%{name}-%{version}.tar.gz
# Source0-md5:	afe041581b8f01666e353bec20917c85
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
%{__make} \
	CC="%{__cc}" \
        CFLAGS="%{rpmcflags}" \
        LDFLAGS="%{rpmldflags}"

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
%doc ChangeLog README
%attr(755,root,root) /sbin/hostap_*
%attr(755,root,root) /sbin/prism2_*
%attr(755,root,root) /sbin/split_combined_hex
