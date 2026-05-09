# Proiect Gastronomie: Ramen
**Student:** Curca Andrei-Daniel  
**Grupă:** 444D

## Structură Proiect
```text
.
├── app/
│   └── lib/
│       ├── __init__.py
│       └── biblioteca_gastronomie.py  # Logica pentru Ramen
├── screenshots/                          # Capturi de ecran
├── Dockerfile                        # Configurare Docker
├── Jenkinsfile                       # Pipeline CI/CD
├── gastronomie.py                    # Aplicația Flask
├── requirements.txt                  # Dependențe
├── test_gastronomie.py               # Teste unitare
└── README.md                         # Documentația

```

## 1. Funcționalitate
Am implementat o aplicație Flask pentru tema Gastronomie, axată pe Ramen. Interfața este interactivă și conține rute pentru:

Proveniență: Detalii despre originile preparatului.

Ingrediente: Listarea componentelor principale.

Mod de preparare: Descrierea procesului de gătire.

## 2. Stadiul implementării
Cod aplicație: Finalizat.

Teste unitare: Implementate în test_gastronomie.py (validate local).

Jenkins Pipeline: Configurat și funcțional în totalitate.

Containerizare: Fișier Dockerfile creat, imagine construită și testată.

## 3. Containerizare

![Imaginea de container creata](screenshots/docker_ss.png)

![Containerul creat pe baza imaginii](screenshots/docker_ps.png)

![Browserul accesand aplicatia din container](screenshots/meniu_aplicatie.png)

![Mesaje consola (Log-uri apeluri)](screenshots/loguri.png)

![Testarile Jenkins](screenshots/teste_jenkins.png)

![Dovada Teste Jenkins](screenshots/testare_jenkins.png)

![Pipeline Jenkins](screenshots/pipeline_jenkins.png)
