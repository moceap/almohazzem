Summary(ar): البيئة التّحزيمية المُتكاملة
Summary: Powerful Linux packaging SDK
Name: almohazzem
Version: 1.3.2
Release: 3%{?dist}
License: WAQFv1
BuildArch: noarch
URL: http://ojuba.org
BuildRequires:	desktop-file-utils
Requires: gtkdialog, almohawell, fakeroot
Requires: almohawell
Requires: fakeroot
Source: %{name}-%{version}.tar.gz

%description -l ar
الحمد و الفضل لله الذي وفّق لإطلاق هذا الإنجاز ، فبمنته وكرمه تم
التوصل إلى بيئة المحزم التطويرية .

بيئة المحزم التطويرية تمكن المطوّرين و المبرمجين المبتدئين على
حد سواء من إنشاء حزمهم اللينكساوية باحترافية بضغطة واحدة .

وبالإضافة إلى السهولة الشديدة و اليسر الذي توفره بيئة المحزم في
التحزيم ، توفر بيئة المحزم خيارات كثيرة في الصدفة كما توفر على
أدوات تتعلق بالحزم الجاهزة من ( تحويل - تثبيت - استخراج ) .

تحوي بيئة المحزم في طياتها على العديد من البرامج الفريدة كمولد
الرموز و مولد المُدخلات ، مما يضفي لمسة رائعة لعملية التحزيم .

من الله يأمل مشروع ألماسه لكم النفع .

%description
Allah all thanked to help us in releasing this SDK

almohazzem SDK own both developers and starter programmers
the ability to produce their Linux packages in just one click

Addition to this simply in packaging , Almohazzem SDK provide
multi fuctions related in already packages such as ( convert -
install - extract ) .

Almohazzem SDK also has many special peograms like Icons 
Generator (IG) and Desktop Entries Generator (DEG) , all of
those making the packaging operations more amazing .

Allah asked by almasa project to benifit you .

%prep
%setup -q

%build
#Nothing To Build.

%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_prefix}/almasa
mkdir -p %{buildroot}/%{_datadir}
install -m 755 bin/almohazzem %{buildroot}/%{_bindir}
cp -r share/* %{buildroot}/%{_datadir}
cp -r almasa/* %{buildroot}/%{_prefix}/almasa
desktop-file-install %{buildroot}/%{_datadir}/applications/almohazzem.desktop

%post
update-mime-database /usr/share/mime
update-desktop-database

%postun
update-mime-database /usr/share/mime
update-desktop-database

%files
%{_datadir}/*
%{_bindir}/almohazzem
"/usr/almasa/languages/almohazzem/en"
"/usr/almasa/languages/almohazzem/ar"

%changelog
* Sun Nov 27 2016 Mosaab Alzoubi <moceap@hotmail.com> - 1.3.2-3
- Rebuilt for Fedora 25

* Tue Feb 25 2014 by Mosaab Hosni Alzoubi <moceap@hotmail.com> - 1.3.2-2
- General Revision.

* Sat May 18 2013 by Mosaab Hosni Alzoubi <moceap@hotmail.com> - 1.0-1
- packed by Almohazzem 1.0 (Powerful packaging SDK)
