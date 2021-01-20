#!/usr/bin/env bash

#Run diag
sleep(90)
rm /opt/nebraDiagnostics/html/index.html
python3 -u /opt/nebraDiagnostics/diagnosticsProgram.py
python3 -m http.server 80
