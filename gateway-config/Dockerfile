FROM debian:buster-slim AS buildstep

RUN apt-get update && apt-get upgrade -y && apt-get -y install \
  automake \
  libtool \
  autoconf \
  git \
  pkg-config \
  build-essential\
  erlang-base\
  erlang-asn1\
  erlang-public-key\
  erlang-ssl\
  erlang-inets\
  erlang-dev\
  erlang-cuttlefish\
  libdbus-1-dev\
  bluez\
  connman\
  connman-dev\
  cmake





RUN git clone https://github.com/helium/gateway-config.git
RUN cd gateway-config
RUN make
RUN make release

FROM debian:buster-slim

WORKDIR /opt/
COPY --from=buildstep _build/prod/rel/gateway_config  .
