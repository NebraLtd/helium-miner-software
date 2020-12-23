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

RUN git clone https://github.com/NebraLtd/gateway-config.git
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

COPY lsb_release  /etc/

RUN mkdir /opt/gateway_config
WORKDIR /opt/gateway_config
COPY --from=buildstep /opt/devel/gateway-config/_build/prod/rel/gateway_config  .

COPY start-gateway-config.sh .
RUN chmod +x start-gateway-config.sh

ENTRYPOINT ["sh", "/opt/gateway_config/start-gateway-config.sh"]
