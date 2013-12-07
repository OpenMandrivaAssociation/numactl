%define major 1
%define libname %mklibname numa %{major}
%define devname %mklibname numa -d

Summary:	Simple NUMA policy support
Name:		numactl
Version:	2.0.8
Release:	8
License:	LGPLv2/GPLv2
Group:		System/Configuration/Hardware
Url:		ftp://oss.sgi.com/www/projects/libnuma/download
Source0:	ftp://oss.sgi.com/www/projects/libnuma/download/%{name}-%{version}.tar.gz
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

%package -n	%{devname}
Summary:	Headers and libraries for NUMA policy
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	numa-devel = %{version}-%{release}

%description -n	%{devname}
This package contains headers and libraries useful for developing
applications using different NUMA policies.

%prep
%setup -q

%build
%setup_compile_flags

%make CFLAGS="%{optflags} -I."

%install
%makeinstall_std prefix=%{buildroot}/usr

%files
%doc README CHANGES
%{_bindir}/memhog
%{_bindir}/numactl
%{_bindir}/numademo
%{_bindir}/numastat
%{_bindir}/migratepages
%{_bindir}/migspeed
%{_mandir}/man8/*.8*

%files -n %{libname}
%{_libdir}/libnuma.so.%{major}*

%files -n %{devname}
%{_libdir}/libnuma.so
%{_libdir}/libnuma.a
%{_includedir}/numa.h
%{_includedir}/numaif.h
%{_includedir}/numacompat1.h
%{_mandir}/man3/*

