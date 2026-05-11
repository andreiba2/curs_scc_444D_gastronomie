#!/bin/bash
# Script pentru rularea manuala a testelor unitare local

echo "====== Setam calea pentru importurile de Python ======"
export PYTHONPATH=$(pwd)

echo "====== Instalam pytest (daca lipseste) ======"
pip3 install -r requirements.txt --break-system-packages 2>/dev/null

echo "====== Rulam testele unitare cu pytest ======"
pytest test_gastronomie.py -v

