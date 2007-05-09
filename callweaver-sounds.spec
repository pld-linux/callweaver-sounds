Summary:	Additional sound files for CallWeaver PBX
Summary(pl.UTF-8):	Dodatkowe pliki dźwiękowe do centralki CallWeaver
Name:		callweaver-sounds
Version:	0.1
Release:	1
License:	undecided
Group:		Applications/System
Source0:	http://devs.callweaver.org/sounds/%{name}.tgz
# Source0-md5:	5678d7e5b0c2fdfb1732a0852bc76141
URL:		http://www.callweaver.org/
BuildRequires:	sox
Requires:	callweaver
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Additional sound files for CallWeaver PBX.

%description -l pl.UTF-8
Dodatkowe pliki dźwiękowe do centralki PBX CallWeaver.

%prep
%setup -q -n %{name}

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/callweaver/sounds/en_US/MelanieTaylor

find . -name '*.gsm' -exec install -D "{}" "$RPM_BUILD_ROOT%{_datadir}/callweaver/{}" ";"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/callweaver/sounds
