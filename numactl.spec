%define major 1
%define libname %mklibname numa %{major}
%define develname %mklibname numa -d

Summary:	Simple NUMA policy support
Name:		numactl
Version:	2.0.8
Release:	3
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

%package -n	%{develname}
Summary:	Headers and libraries for NUMA policy
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	numa-devel = %{version}-%{release}
Obsoletes:	%mklibname numa -d 1

%description -n	%{develname}
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

%files -n %{develname}
%{_libdir}/libnuma.so
%{_libdir}/libnuma.a
%{_includedir}/numa.h
%{_includedir}/numaif.h
%{_includedir}/numacompat1.h
%{_mandir}/man3/*


%changelog
* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-4mdv2011.0
+ Revision: 666633
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-3mdv2011.0
+ Revision: 606833
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 2.0.3-2mdv2010.1
+ Revision: 523445
- rebuilt for 2010.1

* Wed Jun 10 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.3-1mdv2010.0
+ Revision: 384890
- Update to new version 2.0.3
- Remove -Werror=format-security patch: integrated upstream

* Thu May 21 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.3-0.rc3.333mdv2010.0
+ Revision: 378372
- Don't package doc files in devel subpackage, they are already included in
  numactl

* Thu May 21 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.3-0.rc3.2mdv2010.0
+ Revision: 378343
- Don't build with -fPic and remove clearcache build fix patch for
  -fPic which is not needed anymore now, as recommended by upstream:
  http://markmail.org/message/2toadsrvr3w5ht67

* Thu May 21 2009 Frederik Himpe <fhimpe@mandriva.org> 2.0.3-0.rc3.1mdv2010.0
+ Revision: 378340
- Sync with Fedora in order to be able to build libvirt correctly with
  numa support:
- Update to new version 2.0.3-rc3
- Add patch fixing RH bug #499633 (libnuma: Warning: /sys not mounted
  or invalid)

* Sun May 10 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.0.2-1mdv2010.0
+ Revision: 373970
- new version

  + Giuseppe Ghibò <ghibo@mandriva.com>
    - Remove annoying warning "libnuma: Warning: /sys not mounted" for systems not having numa mounted (FC).
    - Add Provides: numa-devel.
    - Add %%{ix_86} arch to supported archs.
    - Update to relese 2.0.2
    - Merged Patch1 from Fedora.

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 1.0.1-3mdv2009.0
+ Revision: 241098
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 22 2007 Erwan Velu <erwan@mandriva.org> 1.0.1-1mdv2008.0
+ Revision: 69299
- 1.0.1
- Fixing url
  0.9.11

* Mon Apr 23 2007 Erwan Velu <erwan@mandriva.org> 0.9.10-1mdv2008.0
+ Revision: 17632
- 0.9.10
- Import numactl



* Wed Jan 04 2006 Erwan Velu <erwan@seanodes.com> 0.9-1mdk
- 0.9

* Wed May 18 2005 Gwenole Beauchesne <gbeauchesne@mandriva.com> 0.6.4-1mdk
- First Mandriva Linux release
