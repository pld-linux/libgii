#
# Conditional build:
%bcond_with	pthreads # with pthreads support
#
Summary:	General Input Interface library fo LibGGI
Summary(pl):	Biblioteka do obs³ugi urz±dzeñ wej¶ciowych dla GGI
Name:		libgii
Version:	0.8.5
Release:	1
License:	BSD-like
Group:		Libraries
Source0:	http://www.ggi-project.org/ftp/ggi/current/%{name}-%{version}.src.tar.bz2
# Source0-md5:	1584ff2417198d413252a13ce4b6c80f
Patch0:		%{name}-llh.patch
URL:		http://www.ggi-project.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool >= 1:1.4.2-9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibGII (General Input Interface) is intended to be to input what our
LibGGI (General Graphics Interface) library is to graphics. The goal
of LibGII is to provide a single easy to use, but yet powerful, API
for all possible input sources. However we are not there yet. The API
is far from set in stone yet, and is likely to change.

%description -l pl
Biblioteka LibGII (General Intput Interface) zosta³a przewidziana do
obs³ugi urz±dzeñ wej¶ciowych, podobnie jak LibGGI (General Graphics
Interface) - graficznych urz±dzeñ wyj¶ciowych. G³ównym celem
biblioteki jest dostarczenie jednolitego i prostego w u¿yciu API dla
wszystkich mo¿liwych urz±dzeñ wej¶ciowych.

%package X11
Summary:	LibGII X11 input
Summary(pl):	LibGII - obs³uga urz±dzeñ wej¶ciowych w X11
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description X11
X11 input for GGI.

%description X11 -l pl
LibGII - obs³uga urz±dzeñ wej¶ciowych w X11.

%package devel
Summary:	Development part of LibGII
Summary(pl):	Czê¶æ dla programistów biblioteki LibGII
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development part of LibGII.

%description devel -l pl
Pliki potrzebne do programowania z wykorzystaniem LibGII.

%prep
%setup -q
%patch0 -p1

rm -f input/xwin/xev.c m4/{libtool,ltdl}.m4

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoheader}
%{__autoconf}
%{__automake}
%configure \
	%{?with_pthreads:--enable-mutexes=pthread} \
	%{!?debug:--disable-debug}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install demos/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

rm -f $RPM_BUILD_ROOT%{_libdir}/ggi/{filter,input}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README NEWS doc/*.txt
%dir %{_sysconfdir}/ggi
%dir %{_sysconfdir}/ggi/filter
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ggi/libgii.conf
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/ggi/filter/*
%attr(755,root,root) %{_bindir}/mhub
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%dir %{_libdir}/ggi
%dir %{_libdir}/ggi/filter
%attr(755,root,root) %{_libdir}/ggi/filter/*.so
%dir %{_libdir}/ggi/input
%attr(755,root,root) %{_libdir}/ggi/input/file.so
%attr(755,root,root) %{_libdir}/ggi/input/linux_evdev.so
%attr(755,root,root) %{_libdir}/ggi/input/linux_joy.so
%attr(755,root,root) %{_libdir}/ggi/input/linux_kbd.so
%attr(755,root,root) %{_libdir}/ggi/input/linux_mouse.so
%attr(755,root,root) %{_libdir}/ggi/input/mouse.so
%attr(755,root,root) %{_libdir}/ggi/input/null.so
%attr(755,root,root) %{_libdir}/ggi/input/spaceorb.so
%attr(755,root,root) %{_libdir}/ggi/input/stdin.so
%attr(755,root,root) %{_libdir}/ggi/input/tcp.so
%{_mandir}/man1/*
%{_mandir}/man7/*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xsendbut
%attr(755,root,root) %{_libdir}/ggi/input/x*.so

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
