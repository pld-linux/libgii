#
# Conditional build:
%bcond_with	pthreads	# with pthreads support
%bcond_with	static_modules	# build static library AND make all modules builtin (also in shared lib)
#
Summary:	General Input Interface library fo LibGGI
Summary(pl.UTF-8):	Biblioteka do obsługi urządzeń wejściowych dla GGI
Name:		libgii
Version:	1.0.2
Release:	6
License:	BSD-like
Group:		Libraries
Source0:	http://www.ggi-project.org/ftp/ggi/v2.2/%{name}-%{version}.src.tar.bz2
# Source0-md5:	e002b3b3b7fae2b2558fe7ac854359b7
Patch0:		format-security.patch
URL:		http://www.ggi-project.org/
BuildRequires:	autoconf >= 2.59-9
BuildRequires:	automake >= 1.4
BuildRequires:	libtool >= 2:2.0
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXxf86dga-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibGII (General Input Interface) is intended to be to input what our
LibGGI (General Graphics Interface) library is to graphics. The goal
of LibGII is to provide a single easy to use, but yet powerful, API
for all possible input sources. However we are not there yet. The API
is far from set in stone yet, and is likely to change.

%description -l pl.UTF-8
Biblioteka LibGII (General Input Interface) została przewidziana do
obsługi urządzeń wejściowych, podobnie jak LibGGI (General Graphics
Interface) - graficznych urządzeń wyjściowych. Głównym celem
biblioteki jest dostarczenie jednolitego i prostego w użyciu API dla
wszystkich możliwych urządzeń wejściowych.

%package X11
Summary:	LibGII X11 input
Summary(pl.UTF-8):	LibGII - obsługa urządzeń wejściowych w X11
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description X11
X11 input for GGI.

%description X11 -l pl.UTF-8
LibGII - obsługa urządzeń wejściowych w X11.

%package devel
Summary:	Development part of LibGII
Summary(pl.UTF-8):	Część dla programistów biblioteki LibGII
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%if %{with static_modules}
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXxf86dga-devel
%endif

%description devel
Development part of LibGII.

%description devel -l pl.UTF-8
Pliki potrzebne do programowania z wykorzystaniem LibGII.

%package static
Summary:	Static LibGII library
Summary(pl.UTF-8):	Biblioteka statyczna LibGII
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static LibGII library.

%description static -l pl.UTF-8
Biblioteka statyczna LibGII.

%prep
%setup -q
%patch0 -p1

%{__rm} acinclude.m4 m4/lt*.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_modules:--disable-static} \
	%{?with_pthreads:--enable-mutexes=pthread} \
	%{!?debug:--disable-debug}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install demos/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/ggi/{filter,input}/*.la
# inputs not supported on Linux
%{__rm} $RPM_BUILD_ROOT%{_mandir}/man7/input-{directx,quartz}.7

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc FAQ NEWS README
%dir %{_sysconfdir}/ggi
%dir %{_sysconfdir}/ggi/filter
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ggi/libgii.conf
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ggi/filter/keytrans
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/ggi/filter/mouse
%attr(755,root,root) %{_bindir}/mhub
%attr(755,root,root) %{_libdir}/libgg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgg.so.1
%attr(755,root,root) %{_libdir}/libgii.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgii.so.1
%dir %{_libdir}/ggi
%dir %{_libdir}/ggi/filter
%attr(755,root,root) %{_libdir}/ggi/filter/keytrans.so
%attr(755,root,root) %{_libdir}/ggi/filter/mouse.so
%attr(755,root,root) %{_libdir}/ggi/filter/save.so
%attr(755,root,root) %{_libdir}/ggi/filter/tcp.so
%dir %{_libdir}/ggi/input
%attr(755,root,root) %{_libdir}/ggi/input/file.so
%attr(755,root,root) %{_libdir}/ggi/input/linux_evdev.so
%attr(755,root,root) %{_libdir}/ggi/input/linux_joy.so
%attr(755,root,root) %{_libdir}/ggi/input/linux_kbd.so
%attr(755,root,root) %{_libdir}/ggi/input/linux_mouse.so
%attr(755,root,root) %{_libdir}/ggi/input/lk201.so
%attr(755,root,root) %{_libdir}/ggi/input/mouse.so
%attr(755,root,root) %{_libdir}/ggi/input/null.so
%attr(755,root,root) %{_libdir}/ggi/input/spaceorb.so
%attr(755,root,root) %{_libdir}/ggi/input/stdin.so
%attr(755,root,root) %{_libdir}/ggi/input/tcp.so
%{_mandir}/man1/mhub.1*
%{_mandir}/man5/libgii.conf.5*
%{_mandir}/man7/filter-key.7*
%{_mandir}/man7/filter-keytrans*
%{_mandir}/man7/filter-mouse.7*
%{_mandir}/man7/filter-save.7*
%{_mandir}/man7/filter-tcp.7*
%{_mandir}/man7/input-file.7*
%{_mandir}/man7/input-linux-evdev.7*
%{_mandir}/man7/input-linux-kbd.7*
%{_mandir}/man7/input-linux-mouse.7*
%{_mandir}/man7/input-lk201.7*
%{_mandir}/man7/input-mouse.7*
%{_mandir}/man7/input-tcp.7*
%{_mandir}/man7/libgg.7*
%{_mandir}/man7/libgii.7*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xsendbut
%attr(755,root,root) %{_libdir}/ggi/input/x.so
%{_mandir}/man1/xsendbut.1*
%{_mandir}/man7/input-x.7*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/libgg.so
%attr(755,root,root) %{_libdir}/libgii.so
%{_libdir}/libgg.la
%{_libdir}/libgii.la
%{_includedir}/ggi
%{_mandir}/man3/GG_*.3*
%{_mandir}/man3/gg*.3*
%{_mandir}/man3/gii*.3*
%{_examplesdir}/%{name}-%{version}

%if %{with static_modules}
%files static
%defattr(644,root,root,755)
%{_libdir}/libgg.a
%{_libdir}/libgii.a
%endif
