#!/usr/bin/env bash

#Run diag

python3 -u /opt/nebraDiagnostics/diagnosticsProgram.py
python3 -m http.server 80
