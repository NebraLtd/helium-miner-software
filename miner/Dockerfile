FROM quay.io/team-helium/miner:latest-arm64

WORKDIR /opt/miner

COPY docker.config /opt/miner/releases/0.1.0/docker.config

ENTRYPOINT ["/opt/miner/bin/miner"]
CMD ["foreground"]
