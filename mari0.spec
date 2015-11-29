Name:           mari0
Version:        1.6
Release:        5%{?dist}
Summary:        A recreation of the original Super Mario Bros with a portal gun

License:        CC-BY-NC-SA
URL:            http://stabyourself.net/mari0/
#Source0 is the upstream source:
#Updated by hacktivista, see github for details:
#https://github.com/Hacktivista/mari0
#Download here:
#https://github.com/Hacktivista/mari0/archive/fc23e18525c4d0c881e64268e56fd23773f006af.zip
Source0:        %{name}-fc23e18525c4d0c881e64268e56fd23773f006af.zip
#Source1 is just a Desktop file:
Source1:        %{name}.desktop

#BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildArch:      noarch
Requires:       love >= 0.9.0

#Reworded from the website (see URL above)
%description
A complete from scratch recreation of the original Super Mario Bros.
game with a focus on perfectly imitating the feel the 1985 classic
gave us but with a portal gun and puzzle game mechanics from the
popular Value game, Portal. Mari0 also has a 4-player coop mode, with
everyone having their own Portal gun. This game is made with LOVE.

%prep
%setup -q -c -n %{name}-fc23e18525c4d0c881e64268e56fd23773f006af
#Execution Script:
echo -e "#!/bin/sh\nlove %{_datadir}/%{name}/%{name}.love\n" > %{name}

%build
#No Build Required
 
%install
install -p -D -m 0644 %{name}-fc23e18525c4d0c881e64268e56fd23773f006af/%{name}.love %{buildroot}/%{_datadir}/%{name}/%{name}.love
install -p -D -m 0755  %{name} %{buildroot}/%{_bindir}/%{name}
#Install desktop, icons:
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}
install -p -D -m 0644  "%{name}-fc23e18525c4d0c881e64268e56fd23773f006af/_DO NOT INCLUDE/icon.png" %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.love
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Nov 29 2015 Jeremy Newton <alexjnewt at hotmail dot com> - 1.6-5
- Update to work with love 0.9+

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 17 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 1.6-3
- Removed unnecessary unzip Build Require
- Simplified source files
- Fixed up desktop file
- Fixed inconsistent macros

* Mon Jun 4 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 1.6-2
- Added missing Build Require
- Removed unnecessary scriptlets

* Tue Apr 17 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 1.6-1
- Updated to 1.6
- Added a launcher and various improvements

* Tue Mar 6 2012 Jeremy Newton <alexjnewt at hotmail dot com> - 1.2-1
- Initial Package
