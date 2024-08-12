Name: zenity-wrapper
Version: 1.0
Release: 1
Source0: zenity
Summary: Wrapper script that calls qarma or zenity, depending on desktop
URL: https://openmandriva.org/
License: GPL-3.0
Group: User interface/Desktops
Requires: (qarma or zenity-gtk)

%description
Wrapper script that calls qarma or zenity, depending on desktop

%install
mkdir -p %{buildroot}%{_bindir}
cp %{S:0} %{buildroot}%{_bindir}/

%files
%{_bindir}/zenity
