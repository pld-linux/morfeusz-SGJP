Summary:	Morfeusz morphological analyzer
Summary(pl.UTF-8):	Analizator morfologiczny Morfeusz
Name:		morfeusz-SGJP
Version:	20110416
Release:	2
License:	BSD
Group:		Applications/Dictionaries
Source0:	http://sgjp.pl/morfeusz/download/%{name}-src-%{version}.tar.bz2
# Source0-md5:	f2ab93a0df3638f0c8a198c569aa3b63
Patch0:		opt.patch
URL:		http://sgjp.pl/morfeusz/
BuildRequires:	libstdc++-devel
BuildRequires:	readline-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Morpheus program performs morphological analysis for the Polish
language. The current version does not contain the module for guessing
unknown words.

%description -l pl.UTF-8
Program Morfeusz wykonuje analizę morfologiczną dla języka polskiego.
W obecnej wersji nie zawiera modułu zgadującego nieznane słowa (można
więc powiedzieć, że jest słownikiem morfologicznym).

%package devel
Summary:	Development files for Morfeusz
Summary(pl.UTF-8):	Pliki do tworzenia aplikacji wykorzystujących Morfeusza
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development files for Morfeusz.

%description devel -l pl.UTF-8
Pliki do tworzenia aplikacji wykorzystujących Morfeusza.

%prep
%setup -q -c
%patch0 -p1

%build
mkdir build
cd build
%ifarch %{x8664}
ln -s ../Makefile.linux64 Makefile
%else
ln -s ../Makefile.linux32 Makefile
%endif

%{__make} -j1 \
	LDFLAGS="%{rpmldflags}" \
	OPT="%{rpmcppflags} %{rpmcflags} -Wno-error"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_includedir}}

install -p build/libmorfeusz* $RPM_BUILD_ROOT%{_libdir}
install -p build/morfeusz* $RPM_BUILD_ROOT%{_bindir}
install -p morfeusz.h $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc CZYTAJTO README
%attr(755,root,root) %{_bindir}/morfeusz
%attr(755,root,root) %ghost %{_libdir}/libmorfeusz.so.0
%attr(755,root,root) %{_libdir}/libmorfeuszSGJP.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmorfeusz.so
%{_includedir}/morfeusz.h
