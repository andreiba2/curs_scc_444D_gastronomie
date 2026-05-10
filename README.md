# Proiect VCGJ - Gastronomie: Ciorba de burta
**Student:** Vijaica Stefan
**Grupă:** 444D

## Structură Proiect

```text
.
├── app/
│   └── lib/
│       ├── __init__.py
│       └── biblioteca_gastronomie.py  # Logica pentru Ciorba de burta
├── imagini/                          # Capturi de ecran (screenshots)
├── Dockerfile                        # Configurare imagine Docker
├── Jenkinsfile                       # Pipeline CI/CD pentru Jenkins
├── gastronomie.py                    # Aplicația principală Flask
├── requirements.txt                  # Dependențe Python (Flask)
├── test_gastronomie.py               # Teste unitare (Unittest)
└── README.md                         # Documentația proiectului

```

## 1. Funcționalitate
Am implementat o aplicație Flask pentru tema Gastronomie, axată pe Ciorba de burta. 
Interfața este interactivă și conține rute pentru:
* Proveniență 
* Ingrediente 
* Mod de preparare 

## 2. Stadiul implementării
* **Cod aplicație:** Finalizat
* **Teste unitare:** Implementate în `test_gastronomie.py` 
* **Jenkins Pipeline:** Configurat și funcțional (Rezultat: PASS) 
* **Containerizare:** Fisier `Dockerfile` creat și testat
* **Integrare:** Codul a fost împins pe branch-ul `dev_vijaica_stefan`. Pull Request-ul către `main_vijaica_stefan` a fost creat și se așteaptă/a primit review și aprobare de la un coleg. 
* **Review-uri acordate:** Pull Request deschis (ID PR:66  verificat de `andreicurcadaniel` ).
## 3. Containerizare (Capturi de ecran obligatorii)
### Imaginea de container creată

![Imagine Docker](screenshots/docker_images.png)

### Containerul creat pe baza imaginii
 
![Container Rulând](screenshots/docker_ps.png)

### Browserul accesând aplicația din container 

![Browser App](screenshots/meniu_aplicatie.png)

![Browser App](screenshots/meniu_aplicatie_1.png)

### Mesaje consolă (Log-uri apeluri) 

![Loguri Consolă](screenshots/loguri.png)

### Build Time Trend

![Teste Jenkins](screenshots/teste_jenkins.png)

![Teste Jenkins](screenshots/jenkins_ok.png)


