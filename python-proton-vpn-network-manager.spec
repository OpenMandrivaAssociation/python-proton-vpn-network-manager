Name:		python-proton-vpn-network-manager
Version:	0.12.14
Release:	1
Source0:	https://github.com/ProtonVPN/python-proton-vpn-network-manager/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Summary:	Provides the necessary functionality for other components to interact with NetworkManager
URL:		https://github.com/ProtonVPN/python-proton-vpn-network-manager
License:	GPL-3.0
Group:		Development/Python

BuildRequires:	python
BuildRequires: python-gobject3
BuildRequires: networkmanager
BuildRequires: networkmanager-openvpn
BuildRequires: networkmanager-openvpn-gtk
BuildRequires: gobject-introspection
BuildRequires: python-setuptools
BuildRequires: python-proton-core
BuildRequires: python-proton-vpn-api-core >= 0.42.3
BuildRequires: python-proton-vpn-local-agent >= 1.4.4
BuildRequires: python-jinja2

Requires: python-gobject3
Requires: networkmanager
Requires: networkmanager-openvpn
Requires: networkmanager-openvpn-gtk
Requires: gobject-introspection
Requires: python-setuptools
Requires: python-proton-core
Requires: python-proton-vpn-api-core >= 0.42.3
Requires: python-proton-vpn-local-agent >= 1.4.4
Requires: python-jinja2
Requires: lib64networkmanager-gir1.0

BuildArch:	noarch

%description
The proton-vpn-network-manager component provides the necessary functionality for other components to interact with NetworkManager.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/proton
%{py_sitedir}/proton_vpn_network_manager-*.egg-info
