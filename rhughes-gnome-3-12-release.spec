%define repo gnome-3-12

Name:           rhughes-%{repo}-release
Version:        20
Release:        2.R
Summary:        Rhuges Fedora (%{repo}) Repository Configuration

Group:          System Environment/Base
License:        BSD
URL:            http://copr.fedoraproject.org/coprs/rhughes/
Source0:	rhughes-%{repo}-x86_64.repo
Source1:        rhughes-%{repo}-i386.repo

Requires:       system-release >= %{version}

%description
This COPR contains backported GNOME 3.12 packages and any required system
dependencies for Fedora 20. It contains packages built automatically that
have had very little testing.

%prep
echo "Nothing to prep"

%build
echo "Nothing to build"

%install
# Create dirs
install -d -m755 \
  $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d

# Yum .repo files
%ifarch x86_64
%{__install} -p -m644 %{SOURCE0} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rhughes-%{repo}.repo
%else
%{__install} -p -m644 %{SOURCE1} \
    $RPM_BUILD_ROOT%{_sysconfdir}/yum.repos.d/rhughes-%{repo}.repo
%endif

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/yum.repos.d/*


%changelog
* Thu Apr  3 2014 Arkady L. Shane <ashejn@rhughes.ru> - 20-1.R
- initial build
