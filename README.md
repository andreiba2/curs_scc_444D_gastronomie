# 🍝 Proiect Gastronomie: Paste Carbonara

**Student:** Năstase Maria-Magdalena  
**Grupă:** 444D  
**Disciplină:** SCC

---

## Structură Proiect

```text
.
├── app/
│   └── lib/
│       ├── __init__.py                # Inițializare modul bibliotecă
│       └── biblioteca_gastronomie.py  # Conținut text (istorie, ingrediente, preparare)
├── screenshots/                       # Capturi de ecran (Interfață, Docker, Teste)
├── Dockerfile                         # Configurare imagine Docker
├── Jenkinsfile                        # Pipeline CI/CD pentru automatizare
├── gastronomie.py                     # Aplicația principală Flask
├── requirements.txt                   # Dependențe Python (Flask)
├── test_gastronomie.py                # Teste unitare pentru validare
└── README.md                          # Documentația proiectului


## 1. Funcționalitate

Am implementat o aplicație Flask pentru tema Gastronomie, axată pe rețeta de **Paste Carbonara**. Interfața este interactivă și conține rute pentru:

* **Proveniență:** Detalii despre originile preparatului în regiunea Lazio.
* **Ingrediente:** Listarea componentelor principale (Guanciale, Pecorino, etc.).
* **Mod de preparare:** Descrierea procesului de gătire și a tehnicii emulsiei.

## 2. Stadiul implementării

* **Cod aplicație:** Finalizat și structurat modular.
* **Teste unitare:** Implementate în test_gastronomie.py (validate local).
* **Jenkins Pipeline:** Configurat și funcțional în totalitate.
* **Containerizare:** Fișier Dockerfile creat, imagine construită și testată.

## 3. Ghid de Rulare (Docker)

Pentru a lansa aplicația într-un container izolat, se utilizează următoarele comenzi:

**docker build -t carbonara-app .** **docker run -d -p 5000:5000 --name container_carbonara carbonara-app**

Aplicația poate fi accesată la: http://localhost:5000/gastronomie

## 4. Testare

Testele automate pot fi rulate direct în containerul Docker:

**docker exec -it container_carbonara python3 test_gastronomie.py**

---
*Proiect realizat pentru disciplina SCC.*
