%define name	numactl
%define version 2.0.3
%define release	%mkrel 4
%define libname	%mklibname numa 1
%define develname	%mklibname numa -d

Summary:	Simple NUMA policy support
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	LGPLv2/GPLv2
Group:		System/Configuration/Hardware
Url:		ftp://oss.sgi.com/www/projects/libnuma/download
Source0:	ftp://oss.sgi.com/www/projects/libnuma/download/%{name}-%{version}.tar.gz
# Fedora patch, fixes RH bug #499633
# (libnuma: Warning: /sys not mounted or invalid)
Patch2:		numactl-2.0.3-rc3-distance_parsing.patch
ExclusiveArch:	%{ix86} x86_64 ia64
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This package contains the `numactl' program to run other programs with
a specific NUMA policy.

%package -n	%{libname}
Summary:	Runtime libraries for NUMA policy support
Group:		System/Libraries
Requires:	kernel >= 2.6.7

%description -n	%{libname}
This package contains the dynamic libraries for NUMA policy support.

%package -n	%{develname}
Summary:	Headers and libraries for NUMA policy
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	numa-devel = %{version}-%{release}
Obsoletes:  %mklibname numa -d 1

%description -n	%{develname}
This package contains headers and libraries useful for developing
applications using different NUMA policies.

%prep
%setup -q 
%patch2 -p1 

%build
%make CFLAGS="%{optflags} -I."

%install
rm -rf %{buildroot}
%makeinstall_std prefix=%{buildroot}/usr


%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

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

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libnuma.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/libnuma.so
%{_libdir}/libnuma.a
%{_includedir}/numa.h
%{_includedir}/numaif.h
%{_includedir}/numacompat1.h
%{_mandir}/man3/*
