Name:           mari0
Version:        1.6.1
Release:        1%{?dist}
Summary:        A recreation of the original Super Mario Bros with a portal gun

License:        CC-BY-NC-SA
URL:            http://stabyourself.net/mari0/
Source0:        https://github.com/Stabyourself/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
#Source1 is just a Desktop file:
Source1:        %{name}.desktop
Patch0:         https://github.com/Stabyourself/mari0/commit/9c2d30a4d7e838135c8cb687dbb59d002626450f.patch#/runtime_fix.patch

BuildArch:      noarch

#BuildRequires:  ImageMagick
BuildRequires:  desktop-file-utils
Requires:       love >= 0.10.1

#Reworded from the website (see URL above)
%description
A complete from scratch recreation of the original Super Mario Bros.
game with a focus on perfectly imitating the feel the 1985 classic
gave us but with a portal gun and puzzle game mechanics from the
popular Value game, Portal. Mari0 also has a 4-player coop mode, with
everyone having their own Portal gun. This game is made with LOVE.

%prep
%autosetup -p1

%build
zip -r %{name}.love . -x "_DO NOT INCLUDE"
#Execution Script:
echo -e "#!/bin/sh\nlove %{_datadir}/%{name}/%{name}.love\n" > %{name}

%install
install -p -D -m 0644 %{name}.love %{buildroot}/%{_datadir}/%{name}/%{name}.love
install -p -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
#Install desktop, icons:
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}
install -p -D -m 0644  "_DO NOT INCLUDE/icon.png" %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.love
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Feb 01 2018 Leigh Scott <leigh123linux@googlemail.com> - 1.6.1-1
- Update to 1.6.1 release
- Fix runtime issue (rfbz#4667)
- Fix broken release tag, previous build was git but didn't have git prefix

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.6-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 1.6-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Oct 26 2016 Jeremy Newton <alexjnewt at hotmail dot com> - 1.6-6
- Update to git version (fixes issue with love 0.10.*)

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
