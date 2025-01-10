%undefine _debugsource_packages

Name:           cosmic-osd
Version:        1.0.0
Release:        0.alpha5.0
Summary:        COSMIC OSD
License:        GPL-3.0-only
Group:          Desktop/COSMIC
URL:            https://github.com/pop-os/cosmic-osd
Source0:        https://github.com/pop-os/cosmic-osd/archive/epoch-%{version}-alpha.5/%{name}-epoch-%{version}-alpha.5.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

BuildRequires:  rust-packaging
BuildRequires:  make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}-alpha.5 -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
# By default cosmic-osd set polkit to /usr/libexec/polkit-agent-helper-1, lets force it to Mandriva dir
# https://github.com/pop-os/cosmic-epoch/issues/1065
%make_build polkit-agent-helper-1=/usr/lib/polkit-1/polkit-agent-helper-1

%install
%make_install DESTDIR=%{buildroot} prefix=%{_prefix}

%files
%license LICENSE
%{_bindir}/%{name}
