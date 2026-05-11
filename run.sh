#!/bin/bash
# Script pentru rularea manuala a aplicatiei Flask fara Docker

echo "====== Setam calea pentru importurile de Python ======"
export PYTHONPATH=$(pwd)

echo "====== Instalam dependentele ======"
pip3 install -r requirements.txt --break-system-packages 

echo "====== Pornim serverul Flask ======"
python3 gastronomie.py
