%global goipath  github.com/kevinburke/ssh_config
%global tag 0.4
Version: %{tag}

%global common_description %{expand:
Package ssh_config provides tools for manipulating SSH config files.

Importantly, this parser attempts to preserve comments in a given file, so you
can manipulate a `ssh_config` file from a program, if your heart desires.

The Get() and GetStrict() functions will attempt to read values from
$HOME/.ssh/config, falling back to /etc/ssh/ssh_config. The first argument is
the host name to match on ("example.com"), and the second argument is the key
you want to retrieve ("Port"). The keywords are case insensitive.}

%gometa

Name: %{goname}
Release: 2%{?dist}
Summary: Go parser for ssh_config files
License: MIT
URL: %{gourl}
Source0: %{gosource}
BuildRequires: golang(github.com/pelletier/go-buffruneio)

%description
%{common_description}

%package devel
Summary: %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q

%install
%goinstall

%check
%gochecks

%files devel -f devel.file-list
%license LICENSE
%doc AUTHORS.txt README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Apr 02 2018 Dominik Mierzejewski <dominik@greysector.net> - 0.4-1
- First package for Fedora
