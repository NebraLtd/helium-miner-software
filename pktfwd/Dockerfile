#Packet Forwarder Docker File
#(C) Pi Supply 2019
#Licensed under the GNU GPL V3 License.
FROM debian:buster-slim AS buildstep

WORKDIR /opt/iotloragateway/packet_forwarder

RUN apt-get update && apt-get -y install protobuf-compiler \
  libprotobuf-dev \
  libprotoc-dev \
  automake \
  libtool \
  autoconf \
  git \
  pkg-config \
  protobuf-c-compiler \
  libprotobuf-c-dev \
  build-essential \
  libc6-dev

COPY buildfiles buildfiles

ARG moo=1
RUN chmod +x ./buildfiles/packetCompile.sh
RUN ./buildfiles/packetCompile.sh



FROM debian:buster-slim

WORKDIR /opt/iotloragateway/packet_forwarder

RUN apt-get update && apt-get -y install libprotobuf-c1 python3-minimal python3-yaml --no-install-recommends && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY --from=buildstep /opt/iotloragateway/packetforwarder_sg0 .
COPY --from=buildstep /usr/local/lib/libpaho-embed-* /usr/lib/
COPY --from=buildstep /usr/lib/libttn* /usr/lib/

COPY lora_templates lora_templates/


RUN cp lora_templates/local_conf.json local_conf_sg0.json
RUN cp lora_templates/EU-global_conf.json global_conf_sg0.json



RUN chmod 777 ./local_conf_sg0.json
RUN chmod +x ./packetforwarder_sg0

COPY files/run_pkt.sh .
COPY files/configurePktFwd.py .
COPY files/reset-pins.sh .
COPY files/reset-38.sh .
COPY files/reset-39.sh .
RUN chmod +x reset-pins.sh
RUN chmod +x reset-38.sh
RUN chmod +x reset-39.sh
RUN chmod +x run_pkt.sh
RUN chmod +x configurePktFwd.py


ENTRYPOINT ["sh", "/opt/iotloragateway/packet_forwarder/run_pkt.sh"]
