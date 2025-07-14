#!/bin/bash

echo "[*] Installing Python dependencies..."
pip install -r requirements.txt
pip install -r sidecar-requirements.txt
pip install -r ui-requirements.txt

echo "[*] Building Docker images..."
docker build . -f aeroalpes.Dockerfile -t aeroalpes/flask
docker build . -f adaptador.Dockerfile -t aeroalpes/adaptador
docker build . -f notificacion.Dockerfile -t aeroalpes/notificacion
docker build . -f ui.Dockerfile -t aeroalpes/ui

echo "[*] Pulling docker-compose dependencies..."
docker-compose pull

echo "[✓] Dev container setup completed successfully."
