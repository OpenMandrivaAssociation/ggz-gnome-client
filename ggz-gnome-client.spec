%define libggz_version %{version}
%define ggz_client_libs_version %{version}

Name:		ggz-gnome-client
Summary:	GGZ Client for Gnome Desktop
Version:	0.0.14.1
Release:	7
License:	GPL
Group:		Games/Other
URL:		http://ggzgamingzone.org/
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
export LDFLAGS="-lX11"
%configure2_5x \
	--bindir=%{_gamesbindir} \
	--datadir="\${prefix}/share" \
	--with-libggz-libraries=%{_libdir} \
	--with-ggzcore-libraries=%{_libdir} \
	--with-ggzmod-libraries=%{_libdir}

%make

%install
%makeinstall_std

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --remove-key="Encoding" \
  --add-category="GTK" \
  --add-category="Game" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

%preun
%preun_uninstall_gconf_schemas ggz-gnome

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README README.GGZ
%{_sysconfdir}/gconf/schemas/ggz-gnome.schemas
%{_gamesbindir}/ggz-gnome
%{_gamesbindir}/motd_editor
%{_datadir}/applications/*
%{_datadir}/ggz/ggz-gnome/*
%{_datadir}/locale/*
%{_mandir}/man?/*




%changelog
* Mon May 23 2011 Funda Wang <fwang@mandriva.org> 0.0.14.1-6mdv2011.0
+ Revision: 677703
- rebuild to add gconftool as req

* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.0.14.1-5mdv2011.0
+ Revision: 618452
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.0.14.1-4mdv2010.0
+ Revision: 429198
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.0.14.1-3mdv2009.0
+ Revision: 245996
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Tue Feb 26 2008 Emmanuel Andry <eandry@mandriva.org> 0.0.14.1-1mdv2008.1
+ Revision: 175549
- New version

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 16 2007 Emmanuel Andry <eandry@mandriva.org> 0.0.14-2mdv2008.0
+ Revision: 88668
- drop old menu


* Sat Feb 10 2007 Emmanuel Andry <eandry@mandriva.org> 0.0.14-1mdv2007.0
+ Revision: 118768
- Buildrequires libgnomeui2-devel
- Import ggz-gnome-client

