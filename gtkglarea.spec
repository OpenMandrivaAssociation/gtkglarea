%define name gtkglarea
%define version 1.2.3
%define release %mkrel 11

%define major 5
%define libname %mklibname %{name} %major
%define develname %mklibname %{name} -d


Summary:	OpenGL widget for GTK+ 1.2
Name:		%{name}
Version:	%{version}
Release: 	%{release}
License:	LGPL
Group:		System/Libraries

Source0:	%{name}-%{version}.tar.bz2
Patch0:		gtkglarea-1.2.3-fix-underquoted-calls.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.student.oulu.fi/~jlof/gtkglarea/
BuildRequires:	mesaglu-devel
BuildRequires:	gtk+-devel

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is very similar
to GtkDrawingArea widget and adds only three extra functions.

Lower level gdkgl functions make it easy to render on any widget that has
OpenGL capable visual, rendering to off-screen pixmaps is also supported.

%package -n	%{libname}
Summary:        OpenGL widget for GTK+ GUI toolkit
Group:          System/Libraries
Provides:	%{name}
Obsoletes:	%{name} = %{version}-%{release}

%description -n	%{libname}
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is very similar
to GtkDrawinigArea widget and adds only three extra functions.

Lower level gdkgl functions make it easy to render on any widget that has
OpenGL capable visual, rendering to off-screen pixmaps is also supported.

%package -n	%{develname}
Summary:	Development libraries for GtkGLArea
Group:		Development/GNOME and GTK+
Requires:	%{libname} >= %{version}
Provides:	%{name}-devel = %{version}-%{release} 
Provides:	lib%{name}-devel
Obsoletes:	%{mklibname gtkglarea 5 -d}

%description -n	%{develname}
Libraries and includes files you can use for GtkGLArea development.

%prep
%setup -q
%patch0 -p1 -b .underquoted

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/lib*.so.%{major}*

%files -n %{develname}
%defattr(-, root, root)
%doc docs/*.txt
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*
%{_datadir}/aclocal/*
