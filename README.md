### PROIECT SCC 2026 - 444D

## TEMA: GASTRONOMIE

Bun venit pe README-ul principal al grupei 444D! Mai jos puteți naviga către README-ul fiecărui student al grupei:

1. [Antoci George-Cosmin - Chilli con Carne](#1-antoci-george-cosmin---chilli-con-carne)
2. [Bădoi Andrei-Cristian - Paella](#2-bădoi-andrei-cristian---paella)
3. [Bâtcă David-Andrei - Lava Cake](#3-bâtcă-david-andrei---lava-cake)
4. [Budur Maria - Sushi](#4-budur-maria---sushi)
5. [Butunoi Ioan-Alexandru - Mici](#5-butunoi-ioan-alexandru---mici)
6. [Costea Mihai-Daniel - Brașovence](#6-costea-mihai-daniel---brașovence)
7. [Curcă Andrei-Daniel - Ramen](#7-curcă-andrei-daniel---ramen)
8. [Enache Victor-George - Piftie](#8-enache-victor-george---piftie)
9. [Frăticiu Vlad-Alexandru - Bouyiourdi](#9-frăticiu-vlad-alexandru---bouyiourdi)
10. [Gîtu Ștefan-Teodor - Cordon bleu](#10-gîtu-ștefan-teodor---cordon-bleu)
11. [Guță Andrei-Petrișor - Gulaș](#11-guță-andrei-petrișor---gulaș)
12. [Ionescu Eduard-Nicolae - Cheesecake](#12-ionescu-eduard-nicolae---cheesecake)
13. [Konya Andra-Maria - Lasagna](#13-konya-andra-maria---lasagna)
14. [Năstase Maria-Magdalena - Carbonara](#14-năstase-maria-magdalena---carbonara)
15. [Neacșu Radu-Costin - Margherita](#15-neacșu-radu-costin---margherita)
16. [Nițu Alexandra - Clătite americane](#16-nițu-alexandra---clătite-americane)
17. [Olteanu Rareș-Cristian - Baklava](#17-olteanu-rareș-cristian---baklava)
18. [Panait Vlad-Marian - Tiramisu](#18-panait-vlad-marian---tiramisu)
19. [Popescu Bogdan-Constantin - Tacos](#19-popescu-bogdan-constantin---tacos)
20. [Sămaru Alexandru-Octavian - Salată de boeuf](#20-sămaru-alexandru-octavian---salată-de-boeuf)
21. [Stănciulescu Cristian-Valentin - Ratatouille](#21-stănciulescu-cristian-valentin---ratatouille)
22. [Șerbănescu Daniela-Cristina - Tortilla de patatas](#22-șerbănescu-daniela-cristina---tortilla-de-patatas)
23. [Șimonescu-Diaconu Sebastian-Matei - Pizza](#23-șimonescu-diaconu-sebastian-matei---pizza)
24. [Vîjaică Ștefan - Ciorbă de burtă](#24-vîjaică-ștefan---ciorbă-de-burtă)
25. [Voicu Cătălin-Constantin - Macarons](#25-voicu-cătălin-constantin---macarons)

---

## 1. Antoci George-Cosmin - Chilli con Carne
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

![Pagina principala](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_cosmin_antoci/screenshots/pagina_principala_site.png?raw=true)

![Pagina ingrediente](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_cosmin_antoci/screenshots/pagina_ingrediente.png?raw=true)

### Testare cu Jenkins

Am configurat un Jenkinsfile cu 3 stage-uri (verificare fisiere, instalare dependinte, testare unitara). Toate cele 10 teste trec cu succes.

![Pipeline-ul Jenkins](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_cosmin_antoci/screenshots/jenkins_pagina_principala_pipeline.png?raw=true)

![Rezultatul testelor in Jenkins](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_cosmin_antoci/screenshots/jenkins_console_output.png?raw=true)

![Build-Time-ul din Jenkins](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_cosmin_antoci/screenshots/Build_Time_Trend.png?raw=true)
## 4. Containerizare

Am creat un Dockerfile bazat pe `python:3.12-slim` care instaleaza dependintele si porneste aplicatia pe portul 5000.

![Imaginea de container creata](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_cosmin_antoci/screenshots/docker_images.png?raw=true)

![Containerul creat pe baza imaginii](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_cosmin_antoci/screenshots/docker_ps.png?raw=true)

![Browserul accesand aplicatia din container](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_cosmin_antoci/screenshots/pagina_principala_site.png?raw=true)

![Mesajele din consola (logs container)](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_cosmin_antoci/screenshots/docker_logs.png?raw=true)

## 5. Integrare

- PR de la `dev_cosmin_antoci` la `main_cosmin_antoci`: in asteptare creare.
- PR de la `main_cosmin_antoci` la `main`: in asteptare creare si review de la un coleg.

## 6. Pull Request-uri la care am facut review

- PR #31 - "templates/index.html" de la colegul Costea Mihai Daniel (Brasovence) - Approved

---

## 2. Bădoi Andrei-Cristian - Paella

# Proiect VCGJ - Gastronomie: Paella 🥘
**Dezvoltator:** Bădoi Andrei-Cristian
**ID Dezvoltator:** andreiba2
**Grupă:** 444D

---

## 1. Funcționalitate adăugată
Am implementat modulul pentru preparatul **Paella** în cadrul aplicației de gastronomie. Această contribuție include:
* **Logica de business:** Funcții pentru listarea ingredientelor și a pașilor de preparare în `app/lib/biblioteca_gastronomie.py`.
* **Interfața Web:** Endpoint-uri Flask în `gastronomie.py` pentru randarea paginilor specifice.
* **Resurse:** Fișiere `__init__.py` pentru asigurarea structurii de pachete Python.

## 2. Stadiul implementării (Checklist)
- [x] Codul sursă respectă arhitectura proiectului.
- [x] Bibliotecile de funcții sunt documentate și testate.
- [x] Fișierul `requirements.txt` conține toate dependențele (Flask, Pytest).
- [x] Aplicația este containerizată folosind Docker.
- [x] Pipeline-ul de Jenkins este funcțional (Testare -> Build).

## 3. Testarea și Calitatea aplicației (VCGJ)
Validarea funcționalității a fost realizată prin două metode:

* **Testare Automată (Unit Testing):** Am creat scriptul `test_gastronomie.py` care verifică integritatea datelor pentru Paella folosind `pytest`.
* **Automatizare Jenkins:** Proiectul trece prin stadiul de `Testare Automata` în Jenkins. 
  * **Rezultat:** `passed`
  
  ![Jenkins](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Badoi_Andrei/screenshots/b2_jenkins.png?raw=true)

## 4. Dovezi Execuție Container (Docker)
Conform cerințelor, mai jos sunt prezentate dovezile foto ale containerizării:

### A. Imaginea Docker creata
![Imagine Docker](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Badoi_Andrei/screenshots/b2_imagine_docker.png?raw=true)

### B. Containerul în rulare
![Container activ](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Badoi_Andrei/screenshots/b2_container_functional.png?raw=true)

### C. Aplicația în Browser
![Aplicație în browser](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Badoi_Andrei/screenshots/b2_pagina_web1.png?raw=true)
![Aplicație în browser](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Badoi_Andrei/screenshots/b2_pagina_web2.png?raw=true)
![Aplicație în browser](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Badoi_Andrei/screenshots/b2_pagina_web3.png?raw=true)
![Aplicație în browser](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Badoi_Andrei/screenshots/b2_pagina_web4.png?raw=true)

### D. Log-urile containerului
![Loguri consolă](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Badoi_Andrei/screenshots/b2_logs.png?raw=true)

---

## 3. Bâtcă David-Andrei - Lava Cake
# Gastronomie – Lava Cake App

**Student:** Bâtcă David-Andrei
**Grupa:** 444D

Aplicație web simplă construită cu **Flask**, care prezintă informații despre desertul *Lava Cake*.

---

## Structura proiectului

```
├── app.py                        # Punctul de intrare al aplicației
├── app/
│   └── lib/
│       └── lib_gastronomie.py    # Funcții cu conținut HTML (descriere, ingrediente, etc.)
├── test_gastronomie.py           # Teste unitare
├── Dockerfile                    # Imagine Docker pentru rulare containerizată
├── Jenkinsfile                   # Pipeline CI/CD
└── requirements.txt
```

---

## Rute disponibile

| Rută | Descriere |
|------|-----------|
| `/` | Pagina principală |
| `/lava-cake` | Descriere generală + navigare |
| `/lava-cake/provenienta` | Originea desertului |
| `/lava-cake/ingrediente` | Lista de ingrediente |
| `/lava-cake/preparare` | Mod de preparare pas cu pas |

---

## Rulare locală

```bash
pip install -r requirements.txt
python app.py
```

Aplicația pornește pe `http://localhost:5000`.

---

## Rulare cu Docker

```bash
docker build -t gastronomie-app .
docker run -p 5000:5000 gastronomie-app
```

---

## Testare

```bash
python test_gastronomie.py
```

Testele verifică că funcțiile din `lib_gastronomie.py` returnează conținutul corect (cuvinte cheie: `"francez"`, `"făină"`, `"Coace"`).

---

## CI/CD – Jenkins

Pipeline-ul Jenkins rulează automat două etape:

1. **Instalare dependențe** – creează un virtual environment și instalează pachetele din `requirements.txt`
2. **Testare** – rulează `test_gastronomie.py`

La final afișează `Success ✅` sau `Error ❌`.
---

## 4. Budur C. Maria - Sushi
## Capturi de ecran

### 1. Clonarea repository-ului și crearea branch-ului

![Clonare repository și branch](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_budur_maria/images/2.png?raw=true)

Descriere: captura arată clonarea repository-ului de pe GitHub și crearea branch-ului personal `dev_budur_maria`.

### 2. Instalarea dependențelor

![Instalare dependențe](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_budur_maria/images/3.png?raw=true)

Descriere: captura arată instalarea pachetelor necesare pentru proiect: Flask, pytest și pylint.

### 3. Crearea structurii proiectului

![Structura proiectului](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_budur_maria/images/4.png?raw=true)

Descriere: captura arată crearea folderelor și fișierelor principale pentru aplicația Flask.

### 4. Rularea testelor locale

![Teste locale](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_budur_maria/images/5.png?raw=true)

Descriere: captura arată rularea testelor cu pytest și rezultatul obținut pentru testele aplicației și ale bibliotecii.

### 5. Aplicația rulată în browser

![Aplicația în browser](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_budur_maria/images/8.png?raw=true)

Descriere: captura arată pagina principală a aplicației Sushi rulată în browser.

### 6. Construirea imaginii Docker

![Docker build](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_budur_maria/images/10.png?raw=true)

Descriere: captura arată construirea imaginii Docker pentru aplicația Flask.

### 7. Rularea containerului Docker

![Docker run](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_budur_maria/images/14.png?raw=true)

Descriere: captura arată rularea containerului Docker și pornirea aplicației pe portul 5000.

### 8. Verificarea imaginilor și containerelor Docker

![Docker images și ps](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_budur_maria/images/15.png?raw=true)

Descriere: captura arată verificarea imaginilor Docker create și a containerelor rulate.

### 9. Verificarea Jenkins

![Jenkins status](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_budur_maria/images/17.png?raw=true)

Descriere: captura arată verificarea serviciului Jenkins și faptul că acesta rulează.

### 10. Push pe GitHub

![Git push](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_budur_maria/images/24.png?raw=true)

Descriere: captura arată încărcarea modificărilor pe GitHub pe branch-ul `dev_budur_maria`.

---

## 5. Butunoi Ioan-Alexandru - Mici

# Gastronomie - Mici
**Dezvoltator:** Alexandru  
**Grupă:** 444D  
**Element:** Mici  

## Functionalitate adaugata
- `reteta_mici()` - returneaza reteta traditionala a micilor
- `descriere_mici()` - returneaza descrierea preparatului
- Rute Flask:
  - `/` - pagina principala cu navigare
  - `/gastronomie` - pagina generala gastronomie
  - `/mici` - pagina dedicata micilor
  - `/mici/reteta` - reteta micilor
  - `/mici/descriere` - descrierea micilor

## Stadiul implementarii
- [x] Cod functional adaugat in `app/lib/biblioteca_gastronomie.py`
- [x] Rute Flask adaugate in `gastronomie.py`
- [x] Teste scrise in `tests/test_mici.py`
- [x] Jenkinsfile configurat
- [x] Dockerfile creat
- [x] Aplicatie containerizata si testata

## Testare
### Testare manuala
- Rulat `python gastronomie.py` si accesat rutele in browser 

### Testare cu Jenkins
- Rezultat: **PASS** 
<img width="1625" height="520" alt="image" src="https://github.com/user-attachments/assets/dfc63e67-4068-470b-9d41-a5368e09ec49" />


## Containerizare
<img width="1641" height="921" alt="image" src="https://github.com/user-attachments/assets/2642d0d0-528d-4b20-844f-81ea51958cd8" />

<img width="1641" height="836" alt="image" src="https://github.com/user-attachments/assets/486fbd11-561d-4f19-add1-4f0cc95a895e" />

---

## 6. Costea Mihai-Daniel - Brașovence

# Proiect SCC - Gastronomie (Brasovence)
**Student:** Costea Mihai Daniel 
**Grupa:** 444D 

### Functionalitate:
Adaugat rutele `/gastronomie`, `/brasovence`, `/descriere_brasovence` si `/ingrediente_brasovence`. 
Implementat biblioteca in `app/lib/biblioteca_gastronomie.py`. 

### Stadiu:
Cod aplicatie: Finalizat 
Jenkinsfile: Configurat 
Dockerfile: Creat 

Pagina principala:

<img width="1911" height="883" alt="Screenshot From 2026-05-09 18-49-26" src="https://github.com/user-attachments/assets/ab5cbb07-0a17-408f-b4a0-75a2a2cbf560" />

Pagina Tara/locul de provenienta

<img width="1911" height="883" alt="Screenshot From 2026-05-09 18-49-37" src="https://github.com/user-attachments/assets/d763a36e-5bee-4e24-9f9b-6d70050add7a" />

Pagina Ingrediente

<img width="1911" height="883" alt="Screenshot From 2026-05-09 18-49-49" src="https://github.com/user-attachments/assets/9a6818f4-ddbc-471b-acb0-661e7456ce61" />
Pagina Modul de preparare

<img width="1911" height="883" alt="Screenshot From 2026-05-09 18-49-55" src="https://github.com/user-attachments/assets/738d35e8-b23a-4e7c-b140-1e8bc0879d60" />

Screenshot Jenkins

<img width="1911" height="883" alt="Screenshot From 2026-05-10 18-15-41" src="https://github.com/user-attachments/assets/87957462-ee87-4079-9109-812fbd1c967a" />

---

## 7. Curcă Andrei-Daniel - Ramen

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
├── screenshots/                      # Capturi de ecran
├── Dockerfile                        # Configurare Docker
├── Jenkinsfile                       # Pipeline CI/CD
├── gastronomie.py                    # Aplicația Flask
├── requirements.txt                  # Dependențe
├── test_gastronomie.py               # Teste unitare
└── README.md                         # Documentația

```

## 1. Funcționalitate
Am implementat o aplicație Flask pentru tema Gastronomie, axată pe Ramen. Interfața este interactivă și conține rute pentru:
- **Tema și Elementul (Ramen):** Meniul principal și pagina specifică preparatului.
- **Proveniență:** Detalii despre originile preparatului.
- **Ingrediente:** Listarea componentelor principale.
- **Mod de preparare:** Descrierea procesului de gătire.

## 2. Stadiul implementării
- **Cod aplicație:** Finalizat. Rutele și funcțiile au fost implementate cu succes.
- **Teste unitare:** Implementate în `test_gastronomie.py` (validate local).
- **Jenkins Pipeline:** Configurat și funcțional în totalitate. Testele trec cu statusul PASS.
- **Containerizare:** Fișier `Dockerfile` creat, imagine construită și testată.
- **Integrare:** Codul a fost împins pe branch-ul `dev_Curca_Andrei`. Pull Request-ul către `main_Curca_Andrei` a fost creat și se așteaptă review și aprobare de la un coleg.
- **Review-uri acordate:** Pull Request deschis (ID PR: #63 - verificat de 10stefiv-afk).

## 3. Ce mai este de făcut
Proiectul este considerat finalizat conform cerințelor.

## 4. Demonstrație Vizuală (Screenshots)

### 🐋 Containerizare Docker
*Construirea și rularea containerului*

![Imaginea de container creată](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Curca_Andrei/screenshots/docker_ss.png?raw=true)

![Containerul rulând pe baza imaginii](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Curca_Andrei/screenshots/docker_ps.png?raw=true)

---

### 🌐 Interfața Web a Aplicației
*Navigarea prin aplicația găzduită în container*

![Meniu Principal](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Curca_Andrei/screenshots/meniu_1.png?raw=true)

![Meniu Ramen](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Curca_Andrei/screenshots/meniu_2.png?raw=true)

![Proveniență](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Curca_Andrei/screenshots/meniu_3.png?raw=true)

![Ingrediente](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Curca_Andrei/screenshots/meniu_4.png?raw=true)

![Preparare](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Curca_Andrei/screenshots/meniu_5.png?raw=true)

---

### 🖥️ Jurnal Execuție (Logs)
*Mesaje afișate în consolă la interacțiunea cu browser-ul*

![Log-uri consolă apeluri](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Curca_Andrei/screenshots/loguri.png?raw=true)

---

### ⚙️ CI/CD și Testare cu Jenkins
*Verificarea automată a codului și a testelor unitare*

![Configurare Jenkins Pipeline](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Curca_Andrei/screenshots/pipeline_jenkins.png?raw=true)

![Dovadă Rulare Teste Jenkins](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Curca_Andrei/screenshots/testare_jenkins.png?raw=true)

![Rezultat Final Teste Jenkins](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Curca_Andrei/screenshots/teste_jenkins.png?raw=true)


---

## 8. Enache Victor-George - Piftie

📝 Documentație Proiect: Piftie (Victor Enache)
Element: Piftie

Funcționalitate adăugată: Rutele /gastronomie, /piftie, /descriere_piftie, /ingrediente_piftie și funcțiile aferente din biblioteca_gastronomie.py.

Stadiul implementării: Codul pentru elementul piftie a fost adăugat integral, inclusiv interfața HTML simplă.

Testare: Fișier Jenkinsfile configurat. Testele unitare (pytest) trec cu succes atât la rularea manuală, cât și prin pipeline-ul automat din Jenkins (Status: PASS).

Integrare: Pull Request deschis din dev_victor_enache către main_victor_enache cu rezultatele testelor atașate. Aștept review pentru integrarea finală.

Containerizare: Imagine Docker creată și testată local. Aplicația este funcțională în container.

Testare Jenkins : <img width="946" height="321" alt="Screenshot 2026-05-08 192817" src="https://github.com/user-attachments/assets/3c7a36ee-f85a-4bdb-bca6-5f4bc24e586a" />

🐳 Demonstrație Containerizare (Docker)
Aici inserezi cele 4 capturi de ecran obligatorii:

Imagine Docker: <img width="704" height="141" alt="image" src="https://github.com/user-attachments/assets/f771d438-caa4-4341-89cf-06d7492f3599" />

Container pornit: <img width="850" height="109" alt="image" src="https://github.com/user-attachments/assets/5546a07d-5e46-46ce-8ce0-ce087e3cc6d4" />

Acces Browser: <img width="1128" height="673" alt="Screenshot 2026-05-08 195119" src="https://github.com/user-attachments/assets/d715eb7a-33ca-464d-ad29-96b29241eda6" />

Log-uri Consolă: <img width="874" height="314" alt="image" src="https://github.com/user-attachments/assets/6bb386f5-4fe6-4870-9376-1b3c39178697" />

---

## 9. Frăticiu Vlad-Alexandru - Bouyiourdi


### Dovezi Implementare și Testare
#### Teste Unitare
Toate testele au trecut cu succes, validând logica bibliotecii:
![Teste Unitare](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Fraticiu_Vlad/Screenshots/teste_unitare.png?raw=true)

#### Containerizare Docker
Aplicația a fost împachetată și rulată într-un container izolat:
- **Imagine creată:** ![Imagine Docker](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Fraticiu_Vlad/Screenshots/imagine_docker.png?raw=true)
- **Execuție container:** ![Execuție](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Fraticiu_Vlad/Screenshots/executie_docker.png?raw=true)

#### Verificare Funcționalitate
Logurile de acces și vizualizarea în browser confirmă funcționarea corectă:
- **Loguri Consolă:** ![Loguri](https://github.com/andreiba2/curs_scc_444D_gastronomie/raw/main_Fraticiu_Vlad/Screenshots/loguri_consola.png)
- **Browser:** ![Browser](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Fraticiu_Vlad/Screenshots/aplicatie_browser.png?raw=true)
---

## 10. Gîtu Ștefan-Teodor - Cordon bleu

# Proiect SCC 2026 - Cordon Bleu

## Informații generale
- **Tema grupei:** Gastronomie (444D)
- **Element ales:** Cordon Bleu
- **Student:** Stefan Gitu
- **Branch dezvoltare:** dev_stefan_gitu
- **Branch principal:** main_stefan_gitu

## Funcționalitate implementată

| Rută | Descriere |
|---|---|
| `/gastronomie` | Pagina principală |
| `/cordon_bleu` | Elementul ales |
| `/cordon_bleu/descriere` | Descrierea preparatului |
| `/cordon_bleu/origine` | Originea preparatului |

## Screenshot-uri aplicație

### Pagina principală Gastronomie
![Gastronomie](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_stefan_gitu/img/Screenshot_from_2026-05-10_00-32-34.png?raw=true)

### Pagina Cordon Bleu
![Cordon Bleu](https://github.com/andreiba2/curs_scc_444D_gastronomie/raw/main_stefan_gitu/img/Screenshot_from_2026-05-10_00-33-04.png?raw=true)

### Pagina Descriere
![Descriere](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_stefan_gitu/img/Screenshot_from_2026-05-10_00-33-13.png?raw=true)

### Pagina Origine
![Origine](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_stefan_gitu/img/Screenshot_from_2026-05-10_00-33-22.png?raw=true)

## Screenshot Jenkins - Teste trecute
![Jenkins](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_stefan_gitu/img/Screenshot_from_2026-05-10_00-47-19.png?raw=true)

---

## 11. Guță Andrei-Petrișor - Gulaș
# curs_scc_444D_gastronomie
# Gulaș — Guta Andrei-Petrisor (444D)

## Funcționalitati adăugate
- Funcția `provenienta_gulas()` — returnează originea istorică a gulașului
- Funcția `ingrediente_gulas()` — returnează ingredientele principale
- Funcția `preparare_gulas()` — returnează metoda de preparare
- 
Rute disponibile:
- `/gastronomie` — pagina temei
- `/gulas` — pagina elementului
- `/gulas/provenienta_gulas` — originea gulașului
- `/gulas/ingrediente_gulas` — ingredientele gulașului
- `/gulas/preparare_gulas` — prepararea gulașului
  
![](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Guta_Andrei/screenshots/working_app.png?raw=true)

## Testare
### Testare manuală
Aplicația a fost pornită local cu `python3 gastronomie.py` și rutele au fost accesate din browser.

### Testare cu Jenkins
Testele rulate manual si cu automat cu Jenkins utilizand `pytest`. Rezultat: **PASS**
![](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Guta_Andrei/screenshots/jenkins_pass.png?raw=true)

##Integrare
PR deschis din `dev_Guta_Andrei` către `main_Guta_Andrei` (cu rezultate teste atașate). Aștept review pentru PR-ul către ramura `main` pentru README.

## Containerizare
Imagine creata si testare locala.

Docker build and run
![](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Guta_Andrei/screenshots/docker_build+run.png?raw=true)

Id container Docker
![](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Guta_Andrei/screenshots/docker_container_id.png?raw=true)

Docker Logs
![](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Guta_Andrei/screenshots/docker_logs.png?raw=true)



Docker Images
![](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Guta_Andrei/screenshots/docker_images.png?raw=true)

---

## 12. Ionescu Eduard-Nicolae - Cheesecake

# Proiect Gastronomie: Cheesecake

**Student:** Ionescu Eduard - Nicolae
**Grupă:** 444D

---

## Structură Proiect

```
app/
├── lib/
│   └── biblioteca_gastronomie.py  
screenshots/
tests/
│   └── test_verificare_descriere.py 
│   └── test_verificare_ingrediente.py 
│   └── test_verificare_preparare.py 
Dockerfile
Jenkinsfile
LICENSE
README.md
gastronomie.py
requirements.txt
```

---

## 1. Funcționalitate

Am implementat o aplicație Flask pentru tema Cheesecake. Interfața conține rute pentru:

- **Pagina de start** `/` 
- **Proveniență** `/origine` 
- **Ingrediente** `/ingrediente`
- **Mod de preparare** `/preparare`

---

## 2. Stadiul Implementării

- **Cod aplicație:** Finalizat.
- **Teste unitare:** Implementate în folderul `tests` (test_verificare_descriere, test_verificare_ingrediente, test_verificare_preparare - verificate local si in Jenkins).
- **Jenkins Pipeline:** Configurat și funcțional în totalitate.
- **Containerizare:** Fișier Dockerfile creat, imagine construită și testată.

##Integrare PR #2, #8, #37 inchise din dev_Ionescu_Eduard_Nicolae către main_Ionescu_Eduard_Nicolae. 

##Integrare PR #56 deschis din dev_Ionescu_Eduard_Nicolae către main_Ionescu_Eduard_Nicolae (am atasat rezultatul testelor din Jenkins). 

##Am pus la review README-ul către ramura main.

##Am facut review la PR #55.
---

## 3. Containerizare

### Buildarea si rularea imaginii Docker

![Docker Images](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Ionescu_Eduard_Nicolae/screenshots/poza_docker_build.png?raw=true)
![Docker Images](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Ionescu_Eduard_Nicolae/screenshots/poza_docker_run.png?raw=true)
![Docker Images](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Ionescu_Eduard_Nicolae/screenshots/poza_docker_logs.png?raw=true)
![Docker Images](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Ionescu_Eduard_Nicolae/screenshots/poza_docker_images.png?raw=true)

---

## 4. Testare manuala - Rutele au fost accesate din browser.

### Aplicație rulând în container

![Home](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Ionescu_Eduard_Nicolae/screenshots/poza_home.png?raw=true)

### Pagina Proveniență

![Provenienta](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Ionescu_Eduard_Nicolae/screenshots/poza_origine.png?raw=true)

### Pagina Ingrediente

![Ingrediente](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Ionescu_Eduard_Nicolae/screenshots/poza_ingrediente.png?raw=true)

### Pagina Mod de Preparare

![Preparare](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Ionescu_Eduard_Nicolae/screenshots/poza_preparare.png?raw=true)

### Rezultat Pytest
    
    Am pornit local testele cu comanda "python3 -m pytest"

![Pytest](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Ionescu_Eduard_Nicolae/screenshots/rezultat_pytest.png?raw=true)

---

## 5. Testare automata - Jenkins Pipeline

Testele au rulat cu succes din Jenkins odata cu finalizarea aplicatiei si dupa fixarea erorilor de build specifice Jenkins.

![Jenkins](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Ionescu_Eduard_Nicolae/screenshots/jenkins.png?raw=true)
![Jenkins](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_Ionescu_Eduard_Nicolae/screenshots/jenkins_teste.png?raw=true)

---

## 13. Konya Andra-Maria - Lasagna

# Proiect VCGJ - Gastronomie: Lasagna
**Dezvoltator:** Konya Andra-Maria
**ID Dezvoltator:** andrakonya16

## 1. Funcționalitate adăugată
Am implementat funcționalitatea pentru preparatul **Lasagna** în cadrul temei de Gastronomie. Aceasta include:
* O bibliotecă Python situată în `app/lib/biblioteca_gastronomie.py` cu funcții pentru ingrediente și mod de preparare.
* Rute dedicate în aplicația principală `gastronomie.py` pentru vizualizarea acestor informații în browser.

## 2. Stadiul implementării
- [x] Codul sursă a fost adăugat în repository pe branch-ul de dezvoltare.
- [x] Structura de directoare respectă cerințele (`app/lib/`).
- [x] Aplicația WEB rulează și funcționalitatea poate fi accesată din browser.

## 3. Testarea aplicației
Testarea a fost realizată atât manual, cât și automat:
* **Testare manuală:** Verificarea fiecărei rute direct în browser.
* **Testare automată:** Utilizarea `unit-test`-elor în Python (fișierul `test_gastronomie.py`).
* **Jenkins:** Fișierul `Jenkinsfile` este configurat pentru a rula testele automat la fiecare build. Testele trec cu succes (Rezultat: **PASS**).
![Testare Jenkins](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_konya_andra/screenshots/k_jenkins.jpeg?raw=true)

## 4. Integrare și Code Review
* **Status PR:** Codul a fost integrat cu succes din branch-ul `dev_konya_andra` în `main_konya_andra`. Fişierul README.md a fost integrat în branch-ul `main` al grupei.
* **Review-uri efectuate:** Am efectuat code review pentru Pull Request lui:
    * PR ID # 78 - andreiba2

## 5. Containerizare (Docker)
Aplicația a fost containerizată folosind un `Dockerfile`. Containerul include toată funcționalitatea necesară pentru preparatul Lasagna și rulează cu succes.

### Dovezi execuție container:
1. **Imaginea de container creată:** ![Imagine Docker](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_konya_andra/screenshots/k_imagine_docker.jpeg?raw=true) 
2. **Containerul creat și rulând:** ![Container activ](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_konya_andra/screenshots/k_container_functional.jpeg?raw=true)
3. **Browserul accesând aplicația din container:** ![Pagina principala](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_konya_andra/screenshots/k_pagina_web1.jpeg?raw=true)
 ![Pagina Lasagna](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_konya_andra/screenshots/k_pagina_web2.jpeg?raw=true)
 ![Pagina mod de preparare](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_konya_andra/screenshots/k_pagina_web3.jpeg?raw=true)
 ![Pagina ingrediente](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_konya_andra/screenshots/k_pagina_web4.jpeg?raw=true)
4. **Consola cu mesajele de log ale aplicației:** ![Loguri consolă](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_konya_andra/screenshots/k_logs.jpeg?raw=true)

## 6. Stare finală
- [x] Proiect finalizat cu succes și toate cerințele din documentație îndeplinite. Documentația este disponibilă în branch-ul de dezvoltare și în cel main.

---

## 14. Năstase Maria-Magdalena - Carbonara

# 🍝 Proiect Gastronomie: Paste Carbonara

**Student:** Năstase Maria-Magdalena  
**Grupă:** 444D  
**Disciplină:** SCC

## Structură Proiect

Fiecare componentă a fost organizată pentru a respecta cerințele de dezvoltare colaborativă și livrare continuă: 

```text
.
├── app/
│   └── lib/
│       ├── __init__.py                # Initializare modul bibliotecă
│       └── biblioteca_gastronomie.py  # Conține funcțiile specifice elementului (Ingrediente, Proveniență) 

├── screenshots/                       # Capturi de ecran (Aplicație/Docker)
├── Dockerfile                         # Configurare imagine Docker
├── Jenkinsfile                        # Pipeline CI/CD Jenkins
├── gastronomie.py                     # Aplicația principală Flask configurată cu cele 4 rute
├── requirements.txt                   # Dependențe Python (Flask)
├── test_gastronomie.py                # Teste unitare și integrare
└── README.md                          # Documentația proiectului
```

## 2. Funcționalitate
Aplicația Flask pentru tema **Gastronomie** se concentrează pe elementul **Paste Carbonara** și include cele **patru rute obligatorii**: 
- **Tema:** `/gastronomie` - Pagina generală de prezentare a temei grupei. 
- **Elementul:** `/gastronomie/carbonara` - Pagina principală dedicată elementului ales. 
- **Caracteristica 1 -> Proveniență:** `/gastronomie/carbonara/provenienta` - Detalii despre originile rețetei. 
- **Caracteristica 2 -> Ingrediente:** `/gastronomie/carbonara/ingrediente` - Lista ingredientelor autentice. 
- **Caracteristica 3 -> Mod de preparare:** `/gastronomie/carbonara/preparare` - Tehnica specifică de gătire.

---

## 3. Stadiul implementării
* **Cod aplicație:** Finalizat și integrat. Rutele și funcțiile din bibliotecă sunt complet funcționale.**Teste unitare:** Implementate în `test_gastronomie.py` și validate local. 
* **Jenkins Pipeline:** Configurat corect; testele sunt executate automat și au statusul **PASS**. 
* **Containerizare:** Proiectul este pregătit de livrare prin Docker; aplicația rulează pe portul **5000**. 
* **Integrare:** Codul a fost integrat în branch-ul `main_nastase_magda` în urma procesului de review. 
* **Ce mai este de făcut:** Proiectul este finalizat conform specificațiilor actuale. 

## 4. Interfața Web (Capturi de ecran)
*Aici sunt prezentate capturile cu interfața grafică dezvoltată:*

### Pagina Principală (Home)
![Home](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_nastase_magda/screenshots/Home.png?raw=true)

### Structura Rutelor catre Caracteristici
![Rute](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_nastase_magda/screenshots/rute.png?raw=true)

### Detalii Carbonara (Caracteristicile)

Caracteristica 1 -> Provenienta
![Carbonara 1](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_nastase_magda/screenshots/car1.png?raw=true)
Caracteristica 2 -> Ingrediente
![Carbonara 2](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_nastase_magda/screenshots/car2.png?raw=true)
Caracteristica 3 -> Preparare
![Carbonara 3](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_nastase_magda/screenshots/car3.png?raw=true)
---

## 5. Containerizare (Dovezi Docker)
Conform cerințelor de containerizare, am realizat următoarele capturi: 

### Imaginea de container creată
![Imagine](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_nastase_magda/screenshots/docker_imgs.png?raw=true)

### Containerul rulând pe baza imaginii (docker ps)
![Container](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_nastase_magda/screenshots/docker_ps.png?raw=true)

### Browserul accesând aplicația din container
![Browser](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_nastase_magda/screenshots/Home.png?raw=true) 

### Mesajele afișate în consolă (Log-uri/docker logs)
![Logs](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_nastase_magda/screenshots/docker_run.png?raw=true)

### Rezultatul rulării testelor cu Jenkins (PASS)
![Jenkins](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_nastase_magda/screenshots/docker_run.png?raw=true)

---

## 6. Ghid de Rulare (Docker)
* Pentru a lansa aplicația într-un container izolat, se utilizează următoarele comenzi:

 Construire imagine

* `docker build -t carbonara-app .`

 Lansare container

* `docker run -d -p 5000:5000 --name container_carbonara carbonara-app`

---

## 7. Integrare și Review
Colaborarea a fost realizată prin sistemul de Pull Request pe GitHub: 

* **ID Pull Request Personal:** #69, de pe branch-ul  dev_nastase_magda către main_nastase_magda
* **Aprobare primită:** PR-ul a fost validat de la andreiba2, confirmând calitatea codului. 

---

*Proiect realizat pentru disciplina **Servicii Cloud și Containerizare**, 2026.* 

---

## 15. Neacșu Radu-Costin - Margherita

# Proiect SCC - Gastronomie (Margherita)

**Student:** Neacșu Radu-Costin  
**Grupa:** 444D  
**Branch dezvoltare:** dev_neacsu_radu  
**Branch principal:** main_neacsu_radu  

### 1. Funcționalitate
Am implementat o aplicație Flask pentru tema Gastronomie, axată pe Pizza Margherita. Interfața este interactivă și conține rute pentru:
- **Principală:** Pagina de start și meniul de navigare.
- **Proveniență:** Detalii despre originile preparatului.
- **Ingrediente:** Listarea componentelor principale.
- **Mod de preparare:** Descrierea procesului de gătire.

### 2. Stadiul implementării
- **Cod aplicație:** Finalizat. Rutele și funcțiile Flask au fost implementate cu succes.
- **Teste unitare:** Implementate în `test_gastronomie.py` (validate local).
- **Testare manuală:** Interfața web a fost validată manual prin accesarea fiecărei rute în browser pe `localhost:5000`, asigurând afișarea corectă a conținutului și funcționarea butoanelor.

![Testare Manuala](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_neacsu_radu/screenshots/Testare_manuala.png?raw=true)

- **Jenkins Pipeline:** Configurat și funcțional în totalitate. Testele automate trec cu statusul PASS.
- **Containerizare:** Fișier `Dockerfile` creat, imagine construită și testată cu succes.
- **Integrare:** Codul a fost împins pe branch-ul `dev_neacsu_radu`. Pull Request-ul către `main_neacsu_radu` a fost creat, aprobat și integrat cu succes.
- **Review-uri acordate:** Am realizat code review pentru un coleg de echipă.

### 3. Testare Automată (Jenkins)
- Testele unitare au fost rulate cu succes folosind un pipeline declarativ.
- Rezultat Jenkins: PASS. Istoricul execuției și pipeline-ul vizual:

![Jenkins Pipeline](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_neacsu_radu/screenshots/Jenkins_Pipeline.png?raw=true)

### 4. Containerizare (Docker)
Aplicația a fost containerizată și testată. Dovezi:

- **Imaginea creată:** ![Imagine](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_neacsu_radu/screenshots/sudo_docker_images.png?raw=true)

- **Containerul creat:** ![Container](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_neacsu_radu/screenshots/sudo_docker_ps.png?raw=true)

- **Mesaje consolă:** ![Logs](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_neacsu_radu/screenshots/sudo_docker_run.png?raw=true)

- **Acces din browser (Paginile aplicației):** *Pagina Principală:*
![Browser](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_neacsu_radu/screenshots/Pagina_principala.png?raw=true)

*Pagina Proveniență:*
![Provenienta](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_neacsu_radu/screenshots/Provenienta.png?raw=true)

*Pagina Ingrediente:*
![Ingrediente](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_neacsu_radu/screenshots/Ingrediente.png?raw=true)

*Pagina Preparare:*
![Preparare](https://github.com/andreiba2/curs_scc_444D_gastronomie/blob/main_neacsu_radu/screenshots/Preparare.png?raw=true)

---

## 16. Nițu Alexandra - Clătite americane
*(Lipește aici README-ul Alexandrei)*
---

## 17. Olteanu Rareș-Cristian - Baklava
*(Lipește aici README-ul lui Rareș)*
---

## 18. Panait Vlad-Marian - Tiramisu
*(Lipește aici README-ul lui Vlad)*
---

## 19. Popescu Bogdan-Constantin - Tacos
*(Lipește aici README-ul lui Bogdan)*
---

## 20. Sămaru Alexandru-Octavian - Salată de boeuf
*(Lipește aici README-ul lui Alexandru)*
---

## 21. Stănciulescu Cristian-Valentin - Ratatouille
*(Lipește aici README-ul lui Cristian)*
---

## 22. Șerbănescu Daniela-Cristina - Tortilla de patatas
*(Lipește aici README-ul Danielei)*
---

## 23. Șimonescu-Diaconu Sebastian-Matei - Pizza
*(Lipește aici README-ul lui Sebastian)*
---

## 24. Vîjaică Ștefan - Ciorbă de burtă
*(Lipește aici README-ul lui Ștefan)*
---

## 25. Voicu Cătălin-Constantin - Macarons
*(Lipește aici README-ul lui Cătălin)*
---
