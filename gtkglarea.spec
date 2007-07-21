%define name gtkglarea
%define version 1.2.3
%define release %mkrel 9

%define major 5
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d


Summary:	GtkGLArea is an OpenGL widget for GTK+ GUI toolkit
Name:		%{name}
Version:	%{version}
Release: 	%{release}
License:	LGPL
Group:		System/Libraries

Source0:	%{name}-%{version}.tar.bz2
Patch0:		gtkglarea-1.2.3-fix-underquoted-calls.patch.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.student.oulu.fi/~jlof/gtkglarea/
BuildRequires:	mesaglu-devel
BuildRequires:	gtk+-devel

%description
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is very similar
to GtkDrawinigArea widget and adds only three extra functions.

Lower level gdkgl functions make it easy to render on any widget that has
OpenGL capable visual, rendering to off-screen pixmaps is also supported.

Related project which may iterest those who use GTK-- is GtkGLArea--. It is a
C++ wrapper for gtkglarea written by Karl Nelson <kenelson@ece.ucdavis.edu>.

%package -n	%{libname}
Summary:        GtkGLArea is an OpenGL widget for GTK+ GUI toolkit
Group:          System/Libraries
Provides:	%{name}
Obsoletes:	%{name} = %{version}-%{release}

%description -n	%{libname}
Just as GTK+ is build on top of GDK, GtkGLArea is built on top of gdkgl which
is basically wrapper around GLX functions. The widget itself is very similar
to GtkDrawinigArea widget and adds only three extra functions.

Lower level gdkgl functions make it easy to render on any widget that has
OpenGL capable visual, rendering to off-screen pixmaps is also supported.

Related project which may iterest those who use GTK-- is GtkGLArea--. It is a
C++ wrapper for gtkglarea written by Karl Nelson <kenelson@ece.ucdavis.edu>.

%package -n	%{libnamedev}
Summary:	GtkGLArea is an OpenGL widget for GTK+ -- includes and static libs
Group:		Development/GNOME and GTK+
Requires:	%{libname} >= %{version}
Provides:	%{libname}-devel = %{version}-%{release} %{name}-devel = %{version}-%{release} 
Provides:	libgtkglarea-devel
Obsoletes:	%{name}-devel

%description -n	%{libnamedev}
Libraries and includes files you can use for GtkGLArea development

%prep
%setup -q
%patch0 -p1 -b .underquoted

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
ln -sf libgtkgl.so.5.0.0 $RPM_BUILD_ROOT%{_libdir}/libgtkgl.so.4

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{libname}
%defattr(-, root, root)
%doc AUTHORS COPYING ChangeLog README
%{_libdir}/lib*.so.*

%files -n %{libnamedev}
%defattr(-, root, root)
%doc docs/*.txt
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/*
%{_datadir}/aclocal/*
