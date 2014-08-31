Name:           mari0
Version:        1.6
Release:        4%{?dist}
Summary:        A recreation of the original Super Mario Bros with a portal gun

License:        CC-BY-NC-SA
URL:            http://stabyourself.net/mari0/
#Source0 is the upstream source:
Source0:        http://stabyourself.net/dl.php?file=%{name}-1006/%{name}-source.zip
#Source1 is just a Desktop file:
Source1:        %{name}.desktop

BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
BuildArch:      noarch
Requires:       love >= 0.8.0

#Reworded from the website (see URL above)
%description
A complete from scratch recreation of the original Super Mario Bros.
game with a focus on perfectly imitating the feel the 1985 classic
gave us but with a portal gun and puzzle game mechanics from the
popular Value game, Portal. Mari0 also has a 4-player coop mode, with
everyone having their own Portal gun. This game is made with LOVE.

%prep
%setup -q -c
sed -i 's/\r//' readme.txt
iconv -f iso8859-1 -t utf-8 readme.txt > readme.txt.conv && mv -f readme.txt.conv readme.txt
#Execution Script:
echo -e "#!/bin/sh\nlove %{_datadir}/%{name}/%{name}.love\n" > %{name}
unzip -p %{name}_%{version}.love graphics/SMB/title.png | convert - -crop 176x88+0+0 -gravity NorthWest %{name}.png

%build
#No Build Required
 
%install
install -p -D -m 0644 %{name}_%{version}.love %{buildroot}/%{_datadir}/%{name}/%{name}.love
install -p -D -m 0755  %{name} %{buildroot}/%{_bindir}/%{name}
#Install desktop, icons:
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}
install -p -D -m 0644  %{name}.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%doc readme.txt
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.love
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 1.6-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Aug 17 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.6-3
- Removed unnecessary unzip Build Require
- Simplified source files
- Fixed up desktop file
- Fixed inconsistent macros

* Mon Jun 4 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.6-2
- Added missing Build Require
- Removed unnecessary scriptlets

* Tue Apr 17 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.6-1
- Updated to 1.6
- Added a launcher and various improvements

* Tue Mar 6 2012 Jeremy Newton <alexjnewt@hotmail.com> - 1.2-1
- Initial Package
