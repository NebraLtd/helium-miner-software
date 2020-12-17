FROM debian:buster-slim AS buildstep

git clone https://github.com/helium/gateway-config.git
cd gateway-config
make && make release

FROM debian:buster-slim

WORKDIR /opt/
COPY --from=buildstep _build/prod/rel/gateway_config  .
