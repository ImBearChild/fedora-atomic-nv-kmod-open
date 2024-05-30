Name:           fedora-atomic-nv-kmod-open-macros
Version:        0.0.1
Release:        1%{?dist}
Summary:        RPM macro for install Nvidia kernel-open driver from rpm-fusion

License:        MIT
URL:            https://rpmfusion.org/Howto/NVIDIA

BuildArch:      noarch

Supplements:    akmods


%description
Akmods ostree keys for signing modules.

%prep
%setup -q -c -T


%build
echo "%_with_kmod_nvidia_open 1" > macros.nvidia-kmod


%install
install -p -m 644 -t %{buildroot}%{_rpmconfigdir}/macros.d macros.nvidia-kmod

%pre

%post

%preun

%postun

%files
%{_rpmconfigdir}/macros.d/macros.nvidia-kmod

%changelog
* Thu May 30 2024 Nianqing Yao <imbearchild@outlook.com> - 0.0.1
- First Version
