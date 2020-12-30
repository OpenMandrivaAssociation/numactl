%define major 1
%define libname %mklibname numa %{major}
%define devname %mklibname numa -d
%define _disable_lto 1

Summary:	Simple NUMA policy support
Name:		numactl
Version:	2.0.14
Release:	1
License:	LGPLv2/GPLv2
Group:		System/Configuration/Hardware
Url:		ftp://oss.sgi.com/www/projects/libnuma/download
Source0:	https://github.com/numactl/numactl/releases/download/v%{version}/%{name}-%{version}.tar.gz
ExclusiveArch:	%{ix86} %{x86_64} ia64 aarch64 %{riscv}

%description
This package contains the `numactl' program to run other programs with
a specific NUMA policy.

%files
%{_bindir}/memhog
%{_bindir}/numactl
%{_bindir}/numademo
%{_bindir}/numastat
%{_bindir}/migratepages
%{_bindir}/migspeed
%{_mandir}/man8/*.8*

#----------------------------------------------------------------------------

%package -n	%{libname}
Summary:	Runtime libraries for NUMA policy support
Group:		System/Libraries

%description -n	%{libname}
This package contains the dynamic libraries for NUMA policy support.

%files -n %{libname}
%{_libdir}/libnuma.so.%{major}*

#----------------------------------------------------------------------------

%package -n	%{devname}
Summary:	Headers and libraries for NUMA policy
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	numa-devel = %{version}-%{release}

%description -n	%{devname}
This package contains headers and libraries useful for developing
applications using different NUMA policies.

%files -n %{devname}
%{_libdir}/libnuma.so
%{_libdir}/libnuma.a
%{_includedir}/numa.h
%{_includedir}/numaif.h
%{_includedir}/numacompat1.h
%{_libdir}/pkgconfig/numa.pc
%{_mandir}/man3/*
%{_mandir}/man2/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%setup_compile_flags
%configure --prefix=/usr --libdir=%{_libdir} --enable-static

%make_build CFLAGS="%{optflags} -I."

%install
%make_install prefix=%{buildroot}/usr
