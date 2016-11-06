%global GitCommit ff4c2da9e03f
Name:          jose4j
Version:       0.5.2
Release:       1%{?dist}
Summary:       The jose.4.j library is an open source (Apache 2.0) implementation of JWT and the JOSE specification suite.
License:       ASL 2.0
URL:           https://bitbucket.org/b_c/jose4j
Source0:       https://bitbucket.org/b_c/jose4j/get/%{name}-%{version}.tar.gz

BuildRequires: maven-local
BuildRequires: mvn(org.slf4j:slf4j-api)
BuildRequires: mvn(ch.qos.logback:logback-classic)
BuildRequires: mvn(org.mockito:mockito-core)
BuildArch:     noarch

%description
The jose.4.j library is a robust and easy to use open source implementation of JSON Web Token (JWT) and the JOSE specification suite (JWS, JWE, and JWK). It is written in Java and relies solely on the JCA APIs for cryptography.

%package javadoc
Summary:       Javadoc for %{name}

%description javadoc
This package contains javadoc for %{name}.

%prep
%setup -n b_c-jose4j-%{GitCommit}

%pom_remove_plugin -r :nexus-staging-maven-plugin

%mvn_file :%{name} %{name}

%build

%mvn_build -s

%install
%mvn_install

%files -f .mfiles-%{name}
%doc README.md
%license LICENSE  NOTICE.txt

%files javadoc -f .mfiles-javadoc
%license LICENSE  NOTICE.txt

%changelog
* Sun Nov 6 2016 Michal Karm Babacek <karm@fedoraproject.org> 0.5.2-1 
- initial rpm

