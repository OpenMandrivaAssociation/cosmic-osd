%undefine _debugsource_packages

Name:           cosmic-osd
Version:        1.0.0
%define beta alpha.6
Release:        %{?beta:0.%{beta}.}1
Summary:        COSMIC OSD
License:        GPL-3.0-only
Group:          Desktop/COSMIC
URL:            https://github.com/pop-os/cosmic-osd
Source0:        https://github.com/pop-os/cosmic-osd/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
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
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -a1 -p1
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
