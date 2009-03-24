%define name	numactl
%define version 2.0.2
%define release	%mkrel 2
%define libname	%mklibname numa 1

Summary:	Simple NUMA policy support
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.9-DESTDIR.patch
Patch1:		%{name}-%{version}-clearcache-fix.patch
License:	GPL/LGPL
Group:		System/Configuration/Hardware
Url:		ftp://oss.sgi.com/www/projects/libnuma/download
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	%{libname} = %{version}-%{release}
ExclusiveArch:	%{ix86} x86_64 ia64

%description
This package contains the `numactl' program to run other programs with
a specific NUMA policy.

%package -n	%{libname}
Summary:	Runtime libraries for NUMA policy support
Group:		System/Libraries
Requires:	kernel >= 2.6.7

%description -n	%{libname}
This package contains the dynamic libraries for NUMA policy support.

%package -n	%{libname}-devel
Summary:	Headers and libraries for NUMA policy
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	numa-devel = %{version}-%{release}

%description -n	%{libname}-devel
This package contains headers and libraries useful for developing
applications using different NUMA policies.

%prep
%setup -q
%patch1 -p1 -b .cache

%build
%make CFLAGS="%{optflags} -I. -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_mandir/man5/
%makeinstall_std prefix=$RPM_BUILD_ROOT/usr


%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README CHANGES
%{_bindir}/memhog
%{_bindir}/numactl
%{_bindir}/numademo
%{_bindir}/numastat
%{_bindir}/migratepages
%{_bindir}/migspeed
%{_mandir}/man8/numactl.8*
%{_mandir}/man5/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libnuma.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/libnuma.so
%{_libdir}/libnuma.a
%{_includedir}/numa.h
%{_includedir}/numaif.h
%{_includedir}/numacompat1.h
%{_defaultdocdir}/%{name}/*
%{_mandir}/man3/*
