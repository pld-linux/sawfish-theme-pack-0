%define		_nm	sawfish-theme
Summary:	A "pack" of themes for Sawfish - starting with char [0-9]
Summary(pl.UTF-8):   Zestaw motywów dla Sawfish'a - zaczynających się od [0-9]
Name:		sawfish-theme-pack-0
Version:	1
Release:	2
License:	GPL
Group:		Themes
Source0:	http://download.freshmeat.net/themes/1_0/1_0-0.30.tar.gz
# Source0-md5:	b94f237810c1415691265bfea229c81f
Source1:	http://download.freshmeat.net/themes/7of9/7of9-0.52.0.tar.gz
# Source1-md5:	54a4984869c09acc3828db479a0eb6bb
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A pack of themes for Sawfish: 1_0-0.30 7of9-0.28

%description -l pl.UTF-8
Paczka z następującymi motywami dla Sawfisha:
- 1_0-0.30,
- 7of9-0.28.

%package -n %{_nm}-1_0
Summary:	Sawfish's theme "One Oh"
Summary(pl.UTF-8):   Motyw do sawfisha "One Oh"
Group:		Themes
Requires:	sawfish

%description -n %{_nm}-1_0
Pronounced "One Oh", this is a theme I made to go with a background I
made.. Zinx Verituse <zinx@microsoftisevil.com>

%description -n %{_nm}-1_0 -l pl.UTF-8
Motyw "One Oh" autorstwa Zinx Verituse <zinx@microsoftisevil.com>

%package -n %{_nm}-7of9
Summary:	based on the 7of9 WindowMaker theme
Summary(pl.UTF-8):   Bazowany na motywie 7of9 z WindowMakera
Group:		Themes
Requires:	sawfish

%description -n %{_nm}-7of9
This is based on the 7of9 WindowMaker theme, it was ported at a
friend's request. The lisp is based on the blue-heart theme by John
Harper. The theme resembles WindowMaker rather nicely, and goes best
with the included background. Ported by Dean <dean@thestuff.net>
Original WM theme by Ken <kingofstring@comports.com>.

%description -n %{_nm}-7of9 -l pl.UTF-8
Motyw bazowany na motywie 7og9 z WindowMakera. Przeportowany przez
Dean <dean@thestuff.net>. Autorem motywu do WindowMakera jest Ken
<kingofstring@comports.com>.

%prep
%setup -q -c -b 0 -b 1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/sawfish/themes/

mv -f {1_0,7of9} $RPM_BUILD_ROOT%{_datadir}/sawfish/themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{_nm}-1_0
%defattr(644,root,root,755)
%{_datadir}/sawfish/themes/1_0/

%files -n %{_nm}-7of9
%defattr(644,root,root,755)
%{_datadir}/sawfish/themes/7of9
