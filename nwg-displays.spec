Name:           nwg-displays
Version:        0.3.26
Release:        1
Summary:        Output management utility for sway and Hyprland. 
License:        MIT
URL:            https://github.com/nwg-piotr/nwg-displays
Source0:        %{url}/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  pkgconfig(gtk-layer-shell-0)
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(python3)
BuildRequires:  python-setuptools
Requires:       %{_lib}gtk3_0
Requires:       %{_lib}gtk-layer-shell0
Requires:       python3-gobject
Requires:       python3-i3ipc
Requires:       typelib(GtkLayerShell)
BuildArch:      noarch

%description

Nwg-displays is an output management utility for sway and Hyprland Wayland compositor, inspired by wdisplays and wlay. 
The program is expected to:
  - provide an intuitive GUI to manage multiple displays;
  - apply settings;
  - save outputs configuration to a text file;
  - save workspace -> output assignments to a text file;
  - support sway and Hyprland only.

%prep
%autosetup -p1

%build
%py_build

%install
%py_install

install -Dpm 0644 %{name}.svg -t %{buildroot}%{_datadir}/pixmaps/
install -Dpm 0644 nwg-displays.svg -t %{buildroot}%{_datadir}/pixmaps/
install -Dpm 0755 %{name}.desktop -t %{buildroot}%{_datadir}/applications/

# fix env-script-interpreter
sed -i '1s|#!/usr/bin/env python|#!/usr/bin/python3|' \
   %{buildroot}%{python_sitelib}/nwg_displays/main.py

# fix non-executable-script
for file in %{buildroot}%{python_sitelib}/nwg_displays/main.py; do
   chmod a+x $file
done

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.svg
%{python_sitelib}/nwg_displays
%{python_sitelib}/nwg_displays-*.egg-info
