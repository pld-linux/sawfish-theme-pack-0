Summary:	A "pack" of themes for Sawfish - starting with char [0-9]
Summary(pl):	Zestaw tematów dla Sawfish'a - zaczynaj±cych siê od [0-9]
Name:		sawfish-theme-pack-0
Version:	1
Release:	1
License:	GPL
Group:		Themes
Source0:	http://debian.attica.net.nz/themes.org/sawmill/1_0-0.30.tar.gz
Source2:	http://debian.attica.net.nz/themes.org/sawmill/7of9-0.28.tar.gz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6/share

%description
A pack of themes for Sawfish: 1_0-0.30 7of9-0.19 7of9-0.28

%description -l pl
Paczka z nastêpuj±cymi tematami dla Sawfisha:
- 1_0-0.30,
- 7of9-0.19
- 7of9-0.28.

%package 1_0
Summary:	Sawfish's theme "One Oh"
Summary(pl):	Temat do sawfisha "One Oh"
Group:		Themes
Requires:	sawfish

%description 1_0
Pronounced "One Oh", this is a theme I made to go with a background I
made.. Zinx Verituse <zinx@microsoftisevil.com>

%package 7of9
Summary:	based on the 7of9 WindowMaker theme
Summary(pl):	Bazowany na temacie 7of9 z WindowMakera
Group:		Themes
Requires:	sawfish

%description 7of9
This is based on the 7of9 WindowMaker theme, it was ported at a
friend's request. The lisp is based on the blue-heart theme by John
Harper. The theme resembles WindowMaker rather nicely, and goes best
with the included background. Ported by Dean <dean@thestuff.net>
Original WM theme by Ken (kingofstring@comports.com)

%prep
%setup -c -b 0 -b 1 -b 2

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sawfish/themes

install 1_0 0.19 $RPM_BUILD_ROOT%{_datadir}/sawfish/themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)

%files 1_0
%defattr(644,root,root,755)
%{_datadir}/sawfish/themes/1_0/

%files 7of9
%defattr(644,root,root,755)
%{_datadir}/sawfish/themes/7of9
