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

RUN apt-get update &&\
  apt-get upgrade -y &&\
  apt-get -y --no-install-recommends install \
  ca-certificates\
  libdbus-1-3\
  bluez\
  connman\
  erlang-nox &&\
  apt-get clean &&\
  rm -rf /var/lib/apt/lists/*






WORKDIR /opt/
COPY --from=buildstep /opt/devel/gateway-config/_build/prod/rel/gateway_config  .

#WORKDIR /etc/dbus-1/system.d/
#COPY --from=buildstep /opt/gateway-config/_build/prod/rel/gateway_config/config/com.helium.Config.conf .
