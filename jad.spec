Summary:	Jad - the fast JAva Decompiler
Name:		jad
Version:	1.5.8e
Release:	0.1
License:	free for non-commercial
Group:		Applications
Source0:	http://www.kpdus.com/jad/linux/%{name}lx158.zip
# Source0-md5:	2f3570f825da2596c62fe14ab902d34f
URL:		http://www.kpdus.com/jad.html
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Jad is a Java decompiler, i.e. program that reads one or more Java
class files and converts them into Java source files which can be
compiled again.

%prep
%setup -qc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install jad $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Readme.txt
%attr(755,root,root) %{_bindir}/jad
