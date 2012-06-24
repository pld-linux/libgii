Summary:	General Input Interface library fo LibGGI
Summary(pl):	-
Name:		libgii
Version:	0.6
Release:	1
Group:		Library
Group(pl):	Biblioteki
Copyright:	GPL
Source0:	ftp://ftp.ggi-project.org/pub/ggi/ggi/current/%{name}-%{version}.tar.bz2
URL:		http://www.ggi-project.org/
BuildPrereq:	XFree86-devel
BuildRoot:   	/tmp/%{name}-%{version}-root

%description
LibGII (General Input Interface) is intended to be to input what our LibGGI
(General Graphics Interface) library is to graphics.

The goal of LibGII is to provide a single easy to use, but yet powerful,
API for all possible input sources. However we are not there yet. The
API is far from set in stone yet, and is likely to change.

%description -l pl

%package devel
Summary:	Development part of LibGII
Summary(pl):	Cz�� dla programist�w biblioteki LibGII
Group:		Development/Library
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Development part of LibGII.

%description devel -l pl
Pliki potrzebne do programowania z wykorzystaniem LibGII.

%define 	_sysconfdir	/etc

%prep
%setup  -q
#%patch0 -p1
#%patch1 -p1
#%patch2 -p1

%build
autoconf
LDFLAGS="-s" ; export LDFLAGS
%configure \
	--disable-debug \
	--sysconfdir=%{_sysconfdir}

make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/usr/src/examples/%{name}

make install \
	DESTDIR="$RPM_BUILD_ROOT"

install demos/*.c $RPM_BUILD_ROOT/usr/src/examples/%{name}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* \
	README ChangeLog NEWS doc/*.txt doc/*.sgml

%pre

%preun

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz NEWS.gz
%dir %{_libdir}/ggi
%dir %{_libdir}/ggi/filter
%dir %{_libdir}/ggi/input

%{_sysconfdir}/ggi
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(755,root,root) %{_libdir}/ggi/filter/*.so
%attr(755,root,root) %{_libdir}/ggi/input/*.so

%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc doc/*.txt* doc/*.sgml* ChangeLog.gz
%doc /usr/src/examples/%{name}

%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/ggi/*/*.la

%{_mandir}/man3/*


%changelog
* Tue May 18 1999 Artur Frysiak <wiget@pld.org.pl>
  [0.6-1]
- first version (writed from templete.spec)  
