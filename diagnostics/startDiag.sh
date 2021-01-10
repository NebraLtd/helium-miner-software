#!/usr/bin/env bash

#Run diag
sleep(30)
python3 -u /opt/nebraDiagnostics/diagnosticsProgram.py
python3 -m http.server 80
