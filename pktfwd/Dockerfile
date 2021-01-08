#Packet Forwarder Docker File
#(C) Pi Supply 2019
#Licensed under the GNU GPL V3 License.
FROM debian:buster-slim AS buildstep

WORKDIR /opt/iotloragateway/packet_forwarder

RUN apt-get update && apt-get -y install \
  automake \
  libtool \
  autoconf \
  git \
  pkg-config \
  build-essential

COPY buildfiles buildfiles

ARG moo=1
RUN chmod +x ./buildfiles/compileSX1301.sh
RUN ./buildfiles/compileSX1301.sh



FROM debian:buster-slim

WORKDIR /opt/iotloragateway/packet_forwarder

RUN apt-get update && apt-get -y install python3-minimal python3-yaml --no-install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=buildstep /opt/iotloragateway/packetforwarder_sg0 .

COPY lora_templates_sx1301 lora_templates_sx1301/


RUN cp lora_templates_sx1301/local_conf.json local_conf.json
RUN cp lora_templates_sx1301/EU-global_conf.json global_conf.json



RUN chmod 777 ./local_conf_sg0.json
RUN chmod +x ./packetforwarder_sg0

COPY files/run_pkt.sh .
COPY files/configurePktFwd.py .
COPY files/reset-38.sh .
RUN chmod +x reset-38.sh
RUN chmod +x run_pkt.sh
RUN chmod +x configurePktFwd.py


ENTRYPOINT ["sh", "/opt/iotloragateway/packet_forwarder/run_pkt.sh"]
