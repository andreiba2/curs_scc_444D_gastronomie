# Proiect Gastronomie: Cheesecake

**Student:** Ionescu Eduard - Nicolae
**Grupă:** 444D

---

## Structură Proiect

```
app/
├── lib/
│   ├── __init__.py
│   └── biblioteca_gastronomie.py  
screenshots/
Dockerfile
Jenkinsfile
LICENSE
README.md
gastronomie.py
requirements.txt
test_gastronomie.py
```

---

## 1. Funcționalitate

Am implementat o aplicație Flask pentru tema Cheesecake. Interfața  conține rute pentru:

- **Proveniență:** 
- **Ingrediente:** 
- **Mod de preparare** 

---

## 2. Stadiul Implementării

- **Cod aplicație:** Finalizat.
- **Teste unitare:** Implementate în `test_gastronomie.py` (validate local).
- **Jenkins Pipeline:** Configurat și funcțional în totalitate.
- **Containerizare:** Fișier Dockerfile creat, imagine construită și testată.

---

## 3. Containerizare

### Build imagine Docker

![Docker Images](screenshots/poza_docker.png)

### Aplicație rulând în container

![Home](screenshots/poza_home.png)

### Pagina Proveniență

![Provenienta](screenshots/poza_origine.png)

### Pagina Ingrediente

![Ingrediente](screenshots/poza_ingrediente.png)

### Pagina Mod de Preparare

![Preparare](screenshots/poza_preparare.png)

---

## 4. Teste

### Rezultat Pytest

![Pytest](screenshots/rezultat_pytest.png)

### Rezultat Pylint

![Pylint](screenshots/rezultat_pylint.png)

---

## 5. Jenkins Pipeline

![Jenkins](screenshots/jenkins.png)
