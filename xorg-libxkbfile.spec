Summary:	xkbfile library
Name:		xorg-libxkbfile
Version:	1.0.8
Release:	5
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libxkbfile-%{version}.tar.bz2
# Source0-md5:	19e6533ae64abba0773816a23f2b9507
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-libX11-devel
BuildRequires:	xorg-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xkbfile library.

%package devel
Summary:	Header files for libxkbfile library
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
xkbfile library.

This package contains the header files needed to develop programs that
use libxkbfile.

%prep
%setup -qn libxkbfile-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-silent-rules	\
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun -p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %ghost %{_libdir}/libxkbfile.so.?
%attr(755,root,root) %{_libdir}/libxkbfile.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libxkbfile.so
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/xkbfile.pc

