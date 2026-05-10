
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
  
  ![Jenkins](screenshots/b2_jenkins.png)

## 4. Dovezi Execuție Container (Docker)
Conform cerințelor, mai jos sunt prezentate dovezile foto ale containerizării:

### A. Imaginea Docker creata
![Imagine Docker](screenshots/b2_imagine_docker.png)

### B. Containerul în rulare
![Container activ](screenshots/b2_container_functional.png)

### C. Aplicația în Browser
![Aplicație în browser](screenshots/b2_pagina_web1.png)
![Aplicație în browser](screenshots/b2_pagina_web2.png)
![Aplicație în browser](screenshots/b2_pagina_web3.png)
![Aplicație în browser](screenshots/b2_pagina_web4.png)

### D. Log-urile containerului
![Loguri consolă](screenshots/b2_logs.png)

