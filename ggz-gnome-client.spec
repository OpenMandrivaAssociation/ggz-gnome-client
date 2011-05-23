%define name	ggz-gnome-client
%define version 0.0.14.1
%define release %mkrel 6

%define libggz_version %{version}

%define ggz_client_libs_version %{version}

Name:		%{name}
Summary:	GGZ Client for Gnome Desktop
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Games/Other
URL:		http://ggzgamingzone.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source:		http://download.sf.net/ggz/%{name}-%{version}.tar.bz2
BuildRequires:	libggz-devel = %{libggz_version}
BuildRequires:	ggz-client-libs-devel = %{ggz_client_libs_version}
BuildRequires:	desktop-file-utils libgnome2-devel libGConf2-devel libgnomeui2-devel
Requires:	libggz = %{libggz_version}
Requires:	ggz-client-libs = %{ggz_client_libs_version}
Requires:	ggz-game-modules = %{version}

%description
The official GGZ Gaming Zone client for Gnome Desktop.

%prep
%setup -q

%build
%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir="\${prefix}/share" \
	--with-libggz-libraries=%{_libdir} \
	--with-ggzcore-libraries=%{_libdir} \
	--with-ggzmod-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-key="Encoding" \
  --add-category="GTK" \
  --add-category="Game" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang ggz-gnome

%if %mdkversion < 200900
%post
%update_menus
%post_install_gconf_schemas ggz-gnome
%endif

%preun
%preun_uninstall_gconf_schemas ggz-gnome

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf %{buildroot}

%files -f ggz-gnome.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README README.GGZ
%{_sysconfdir}/gconf/schemas/ggz-gnome.schemas
%{_gamesbindir}/ggz-gnome
%{_gamesbindir}/motd_editor
%{_datadir}/applications/*
%{_datadir}/ggz/ggz-gnome/*
%{_datadir}/locale/*
%{_mandir}/man?/*


