%define name	numactl
%define version	0.9.10
%define release	%mkrel 1
%define libname	%mklibname numa 1

Summary:	Simple NUMA policy support
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Patch0:		%{name}-0.9-DESTDIR.patch.bz2
License:	GPL/LGPL
Group:		System/Configuration/Hardware
Url:		http://www.firstfloor.org/~andi/numa.html
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	%{libname} = %{version}-%{release}
ExclusiveArch:	x86_64 ia64

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

%description -n	%{libname}-devel
This package contains headers and libraries useful for developing
applications using different NUMA policies.

%prep
%setup -q
#%patch0 -p0 -b .DESTDIR

%build
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%_mandir/man5/
%makeinstall_std prefix=$RPM_BUILD_ROOT/usr


%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

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
%{_mandir}/man8/numactl.8*
%{_mandir}/man5/*

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/libnuma.so.*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_libdir}/libnuma.so
%{_includedir}/numa.h
%{_includedir}/numaif.h
%{_defaultdocdir}/%{name}-%{version}/*
%{_mandir}/man3/*
