FROM debian:buster-slim

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
  dbus

ENTRYPOINT ["dbus-run-session"]

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
