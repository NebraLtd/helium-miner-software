FROM debian:buster-slim

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
  bluez\
  connman\
  connman-dev\
  cmake\
  dbus

RUN apt-get -y --no-install-recommends install erlang

WORKDIR /opt/

RUN git clone https://github.com/helium/gateway-config.git
WORKDIR /opt/gateway-config

RUN make && make release

#FROM debian:buster-slim AS buildstep

#WORKDIR /opt/
#COPY --from=buildstep /opt/gateway-config/_build/prod/rel/gateway_config  .

#WORKDIR /etc/dbus-1/system.d/
#COPY --from=buildstep /opt/gateway-config/_build/prod/rel/gateway_config/config/com.helium.Config.conf .
