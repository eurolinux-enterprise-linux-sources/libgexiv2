Name:           libgexiv2
Version:        0.10.4
Release:        4%{?dist}
Summary:        Gexiv2 is a GObject-based wrapper around the Exiv2 library

License:        GPLv2+
URL:            http://trac.yorba.org/wiki/gexiv2 
Source0:        https://download.gnome.org/sources/gexiv2/0.10/gexiv2-%{version}.tar.xz

Patch0:         %{name}-pkgconf.patch

# https://bugzilla.redhat.com/show_bug.cgi?id=1486570
Patch1:         %{name}-Adapt-to-Exiv2-BasicIo-API-change.patch

BuildRequires:  exiv2-devel >= 0.26
BuildRequires:  gobject-introspection-devel
BuildRequires:  libtool
BuildRequires:  python2-devel
BuildRequires:  python-gobject-base

# For tests
BuildRequires:  vala

%if !0%{?rhel}
BuildRequires:  python3-devel
BuildRequires:  python3-gobject-base
%endif

%description
libgexiv2 is a GObject-based wrapper around the Exiv2 library. 
It makes the basic features of Exiv2 available to GNOME applications.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n     python2-gexiv2
Summary:        Python2 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python-gobject-base%{?_isa}
# For upgrade path from F24
Provides:       libgexiv2-python2 = %{name}-%{version}
Obsoletes:      libgexiv2-python2 < 0.10.4

%description -n python2-gexiv2
This package contains the python2 bindings for %{name}

%if !0%{?rhel}
%package -n     python3-gexiv2
Summary:        Python3 bindings for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       python3-gobject-base%{?_isa}
# For upgrade path from F24
Provides:       libgexiv2-python3 = %{name}-%{version}
Obsoletes:      libgexiv2-python3 < 0.10.4

%description -n python3-gexiv2
This package contains the python3 bindings for %{name}
%endif

%prep
%setup -q -n gexiv2-%{version}
%patch0 -p1
%patch1 -p1

%build
%configure --enable-tests --enable-introspection --enable-static=no --enable-shared=yes
%make_build

%install
%make_install
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'

# move introspection typelib to correct location
mkdir -p $RPM_BUILD_ROOT%{_libdir}/girepository-1.0
mv $RPM_BUILD_ROOT%{_datadir}/gir-1.0/GExiv2-0.10.typelib \
   $RPM_BUILD_ROOT%{_libdir}/girepository-1.0/GExiv2-0.10.typelib

# Can't get this to work at the moment
# https://bugzilla.gnome.org/show_bug.cgi?id=723790
#%check
#make tests


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license COPYING
%doc AUTHORS THANKS README
%{_libdir}/libgexiv2.so.2*
%{_libdir}/girepository-1.0/GExiv2-0.10.typelib

%files devel
%{_includedir}/gexiv2/
%{_datadir}/gir-1.0/GExiv2-0.10.gir
%{_libdir}/libgexiv2.so
%{_libdir}/pkgconfig/gexiv2.pc
%dir %{_datadir}/vala
%dir %{_datadir}/vala/vapi
%{_datadir}/vala/vapi/gexiv2.vapi

%files -n python2-gexiv2
%{python2_sitearch}/gi/overrides/GExiv2.py*

%if !0%{?rhel}
%files -n python3-gexiv2
%{python3_sitearch}/gi/overrides/GExiv2.py
%{python3_sitearch}/gi/overrides/__pycache__/GExiv2*
%endif

%changelog
* Wed Oct 11 2017 Debarshi Ray <rishi@fedoraproject.org> - 0.10.4-4
- Ensure that the new exiv2 soname is used during the build
- Adapt to Exiv2::BasicIo API change
  Resolves: rhbz#1486570

* Tue Sep 19 2017 Richard Hughes <rhughes@redhat.com> - 0.10.4-3
- Rebuild against the rebased exiv2
- Resolves: rhbz#1486570

* Fri May 19 2017 Debarshi Ray <rishi@fedoraproject.org> - 0.10.4-2
- Add Provides to retain compatibility
  Resolves: rhbz#1387004

* Thu Feb 23 2017 Matthias Clasen <mclasen@redhat.com> - 0.10.4-1
- Rebase to 0.10.4
  Resolves: rhbz#1387004

* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 0.5.0-9
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 0.5.0-8
- Mass rebuild 2013-12-27

* Wed May 08 2013 Richard Hughes <richard@hughsie.com> 0.5.0-7
- RHEL7 does not have python3

* Wed Mar 20 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.5.0-6
- Fix requires

* Wed Mar 20 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.5.0-5
- Fix python bindings generation
- Add new subpackages for python2,3 bindings

* Tue Mar 19 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.5.0-4
- Add patch to remove overlinking rhbz#818587

* Mon Mar 11 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.5.0-3
- Enable introspection for py support
- add new files for introspection

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jan 06 2013 Ankur Sinha <ankursinha AT fedoraproject DOT org> 0.5.0-1
- Update to 0.5.0
- rhbz#890402

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May 02 2012 Rex Dieter <rdieter@fedoraproject.org> - 0.4.1-2
- rebuild (exiv2)

* Tue Apr 03 2012 Kalev Lember <kalevlember@gmail.com> - 0.4.1-1
- Update to 0.4.1

* Thu Feb 23 2012 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.3.91-1
- Update to 0.3.91
- rhbz #796278
- remove patches

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 14 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.2.2-3
- rebuild (exiv2)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sat Jan 01 2011 Rex Dieter <rdieter@fedoraproject.org> - 0.2.2-1
- 0.2.2
- exiv2-0.21 patch

* Tue Aug 24 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.2.0-1
- update to latest upstream release

* Sun Aug 08 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.90-1
- update to latest upstream release

* Tue Jul 13 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.1.0-1
- update to latest upstream release

* Mon Jun 14 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.91-2
- changed file section so package owns the directory containing headers too

* Fri Jun 11 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.91-1
- updated to latest release
- removed patch - it was included in this release

* Sat Jun 05 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.90-5
- changed configure macro as per bug report comment

* Sat Jun 05 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.90-4
- changed configure portion
- added Requires:  vala for devel
- made the file section more precise
- bugzilla #599097 
- changed patch to include a default LIB setting

* Fri Jun 04 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.90-3
- patched makefile

* Thu Jun 03 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.90-2
- some fixes in spec
- moved *.vapi to devel
- removed INSTALL from doc
- added comment to yorba ticket link
- corrected typo in description

* Wed Jun 02 2010 Ankur Sinha <ankursinha AT fedoraproject DOT org> - 0.0.90-1
- initial rpmbuild
