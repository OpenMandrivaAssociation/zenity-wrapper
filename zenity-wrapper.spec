Name: zenity-wrapper
Version: 1.0
Release: 3
Source0: zenity
Summary: Wrapper script that calls qarma or zenity, depending on desktop
URL: https://openmandriva.org/
License: GPL-3.0
Group: User Interface/Desktops
Requires: (zenity-gtk or qarma)
BuildArch: noarch

%description
Wrapper script that calls qarma or zenity, depending on desktop

%install
mkdir -p %{buildroot}%{_bindir}
install -c -m 755 %{S:0} %{buildroot}%{_bindir}/

%files
%{_bindir}/zenity
