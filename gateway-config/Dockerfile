FROM debian:buster-slim  AS buildstep

RUN apt-get update && apt-get upgrade -y && apt-get -y install \
  automake \
  libtool \
  autoconf \
  git \
  ca-certificates\
  pkg-config \
  build-essential\
  libdbus-1-dev\
  libdbus-1-3\
  cmake\
  dbus\
  lsb-release\
  nano

RUN apt-get -y --no-install-recommends install erlang

RUN mkdir /opt/devel

WORKDIR /opt/devel/

RUN git clone https://github.com/helium/gateway-config.git
WORKDIR /opt/devel/gateway-config



RUN make && make release
#RUN cp -R _build/prod/rel/gateway_config/config/com.helium.Config.conf /etc/dbus-1/system.d/

#RUN cp -R _build/prod/rel/gateway_config  /opt/gateway_config

CMD /bin/bash

FROM debian:buster-slim

RUN apt-get update && apt-get upgrade -y  && apt-get -y --no-install-recommends install \
  ca-certificates\
  libdbus-1-3\
  bluez\
  connman\
  erlang-base erlang-common-test erlang-crypto erlang-debugger erlang-dev erlang-dialyzer erlang-diameter erlang-edoc erlang-eldap erlang-erl-docgen erlang-et erlang-eunit erlang-ftp erlang-inets erlang-megaco erlang-mnesia erlang-observer erlang-odbc erlang-os-mon erlang-parsetools erlang-public-key erlang-reltool erlang-runtime-tools erlang-snmp erlang-ssh erlang-ssl erlang-syntax-tools erlang-tftp erlang-tools erlang-wx erlang-xmerl fontconfig fontconfig-config fonts-dejavu-core gtk-update-icon-cache hicolor-icon-theme libatk1.0-0 libatk1.0-data libavahi-client3 libavahi-common-data libavahi-common3 libbsd0 libcairo2 libcroco3 libcups2 libdatrie1 libdbus-1-3 libdrm-amdgpu1 libdrm-common libdrm-etnaviv1 libdrm-nouveau2 libdrm-radeon1 libdrm2 libedit2 libelf1 libexpat1 libfontconfig1 libfreetype6 libfribidi0 libgdk-pixbuf2.0-0 libgdk-pixbuf2.0-common libgl1 libgl1-mesa-dri libglapi-mesa libglib2.0-0 libglu1-mesa libglvnd0 libglx-mesa0 libglx0 libgraphite2-3 libgssapi-krb5-2 libgtk2.0-0 libgtk2.0-common libharfbuzz0b libice6 libicu63 libjbig0 libjpeg62-turbo libjs-jquery libjs-jquery-metadata libjs-jquery-tablesorter libk5crypto3 libkeyutils1 libkrb5-3 libkrb5support0 libllvm7 libltdl7 libncurses6 libnotify4 libodbc1 libpango-1.0-0 libpangocairo-1.0-0 libpangoft2-1.0-0 libpixman-1-0 libpng16-16 libprocps7 librsvg2-2 librsvg2-common libsensors-config libsensors5 libsm6 libssl1.1 libthai-data libthai0 libtiff5 libwebp6 libwxbase3.0-0v5 libwxgtk3.0-0v5 libx11-6 libx11-data libx11-xcb1 libxau6 libxcb-dri2-0 libxcb-dri3-0 libxcb-glx0 libxcb-present0 libxcb-render0 libxcb-shm0 libxcb-sync1 libxcb1 libxcomposite1 libxcursor1 libxdamage1 libxdmcp6 libxext6 libxfixes3 libxi6 libxinerama1 libxml2 libxrandr2 libxrender1 libxshmfence1 libxxf86vm1 lsb-base openssl procps sensible-utils shared-mime-info ucf x11-common







WORKDIR /opt/
COPY --from=buildstep /opt/devel/gateway-config/_build/prod/rel/gateway_config  .

#WORKDIR /etc/dbus-1/system.d/
#COPY --from=buildstep /opt/gateway-config/_build/prod/rel/gateway_config/config/com.helium.Config.conf .
