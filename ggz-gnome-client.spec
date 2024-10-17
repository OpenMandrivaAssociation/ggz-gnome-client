%define libggz_version %{version}
%define ggz_client_libs_version %{version}

Name:		ggz-gnome-client
Summary:	GGZ Client for Gnome Desktop
Version:	0.0.14.1
Release:	8
License:	GPL
Group:		Games/Other
URL:		https://ggzgamingzone.org/
Source:		http://download.sf.net/ggz/%{name}-%{version}.tar.bz2
BuildRequires:	libggz-devel = %{libggz_version}
BuildRequires:	ggz-client-libs-devel = %{ggz_client_libs_version}
BuildRequires:	desktop-file-utils 
BuildRequires:	pkgconfig(libgnome-2.0)
BuildRequires:	pkgconfig(gconf-2.0)
BuildRequires:	pkgconfig(libgnomeui-2.0)
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
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%preun
%preun_uninstall_gconf_schemas ggz-gnome

%files
%doc AUTHORS COPYING ChangeLog INSTALL NEWS README README.GGZ
%{_sysconfdir}/gconf/schemas/ggz-gnome.schemas
%{_gamesbindir}/ggz-gnome
%{_gamesbindir}/motd_editor
%{_datadir}/applications/*
%{_datadir}/ggz/ggz-gnome/*
%{_datadir}/locale/*
%{_mandir}/man?/*

