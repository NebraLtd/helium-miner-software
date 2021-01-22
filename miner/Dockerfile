#FROM quay.io/team-helium/miner:latest-arm64
FROM localhost:5000/miner:arm64

WORKDIR /opt/miner

COPY docker.config /opt/miner/releases/0.1.0/sys.config

ENTRYPOINT ["/opt/miner/bin/miner"]
CMD ["foreground"]
