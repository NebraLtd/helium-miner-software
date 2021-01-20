FROM arm64v8/alpine:edge

WORKDIR /opt/nebraDiagnostics/

RUN apk add --no-cache \
python3 \
i2c-tools \
usbutils \
py3-qrcode \
py3-dbus

RUN mkdir html
COPY startDiag.sh startDiag.sh
COPY Ubuntu-Bold.ttf Ubuntu-Bold.ttf
COPY diagnosticsProgram.py diagnosticsProgram.py
COPY genHTML.py genHTML.py


WORKDIR /opt/nebraDiagnostics/html/
COPY bootstrap.min.css bootstrap.min.css
COPY index.html.template index.html.template

ENTRYPOINT ["sh", "/opt/nebraDiagnostics/startDiag.sh"]
