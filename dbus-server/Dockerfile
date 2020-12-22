FROM debian:buster-slim

RUN apt-get update && apt-get upgrade -y && apt-get -y install \
  git \
  ca-certificates\
  pkg-config \
  libdbus-1-3\
  dbus

ENTRYPOINT ["dbus-run-session"]

#FROM debian:buster-slim AS buildstep



#WORKDIR /opt/
#COPY --from=buildstep /opt/gateway-config/_build/prod/rel/gateway_config  .

#WORKDIR /etc/dbus-1/system.d/
#COPY --from=buildstep /opt/gateway-config/_build/prod/rel/gateway_config/config/com.helium.Config.conf .
