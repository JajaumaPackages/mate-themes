# Conditional for release and snapshot builds. Uncomment for release-builds.
%global rel_build 1

# This is needed, because src-url contains branched part of versioning-scheme.
%global branch 3.14

%global rel_ver 3.14.4

# Settings used for build from snapshots.
%{!?rel_build:%global commit 59b3286ac467f19e9bce39783e71836ced239b7b}
%{!?rel_build:%global commit_date 20160526}
%{!?rel_build:%global shortcommit %(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global git_ver git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global git_rel .git%{commit_date}.%{shortcommit}}
%{!?rel_build:%global git_tar %{name}-%{version}-%{git_ver}.tar.xz}

Name:           mate-themes
Version:        %{rel_ver}
%if 0%{?rel_build}
Release:        1%{?dist}
%else
Release:        0.1%{?git_rel}%{?dist}
%endif
Summary:        MATE Desktop themes
License:        GPLv2+
URL:            http://mate-desktop.org
BuildArch:      noarch

# for downloading the tarball use 'spectool -g -R mate-themes.spec'
# Source for release-builds.
%{?rel_build:Source0:     http://pub.mate-desktop.org/releases/themes/%{branch}/%{name}-%{version}.tar.xz}
# Source for snapshot-builds.
%{!?rel_build:Source0:    http://git.mate-desktop.org/%{name}/snapshot/%{name}-%{commit}.tar.xz#/%{git_tar}}

BuildRequires:  mate-common
BuildRequires:  gtk2-devel
BuildRequires:  gdk-pixbuf2-devel

Requires:       mate-icon-theme
Requires:       gtk2-engines
Requires:       gtk-murrine-engine

%description
MATE Desktop themes

%prep
%if 0%{?rel_build}
# for releases
%setup -qn %{name}-%{version}
%else # 0%{?rel_build}
# for snapshots
%setup -qn %{name}-%{commit}
# needed for git snapshots
NOCONFIGURE=1 ./autogen.sh
%endif # 0%{?rel_build}

%build
%configure --enable-icon-mapping

make %{?_smp_mflags} V=1

%install
%{make_install}

find %{buildroot} -name '*.la' -exec rm -rf {} ';'
find %{buildroot} -name '*.a' -exec rm -rf {} ';'

%post
for icon_theme in \
  ContrastHigh ;
do
  /bin/touch --no-create %{_datadir}/icons/${icon_theme} &> /dev/null || :
done

%postun
if [ $1 -eq 0 ]; then
for icon_theme in \
  ContrastHigh ;
do
  /bin/touch --no-create %{_datadir}/icons/${icon_theme} &> /dev/null || :
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/${icon_theme} &> /dev/null || :
done
fi

%posttrans
for icon_theme in \
  ContrastHigh ;
do
  /usr/bin/gtk-update-icon-cache %{_datadir}/icons/${icon_theme} &> /dev/null || :
done


%files
%doc AUTHORS COPYING README ChangeLog
%{_datadir}/themes/BlackMATE/
%{_datadir}/themes/BlueMenta/
%{_datadir}/themes/Blue-Submarine/
%{_datadir}/themes/ContrastHigh/
%{_datadir}/themes/ContrastHighInverse/
%{_datadir}/themes/GreenLaguna/
%{_datadir}/themes/Green-Submarine/
%{_datadir}/themes/HighContrast/metacity-1/metacity-theme-1.xml
%{_datadir}/themes/Menta/
%{_datadir}/themes/TraditionalOk/
%{_datadir}/themes/TraditionalOkTest/
%{_datadir}/themes/TraditionalGreen/
%{_datadir}/themes/Shiny/
%{_datadir}/icons/ContrastHigh/
%{_datadir}/icons/mate/cursors/


%changelog
* Tue Nov 08 2016 Jajauma's Packages <jajauma@yandex.ru> - 3.14.4-1
- Downgrade source to 3.14.4 for el7

* Wed Oct 26 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.22.4-1
- update to 3.23.4 release

* Mon Sep 26 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.22.3-1
- update to 3.23.3 release

* Sat Sep 03 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.22.2-1
- update to 3.22.2 release

* Mon Jul 25 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.22.1-2
- fix tabs in mate-terminal

* Fri Jul 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.22.1-1
- update 3.22.1 release

* Sat Jul 02 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.22.0-1
- update 3.22.0 release

* Mon Jun 13 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.20.8-3
- increase border size of Menta themes

* Mon Jun 13 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.20.8-2
- adjust buttons in metacity theme of menta themes

* Mon Jun 06 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.20.8-1
- update to 3.20.8 release

* Fri May 27 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.20.8-0.1.git20160526.59b328
- update to git snapshot from 2016-05-26

* Mon May 16 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.20.7-1
- update to 3.20.7 release

* Wed May 04 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.20.6-1
- update to 3.20.6 release

* Tue Apr 12 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.20.5-2
- fix text selection in firefox

* Sun Apr 10 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.20.5-1
- update to 3.20.5 release
- drop ContrastHighInverse theme already shiped with gtk+
- update for latest gtk+ breakages

* Sat Mar 26 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.20.4-1
- update to release 3.20.4
- fix latest breakages from gtk+-3.20.1
- don't build Greenlaguna theme for the moment

* Fri Mar 11 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.20.3-1
- update to release 3.20.3
- fix latest breakage with gtk+-3.19.11
- do not build language files, translations are already in theme files

* Thu Mar 03 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.20.2-1
- release 3.20.2

* Mon Feb 22 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.20.1-1
- release 3.20.1

* Thu Feb 04 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 3.20.0-1
- release 3.20.0 for gtk+-3.20

* Sat Jan 02 2016 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.2-1
- update to 1.12.2 release

* Fri Dec 04 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.1-1
- update to 1.12.1 release

* Fri Nov 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.12.0-1
- update to 1.12.0 release

* Mon Oct 26 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.11.1-1
- update to 1.11.1 release

* Mon Oct 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.6-0.2.git20151005.5fec168
- update to git snapshot from 2015-10-05

* Tue Sep 15 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.5-1
- update to 1.10.5 release

* Fri Sep 04 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.5-0.3.git20150904.5c8d94c
- update to git snapshot from 2015-09-04

* Thu Sep 03 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.5-0.2.git20150903.6b53375
- fix crash of mate-dictionary
- https://github.com/mate-desktop/mate-utils/issues/121

* Thu Aug 20 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.4-1
- update to 1.10.4 release

* Wed Jul 29 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.3-1
- update to 1.10.3 release

* Wed Jul 08 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.2-1
- update to 1.10.2 release
- build submarine themes

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Jun 10 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-1
- update to 1.10.1 release

* Mon Jun 01 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-0.4.git20150531.94e1587
- update to latest git snapshot from 2015-05-31
- add missing image for gtk3 panel

* Sat May 30 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-0.3.git20150530.a0a9b98
- update to latest git snapshot from 2015-05-30

* Wed May 06 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.1-0.2.git20150506.d80f9d7
- update to git snapshot from 2015-05-06

* Tue May 05 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-1
- update to 1.10.0 release

* Sun Apr 19 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-0.6.git20150427.edb9158
- update to git snapshot from 2015-04-27
- remove require gtk-unico-engine
- add shiny metacity theme

* Sun Apr 19 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-0.5.git20150419.ee505bb
- update to git snapshot from 2015-04-19

* Sun Mar 22 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-0.4.git20150320.488e77b
- bump version to avoid upgrade path issue

* Fri Mar 20 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-0.2.git20150320.488e77b
- update to git snapshot from 2015-03-01
- drop Shiny theme

* Mon Mar 02 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.10.0-0.1.git20150301.81f6939
- update to git snapshot from 2015-03-01

* Sat Jan 10 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.3-2
- bump version to fix f20 upgrade path

* Sat Jan 10 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.3-1
- update to 1.9.3 release
- TraditionalOKTest is installable with normal configure flags
- add transition effect to buttons and menuitems for Menta themes GTK3
- add transition effect to buttons and menuitems for BlackMate and GreenLaguna GTK3
- add support for CSD applications in BlackMate and GreenLaguna
- improve handling of CSD applications in other themes
- add support for popovers in GreenLaguna, BlackMate, ContrastHigh and ContrastHighInverse themes
- improve popovers support in Traditional themes
- serveral other improvements

* Sun Jan 04 2015 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.3-0.4.git20141226.962f516
- bump version to fix upgrade path

* Wed Dec 31 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.3-0.1.git20141226.962f516
- update to latest git snapshot from 2014.12.26

* Thu Nov 20 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.2-1
- update to 1.9.2 release

* Tue Nov 18 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.2-0.2.git20140304.5a900e
- bump version to fix upgrade path issue with f20

* Wed Nov 05 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.2-0.1.git20140304.5a900e
- update to latest git snapshot from 2014-11-08

* Tue Oct 21 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-2
- remove all themes which doesn't support GTK3

* Tue Oct 21 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-1
- update to 1.9.1 release for GTK3-3.14
- add gtk-unico-engine runtime require for shiny theme

* Wed Sep 24 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-0.2.git20140914.503ae60
- update to latest git snapshot from 2014-09-14

* Thu Sep 11 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.1-0.1.git20140720.d832073
- update to latest git snapshot
- fix GTK3 issues rhbz (#1140423, #1136994)
- remove adwaita theme runtime requires

* Sun Sep 07 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-3
- add missing icons to ContrastHigh theme

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Jun 01 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.9.0-1
- all major themes has now GTK+-3.12 support
- don't build with all themes
- remove obsolete themes

* Fri May 16 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.1-1
- update to 1.8.1 release

* Wed Mar 05 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.8.1-0.1.git20140304.5a900e
- update to git snapshot from 2014.03.04
- add better git snapshot usage
- BlackMATE, GreenLaguna, Menta and BlueMenta supports now GTk3-3.10
- Good bye adwaita engine warning

* Wed Mar 05 2014 Dan Mashal <dan.mashal@fedoraproject.org> - 1.8.0-1
- Update to 1.8.0

* Wed Feb 19 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.90-1
- update to 1.7.90

* Sat Jan 18 2014 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.2-1
- update to 1.7.2
- use modern 'make install' macro
- add --with-gnome --all-name for find language

* Sun Nov 24 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.2-0.2.git27da094
- update to latest git snapshot
- rename Menta-Blue to BlueMenta
- update BlackMATE to GTK3-3.8

* Thu Nov 14 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.2-0.1.git8a12f75
- update to latest snapshot
- new theme Menta-Blue
- syncronize view of panel menus

* Sat Oct 26 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.7.1-1
- update to 1.7.1 release for fedora > f19
- Menta theme is updated to GTK3-3.10

* Thu Aug 15 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.2-0.2.git3fc43dd
- update GreenLaguna theme to GTK3-8

* Sun Aug 04 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.2-0.1.git15baae1
- fix usage of cursor theme slider
- fix panel-applets menu selected bg by BlackMATE theme

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Mon Jun 17 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-2
- fix GTK3 GreenLaguna menu background
- add runtime require adwaita-gtk3-theme

* Fri Jun 07 2013 Wolfgang Ulbrich <chat-to-me@raveit.de> - 1.6.1-1
- Update to latest 1.6.1 stable release
- removal of aldabra theme, fix #907565

* Wed Apr 03 2013 Dan Mashal <dan.mashal@fedoraproject.org> - 1.6.0-1
- Update to latest 1.6.0 stable release.

* Tue Mar 26 2013 Dan Mashal <dan.mashal@fedoraproject.org> 1.5.1-1
- Update to latest upstream release

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 08 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.5.0-1
- update to 1.5.0 release

* Sat Oct 20 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-7
- add requires gtk2-engines and mate-icon-theme 

* Tue Oct 16 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-6
- fix mistake in scriptlets from last commit

* Tue Oct 16 2012 Leigh Scott <leigh123linux@googlemail.com> - 1.4.0-5
- Fix scriplets
- add requires gtk-murrine-engine

* Sun Oct 14 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-4
- Update BR and add test themes

* Wed Oct 03 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-3
- Fix missing icon scriptlets

* Sun Sep 30 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-2
- Update br and post scriptlets as per package review

* Tue Sep 25 2012 Dan Mashal <dan.mashal@fedoraproject.org> 1.4.0-1
- Initial build
