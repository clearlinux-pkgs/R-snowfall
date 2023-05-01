#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-snowfall
Version  : 1.84.6.2
Release  : 47
URL      : https://cran.r-project.org/src/contrib/snowfall_1.84-6.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/snowfall_1.84-6.2.tar.gz
Summary  : Easier Cluster Computing (Based on 'snow')
Group    : Development/Tools
License  : GPL-2.0
Requires: R-snow
BuildRequires : R-snow
BuildRequires : buildreq-R

%description
parallel R programs. This package offers e.g. extended error
        checks, and additional functions. All functions work in
        sequential mode, too, if no cluster is present or wished.
        Package is also designed as connector to the cluster management
        tool sfCluster, but can also used without it.

%prep
%setup -q -c -n snowfall
cd %{_builddir}/snowfall

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657041127

%install
export SOURCE_DATE_EPOCH=1657041127
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library snowfall
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library snowfall
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library snowfall
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc snowfall || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/snowfall/DESCRIPTION
/usr/lib64/R/library/snowfall/INDEX
/usr/lib64/R/library/snowfall/Meta/Rd.rds
/usr/lib64/R/library/snowfall/Meta/data.rds
/usr/lib64/R/library/snowfall/Meta/features.rds
/usr/lib64/R/library/snowfall/Meta/hsearch.rds
/usr/lib64/R/library/snowfall/Meta/links.rds
/usr/lib64/R/library/snowfall/Meta/nsInfo.rds
/usr/lib64/R/library/snowfall/Meta/package.rds
/usr/lib64/R/library/snowfall/Meta/vignette.rds
/usr/lib64/R/library/snowfall/NAMESPACE
/usr/lib64/R/library/snowfall/NEWS
/usr/lib64/R/library/snowfall/R/snowfall
/usr/lib64/R/library/snowfall/R/snowfall.rdb
/usr/lib64/R/library/snowfall/R/snowfall.rdx
/usr/lib64/R/library/snowfall/R/sysdata.rdb
/usr/lib64/R/library/snowfall/R/sysdata.rdx
/usr/lib64/R/library/snowfall/data/config.txt.gz
/usr/lib64/R/library/snowfall/data/test.rda
/usr/lib64/R/library/snowfall/doc/index.html
/usr/lib64/R/library/snowfall/doc/snowfall.Snw
/usr/lib64/R/library/snowfall/doc/snowfall.pdf
/usr/lib64/R/library/snowfall/help/AnIndex
/usr/lib64/R/library/snowfall/help/aliases.rds
/usr/lib64/R/library/snowfall/help/paths.rds
/usr/lib64/R/library/snowfall/help/snowfall.rdb
/usr/lib64/R/library/snowfall/help/snowfall.rdx
/usr/lib64/R/library/snowfall/html/00Index.html
/usr/lib64/R/library/snowfall/html/R.css
