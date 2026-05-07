# 🍝 Proiect Gastronomie: Paste Carbonara

> Un proiect DevOps complet dedicat rețetei autentice de Carbonara, incluzând containerizare Docker și automatizare CI/CD.

| Student | Grupă | Disciplină |
| :--- | :---: | :--- |
| **Năstase Maria-Magdalena** | 444D | Sisteme de Conducere a Calculatoarelor |

---

## 📸 Prezentare Aplicație (Interfață)

Aplicația oferă o experiență vizuală modernă, cu un fundal tematic și o structură clară pentru a explora rețeta.

<div align="center">
  <img src="screenshots/home_page.png" alt="Interfața Principală" width="80%">
</div>

---

## 🛠️ Structură și Conținut (Tabel Cerințe)

Cerințele de conținut (minimum 100 de cuvinte per secțiune) au fost implementate în biblioteca din folderul `app/lib`.

| Cerință | Status | Descriere Implementare |
| :--- | :---: | :--- |
| **Țara/Locul de proveniență** | ✅ | Capitol istoric despre regiunea Lazio și legătura cu Roma. |
| **Ingrediente principale** | ✅ | Detalii despre cele 5 elemente sacre (Guanciale, Pecorino, Ouo, Piper, Paste). |
| **Mod de preparare** | ✅ | Explicații despre tehnica emulsiei la cald și timing. |

---

## 📂 Organizare Fișiere

Proiectul este organizat conform celor mai bune practici de structură pentru aplicații Flask și pipeline-uri DevOps:

-   📁 `app/lib/`: Biblioteca cu texte și logica de backend (`biblioteca_gastronomie.py`).
-   📁 `screenshots/`: Capturile de ecran care atestă funcționalitatea.
-   📄 `gastronomie.py`: Serverul Flask principal.
-   📄 `test_gastronomie.py`: Testele unitare (verifică textul și rutele).
-   📄 `Dockerfile`: Instrucțiunile de containerizare (bazat pe `python:3.9-slim`).
-   📄 `Jenkinsfile`: Pipeline-ul CI/CD pentru Jenkins.
-   📄 `requirements.txt`: Dependențele Python (Flask).

---

## 🚀 Ghid de Rulare și DevOps

Aplicația este pregătită pentru rulare izolată și automatizare.

### 1. Rulare în Docker

Pentru a porni aplicația într-un container, folosiți comanda:

```bash
# Build imagine și pornire container (pe portul 5000)
docker build -t carbonara-app . && \
docker run -d -p 5000:5000 --name container_carbonara carbonara-app
2. Automatizare CI/CD (Jenkins)
Pipeline-ul configurat în Jenkinsfile automatizează fluxul de lucru la fiecare commit:

Groovy
pipeline {
    agent any
    stages {
        stage('Unit Tests') {
            // Rulează testele înainte de build
        }
        stage('Docker Build') {
            // Construiește noua imagine
        }
        stage('Deploy') {
            // Repornește containerul pe portul 5000
        }
    }
}
