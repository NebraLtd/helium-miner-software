FROM balenalib/raspberrypi3-debian-node

RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get -y install \
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
  dbus

RUN apt-get -y --no-install-recommends install erlang

WORKDIR /opt/

RUN git clone https://github.com/helium/gateway-config.git
WORKDIR /opt/gateway-config

RUN make && make release
RUN cp -R _build/prod/rel/gateway_config/config/com.helium.Config.conf /etc/dbus-1/system.d/

#FROM debian:buster-slim AS buildstep

RUN apt-get -y install \
  ca-certificates\
  libdbus-1-dev\
  libdbus-1-3\
  bluez\
  connman\
  connman-dev\
  dbus

#WORKDIR /opt/
#COPY --from=buildstep /opt/gateway-config/_build/prod/rel/gateway_config  .

#WORKDIR /etc/dbus-1/system.d/
#COPY --from=buildstep /opt/gateway-config/_build/prod/rel/gateway_config/config/com.helium.Config.conf .
