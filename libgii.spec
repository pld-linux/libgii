#
# Conditional build:
# _with_pthreads - with pthreads support
#
Summary:	General Input Interface library fo LibGGI
Summary(pl):	Biblioteka do obs≥ugi urz±dzeÒ wej∂ciowych dla GGI
Name:		libgii
Version:	0.8.1
Release:	2
License:	BSD-like
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Source0:	ftp://ftp.ggi-project.org/pub/ggi/ggi/current/%{name}-%{version}.tar.gz
Patch0:         %{name}-autoconf.patch
URL:		http://www.ggi-project.org/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
LibGII (General Input Interface) is intended to be to input what our
LibGGI (General Graphics Interface) library is to graphics. The goal
of LibGII is to provide a single easy to use, but yet powerful, API
for all possible input sources. However we are not there yet. The API
is far from set in stone yet, and is likely to change.

%description -l pl
Biblioteka LibGII (General Intput Interface) zosta≥a przewidziana do
obs≥ugi urz±dzeÒ wej∂ciowych, podobnie jak LibGGI (General Graphics
Interface) - graficznych urzadzeÒ wyj∂ciowych. G≥Ûwnym celem biblioteki
jest dostarczenie jednolitego i prostego w uøyciu API dla wszystkich
moøliwych urz±dzeÒ wej∂ciowych.

%package X11
Summary:	LibGII X11 input
Summary(pl):	LibGII - obs≥uga urz±dzeÒ wej∂ciowych w X11
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	‚…¬Ã…œ‘≈À…
Group(uk):	‚¶¬Ã¶œ‘≈À…
Requires:	%{name} = %{version}

%description X11
X11 input for GGI.

%description X11 -l pl
LibGII - obs≥uga urz±dzeÒ wej∂ciowych w X11.

%package devel
Summary:	Development part of LibGII
Summary(pl):	CzÍ∂Ê dla programistÛw biblioteki LibGII
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Development part of LibGII.

%description devel -l pl
Pliki potrzebne do programowania z wykorzystaniem LibGII.

%prep
%setup  -q
%patch0 -p1

%build
./autogen.sh
%configure \
	%{?_with_pthreads:--enable-mutexes=pthread} \
	%{?!debug:--disable-debug}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install demos/*.c $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

gzip -9nf README ChangeLog NEWS doc/*.txt

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_sysconfdir}/ggi
%{_sysconfdir}/ggi/libgii.conf
%dir %{_libdir}/ggi
%dir %{_libdir}/ggi/filter
%dir %{_libdir}/ggi/input

%attr(755,root,root) %{_bindir}/mhub
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/ggi/filter/*.so
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
%doc *.gz
%doc doc/*.txt*
%doc %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/ggi/*/*.la
%{_includedir}/*
%{_mandir}/man3/*
%{_mandir}/man9/*
