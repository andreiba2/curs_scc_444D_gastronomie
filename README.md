# 🍝 Proiect Gastronomie: Paste Carbonara

**Student:** Năstase Magda  
**Grupă:** 444D  

Acest proiect reprezintă o aplicație web dezvoltată în **Flask** care prezintă istoria, ingredientele și modul de preparare al rețetei autentice de Carbonara. Aplicația este complet containerizată și pregătită pentru fluxuri de CI/CD.

---

## 📂 Structură Proiect

```text
.
├── app/
│   └── lib/
│       ├── __init__.py
│       └── biblioteca_gastronomie.py  # Logica și textele (100+ cuvinte)
├── screenshots/                      # Capturi de ecran aplicație & Docker
├── Dockerfile                        # Configurare imagine Docker
├── docker-compose.yml                # Configurare Docker Compose
├── Jenkinsfile                       # Pipeline CI/CD Jenkins
├── gastronomie.py                    # Serverul principal Flask
├── requirements.txt                  # Dependențe (Flask)
├── test_gastronomie.py               # Teste unitare și integrare
└── README.md                         # Documentația proiectului
⚙️ Stadiul Implementării
Aplicația Flask: Finalizată. Include rute dinamice pentru /gastronomie, /provenienta, /ingrediente și /preparare.

Bibliotecă Text: Implementată separat în app/lib pentru a asigura modularitatea codului.

Teste Unitare: Implementate în test_gastronomie.py. Verifică atât conținutul textelor, cât și răspunsul serverului (Status 200 OK).

Containerizare: Imagine Docker bazată pe python:3.9-slim, testată și funcțională.

CI/CD: Fișier Jenkinsfile configurat pentru automatizarea etapelor de Test, Build și Deploy.

🚀 Ghid de Utilizare (Docker)
Pentru a rula proiectul local folosind Docker, urmați pașii:

Opțiunea 1: Docker Manual
Bash
# Construire imagine
docker build -t carbonara-app .

# Lansare container
docker run -d -p 5000:5000 --name container_carbonara carbonara-app
Opțiunea 2: Docker Compose (Recomandat)
Bash
docker-compose up -d --build
Notă: Aplicația poate fi accesată la adresa: http://localhost:5000/gastronomie

✅ Testare Automată
Pentru a rula suita de teste direct în mediul de execuție Docker, folosiți comanda:

Bash
docker exec -it container_carbonara python3 test_gastronomie.py
📸 Screenshots
Toate capturile de ecran care atestă funcționalitatea aplicației, trecerea testelor și statusul containerelor Docker se regăsesc în folderul /screenshots.
