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




