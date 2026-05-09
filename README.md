🥗 Proiect SCC - Gastronomie: Salata de Boeuf
Acest proiect reprezintă implementarea individuală a elementului Salata de Boeuf în cadrul temei de grupă „Gastronomie”, respectând fluxul de lucru Git, testarea automată cu Jenkins și containerizarea cu Docker.

🛠️ Detalii Implementare
1. Funcționalitate Aplicație
Aplicația este dezvoltată în Python folosind framework-ul Flask. Au fost implementate următoarele componente:

Bibliotecă locală: app/lib/biblioteca_gastronomie.py conține funcțiile descriere_salata_boeuf() și ingrediente_salata_boeuf().

Rute Flask:

/gastronomie - Pagina de prezentare a temei generale.

/salata_boeuf - Pagina principală a elementului.

/descriere_salata_boeuf - Afișează instrucțiunile de preparare.

/ingrediente_salata_boeuf - Afișează lista de ingrediente necesare.

🧪 Testare și Integrare
Testare Automată (Jenkins)
A fost configurat un fișier Jenkinsfile care rulează automat testele unitare (pytest) la fiecare build.

Status Build: ✅ PASS

<img width="1040" height="525" alt="image" src="https://github.com/user-attachments/assets/c5d01dae-2dac-4a8d-a07d-0403fd506d07" />

Fișier test: test_salata_boeuf.py (verifică integritatea datelor și prezența cuvintelor cheie).

Integrare Git
Branch-uri folosite: dev_alexandru_samaru -> main_alexandru_samaru.

Pull Request: Creat cu succes, include raportul de testare Jenkins.

🐳 Containerizare (Docker)
Aplicația a fost împachetată într-un container Docker pentru izolare și portabilitate.

Dovezi Implementare:
1. Imaginea Docker creată:
<img width="802" height="44" alt="image" src="https://github.com/user-attachments/assets/bc313b66-33c3-49fe-8cb3-d0046d6b35b7" />

2. Containerul pornit și funcțional:
<img width="1130" height="130" alt="image" src="https://github.com/user-attachments/assets/ed7381c5-8c70-4d48-bc3a-4929e59f686f" />

3. Accesarea aplicației din browser:
<img width="578" height="175" alt="image" src="https://github.com/user-attachments/assets/0333700a-98cc-4803-ba95-a1a19f021113" />

4. Log-urile containerului (Consolă):
<img width="922" height="242" alt="image" src="https://github.com/user-attachments/assets/553101b9-e91a-4d88-ac91-cf006373abe3" />

🚀 Ce urmează?
Integrarea liniei de status în README.md general al grupei de pe ramura main.

Arhivarea și predarea proiectului.
