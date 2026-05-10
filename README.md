# Proiect Gastronomie: Tiramisu ☕

**Student:** Vlad Panait  
**Grupă:** 444D  
**Materia:** SCC (Servicii de cloud și containerizare)

---

##  Structură Proiect pe GitHub

```text
curs_scc_444D_gastronomie/
├── app/
│   └── lib/
│       ├── __init__.py
│       └── biblioteca_gastronomie.py
├── screenshots/
│   ├── Docker.png
│   ├── home.png
│   ├── ingredients.png
│   ├── jerkins.png
│   ├── origins.png
│   ├── prepare.png
│   ├── pylint.png
│   ├── pytest.png
│   └── running.png
├── .gitignore
├── Dockerfile
├── Jenkinsfile
├── README.md
├── gastronomie.py
├── requirements.txt
└── test_gastronomie.py
```

---

## 1.  Funcționalitate Aplicație

Am dezvoltat o aplicație web folosind **Python** și **Flask** pentru tema **Tiramisu**. Aplicația este structurată pentru a oferi informații esențiale despre rețetă prin rute dedicate:

* **Pagina Principală:** Meniu interactiv cu butoane către secțiuni.
* **Istoric (`/tiramisu`):** Detalii despre originea desertului.
* **Ingrediente (`/feature-1`):** Listă completă de cumpărături.
* **Preparare (`/feature-2`):** Instrucțiuni pas cu pas.

---

## 2.  Tehnologii și Implementare

* **Backend:** Flask (Python 3).
* **Validare Cod:** `pylint` pentru calitatea codului.
* **Testare:** `pytest` pentru verificarea automată a rutelor.
* **CI/CD:** Jenkins Pipeline (automatizare completă).
* **Containerizare:** Docker (împachetare și rulare izolată).

---

## 3.  Prezentare Interfață (Screenshots)

### Pagina Principală (Home)
![Home](screenshots/home.png)

### Pagina Proveniență & Istoric
![Origine](screenshots/origins.png)

### Pagina Ingrediente (Feature 1)
![Ingrediente](screenshots/ingredients.png)

### Pagina Mod de Preparare (Feature 2)
![Preparare](screenshots/prepare.png)

---

## 4.  Containerizare Docker

Am creat un `Dockerfile` pentru a rula aplicația într-un container. Mai jos se vede procesul de construcție și aplicația rulând pe portul 5000.

**Build Imagine Docker:**
![Docker Build](screenshots/Docker.png)

**Aplicație activă în Container:**
![Running](screenshots/running.png)

---

## 5.  Testare și Calitate (QA)

Calitatea proiectului este asigurată prin teste automate care verifică dacă toate paginile se încarcă corect.

**Rezultate Pytest:**
![Pytest](screenshots/pytest.png)

**Scor Calitate Pylint:**
![Pylint](screenshots/pylint.png)

---

## 6.  Jenkins Pipeline

Am configurat un Pipeline care execută automat pașii de Checkout, Build și Test la fiecare push pe GitHub.

**Vizualizare Etape Pipeline (Stage View):**
![Jenkins](screenshots/jerkins.png)
