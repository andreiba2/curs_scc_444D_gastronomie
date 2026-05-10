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