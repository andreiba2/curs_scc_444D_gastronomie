# Tortilla de Patatas - Flask App

## Descriere

Această aplicație web a fost realizată folosind Flask și prezintă preparatul tradițional spaniol Tortilla de Patatas.

Aplicația conține:
- pagina principală
- țara de proveniență
- ingredientele principale
- modul de preparare

---

## Tehnologii folosite

- Python
- Flask
- HTML
- CSS
- Docker
- Jenkins
- GitHub

---

## Structura proiectului

```text
app/
 ├── lib/
 ├── templates/
 ├── static/
 ├── tests/
 └── tortilla_de_patatas.py
```

---

## Rulare aplicație

```bash
python3 -m app.tortilla_de_patatas
```

Aplicația rulează pe:

```text
http://127.0.0.1:5050
```

---

## Testare

Teste rulate:

```bash
python3 -m app.tests.tests_app
python3 -m app.tests.tests_lib
```

Rezultat:
- 4 teste pentru aplicație
- 3 teste pentru bibliotecă

---

## Docker

Build imagine:

```bash
docker build -t tortilla-app .
```

Run container:

```bash
docker run -p 5050:5050 tortilla-app
```

---

## Jenkins

Pipeline Jenkins:
- instalare dependențe
- rulare teste
- build Docker

---

## Branch-uri Git

- dev_serbanescu_daniela
- main_serbanescu_daniela

## Screenshot-uri

### Creare folder proiect

![Creare folder](screenshots/creare_folder_proiect.png)

### Clone + venv

![Clone si venv](screenshots/clone_venv.png)

### Instalare pachete

![Instalare pachete](screenshots/install_pachete.png)

### Creare aplicație Flask

![Aplicatie Flask](screenshots/creat_aplicatia_flask.png)

### Rulat teste

![Teste](screenshots/rulat_teste.png)

### Testare funcționalitate aplicație

![Functionalitate](screenshots/testare_functionalitate_aplicatie.png)

### Testat aplicația

![Testat aplicatia](screenshots/testat_aplicatia.png)

### Activare Jenkins

![Jenkins activ](screenshots/activat_jenkins.png)

### Testare Jenkins

![Jenkins teste](screenshots/testare_jenkins.png)

### Creare Dockerfile

![Dockerfile](screenshots/creare_dockerfile.png)

### Build Docker

![Build Docker](screenshots/build_docker.png)

### Docker Images

![Docker Images](screenshots/docker_images.png)

### Docker PS

![Docker PS](screenshots/docker_ps.png)

### Run Docker

![Run Docker](screenshots/run_docker.png)

### Push pe Git

![Push Git](screenshots/pus_pe_git.png)

### Push pe Main

![Push Main](screenshots/pus_pe_main.png)
