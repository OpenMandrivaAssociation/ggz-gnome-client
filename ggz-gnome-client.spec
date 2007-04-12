%define name	ggz-gnome-client
%define version 0.0.14
%define release %mkrel 1

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

# http://download.sf.net/ggz/
Source:		%{name}-%{version}.tar.bz2

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

# menu entry
install -d -m 0755 %{buildroot}%{_menudir}
cat > %{buildroot}%{_menudir}/%{name} <<_EOF_
?package(%{name}): \
 command="%{_gamesbindir}/ggz-gnome" \
 icon="other_amusement.png" \
 longtitle="GGZ Gaming Zone game client for Gnome Desktop" \
 needs="x11" \
 section="More Applications/Games/Other" \
 title="GGZ Gnome Game Client" \
 xdg="true"
_EOF_

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-key="Encoding" \
  --add-category="GTK" \
  --add-category="X-MandrivaLinux-MoreApplications-Games-Other;Game" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%find_lang ggz-gnome

%post
%update_menus
%post_install_gconf_schemas ggz-gnome

%preun
%preun_uninstall_gconf_schemas ggz-gnome

%postun
%clean_menus

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
%{_menudir}/%{name}



