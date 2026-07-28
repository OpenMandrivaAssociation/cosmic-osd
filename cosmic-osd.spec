%undefine _debugsource_packages

Name:           cosmic-osd
Version:        1.4.0
#define beta beta.7
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
BuildRequires:  just
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libinput)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libpipewire-0.3)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

# By default cosmic-osd set polkit to /usr/libexec/polkit-agent-helper-1, lets force it to Mandriva dir
# https://github.com/pop-os/cosmic-epoch/issues/1065
#make_build polkit-agent-helper-1=/usr/lib/polkit-1/polkit-agent-helper-1

%build
# as of cosmic 1.4.0, rust 1.97.1 and llvm 23.1.0-rc1.
# Disable LTO because error rustc-LLVM ERROR: expected function definition _RNvCslvstGAdgBpu_7___rustc12___rust_alloc to have an associated value info.
export RUSTFLAGS="-C lto=off"
just polkit-agent-helper-1=/usr/lib/polkit-1/polkit-agent-helper-1 build-release --offline --frozen

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%{_bindir}/%{name}
