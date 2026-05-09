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
- [adauga screenshot cu rezultatul Jenkins]

## Containerizare
<img width="1641" height="921" alt="image" src="https://github.com/user-attachments/assets/2642d0d0-528d-4b20-844f-81ea51958cd8" />

- [adauga screenshot cu browserul la http://localhost:5000/]
- [adauga screenshot cu consolă container]

## Integrare
- PR creat din `dev_alexandru` → `main_alexandru`
- Review primit de la: Badoi Andrei

## PR-uri la care am facut review
- (de completat dupa ce colegii fac PR-uri)

## Ce mai este de facut
- Integrat README in main prin PR
