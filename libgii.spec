Summary:	General Input Interface library fo LibGGI
Summary(pl):	Biblioteka do obs³ugi urz±dzeñ wej¶ciowych dla GGI
Name:		libgii
Version:	0.6
Release:	4
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
License:	GPL
Source0:	ftp://ftp.ggi-project.org/pub/ggi/ggi/current/%{name}-%{version}.tar.bz2
URL:		http://www.ggi-project.org/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc

%description
LibGII (General Input Interface) is intended to be to input what our
LibGGI (General Graphics Interface) library is to graphics. The goal
of LibGII is to provide a single easy to use, but yet powerful, API
for all possible input sources. However we are not there yet. The API
is far from set in stone yet, and is likely to change.

%description -l pl
Biblioteka do obs³ugi urz±dzeñ wej¶ciowych dla GGI.

%package X11
Summary:	LibGII X11 input
Summary(pl):	LibGII - obs³uga urz±dzeñ wej¶ciowych w X11
Group:		Libraries
Group(de):	Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description X11
X11 input for GGI.

%description X11 -l pl
LibGII - obs³uga urz±dzeñ wej¶ciowych w X11.

%package devel
Summary:	Development part of LibGII
Summary(pl):	Czê¶æ dla programistów biblioteki LibGII
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Development part of LibGII.

%description devel -l pl
Pliki potrzebne do programowania z wykorzystaniem LibGII.

%prep
%setup  -q

%build
%configure \
	--disable-debug
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install demos/*.c $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

gzip -9nf README ChangeLog NEWS doc/*.txt doc/*.sgml

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
%attr(755,root,root) %{_libdir}/ggi/input/linux_joy.so
%attr(755,root,root) %{_libdir}/ggi/input/linux_kbd.so
%attr(755,root,root) %{_libdir}/ggi/input/linux_mouse.so
%attr(755,root,root) %{_libdir}/ggi/input/mouse.so
%attr(755,root,root) %{_libdir}/ggi/input/null.so
%attr(755,root,root) %{_libdir}/ggi/input/spaceorb.so
%attr(755,root,root) %{_libdir}/ggi/input/stdin.so

%{_mandir}/man1/*

%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xsendbut
%attr(755,root,root) %{_libdir}/ggi/input/x*.so

%files devel
%defattr(644,root,root,755)
%doc *.gz %doc doc/*.txt* doc/*.sgml*
%doc %{_examplesdir}/%{name}
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/ggi/*/*.la
%{_includedir}/*
%{_mandir}/man3/*
