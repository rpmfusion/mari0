Name:           mari0
Version:        1.6.2
Release:        11%{?dist}
Summary:        A recreation of the original Super Mario Bros with a portal gun

License:        CC-BY-NC-SA
URL:            http://stabyourself.net/mari0/
Source0:        https://github.com/Stabyourself/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
#Source1 is just a Desktop file:
Source1:        %{name}.desktop

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
zip -r %{name}.love .
#Execution Script:
echo -e "#!/bin/sh\nlove %{_datadir}/%{name}/%{name}.love\n" > %{name}

%install
install -p -D -m 0644 %{name}.love %{buildroot}/%{_datadir}/%{name}/%{name}.love
install -p -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}
#Install desktop, icons:
desktop-file-install \
  --dir %{buildroot}%{_datadir}/applications \
  %{SOURCE1}
install -p -D -m 0644 graphics/icon.png %{buildroot}/%{_datadir}/pixmaps/%{name}.png

%files
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}.love
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%changelog
* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.6.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Sat Aug 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.6.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.6.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.6.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.6.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.6.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Sep 09 2019 Leigh Scott <leigh123linux@googlemail.com> - 1.6.2-1
- Update to 1.6.2 release (rfbz#5178)

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.6.1-4
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

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
