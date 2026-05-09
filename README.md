# Proiect Gastronomie: Chilli con carne

**Student:** Antoci George-Cosmin  
**Grupă:** 444D

## Structură Proiect

```text
.
├── app/
│   └── lib/
│       ├── __init__.py
│       └── biblioteca_gastronomie.py   # Functii pentru Chilli con carne
├── screenshots/                         # Capturi de ecran
├── Dockerfile                           # Configurare Docker
├── Jenkinsfile                          # Pipeline Jenkins
├── gastronomie.py                       # Aplicatia Flask
├── requirements.txt                     # Dependente
├── test_gastronomie.py                  # Teste unitare
└── README.md                            # Documentatia
```

## 1. Functionalitate

Am implementat o aplicatie Flask pentru tema Gastronomie, axata pe Chilli con carne. Aplicatia are rute pentru:
- Provenienta: de unde vine preparatul (Tex-Mex, Texas)
- Ingrediente: lista cu ingredientele principale
- Mod de preparare: pasii pentru a gati

## 2. Stadiul implementarii

- Cod aplicatie: Finalizat.
- Teste unitare: 10 teste implementate in `test_gastronomie.py`.
- Jenkins Pipeline: Configurat si functional.
- Containerizare: Dockerfile creat, imagine construita si testata.

## 3. Testare

### Testare manuala

Aplicatia a fost testata manual din browser, accesand toate rutele si verificand ca informatiile se afiseaza corect.

![Pagina principala](screenshots/pagina_principala_site.png)

![Pagina ingrediente](screenshots/pagina_ingrediente.png)

### Testare cu Jenkins

Am configurat un Jenkinsfile cu 3 stage-uri (verificare fisiere, instalare dependinte, testare unitara). Toate cele 10 teste trec cu succes.

![Pipeline-ul Jenkins](screenshots/jenkins_pagina_principala_pipeline.png)

![Rezultatul testelor in Jenkins](screenshots/jenkins_console_output.png)

![Build-Time-ul din Jenkins](screenshots/Build_Time_Trend.png)
## 4. Containerizare

Am creat un Dockerfile bazat pe `python:3.12-slim` care instaleaza dependintele si porneste aplicatia pe portul 5000.

![Imaginea de container creata](screenshots/docker_images.png)

![Containerul creat pe baza imaginii](screenshots/docker_ps.png)

![Browserul accesand aplicatia din container](screenshots/pagina_principala_site.png)

![Mesajele din consola (logs container)](screenshots/docker_logs.png)

## 5. Integrare

- PR de la `dev_cosmin_antoci` la `main_cosmin_antoci`: in asteptare creare.
- PR de la `main_cosmin_antoci` la `main`: in asteptare creare si review de la un coleg.

## 6. Ce mai e de facut

- [ ] Crearea PR-ului de la `dev_cosmin_antoci` la `main_cosmin_antoci`
- [ ] Crearea PR-ului de la `main_cosmin_antoci` la `main`
- [ ] Obtinerea unui review aprobat de la un coleg de grupa
- [ ] Integrarea README-ului in branch-ul `main` al grupei
