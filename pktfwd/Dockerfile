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

ARG moo=2
RUN chmod +x ./buildfiles/compileSX1301.sh
RUN ./buildfiles/compileSX1301.sh



FROM debian:buster-slim

WORKDIR /opt/iotloragateway/packet_forwarder/sx1301

RUN apt-get update && apt-get -y install python3 --no-install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=buildstep /opt/iotloragateway/packetforwarder .

COPY lora_templates_sx1301 lora_templates_sx1301/


RUN cp lora_templates_sx1301/local_conf.json local_conf.json
RUN cp lora_templates_sx1301/EU-global_conf.json global_conf.json



RUN chmod 777 ./local_conf.json
#RUN chmod +x ./packet_forwarder

WORKDIR /opt/iotloragateway/packet_forwarder

COPY files/run_pkt.sh .
COPY files/configurePktFwd.py .
COPY files/reset-38.sh .
RUN chmod +x reset-38.sh
RUN chmod +x run_pkt.sh
RUN chmod +x configurePktFwd.py


ENTRYPOINT ["sh", "/opt/iotloragateway/packet_forwarder/run_pkt.sh"]
