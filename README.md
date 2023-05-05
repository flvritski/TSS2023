# TSS2023
## Proiect pentru cursul "Testarea Sistemelor Software"
## Profesor: Prof. dr. ing. Predut Sorina
## Student: Stefan Florin-Viorel-Dan
## Anul 4, 2023

### Repository structure:
`-array_manipulation`: Vom folosi doar `main.py` la coverage run. Singura ramasa importanta este `test.py` ce contine clasa cu testele pentru `partitionarea echivalenta` (class equivalencePartitioning(unittest.TestCase):
`-src`: Main folder. Aici avem programul de baa impreuna cu toate suitele de teste (e.g boundary analysis separat, iar test.py ce contine boundary analysis + equivalence partioning)

### /src directory
#### `a_m.py` : Fisierul "main". 
#### `test.py` : Fisierul cu suita de teste.

### Generare de mutanti
$ mut.py --target src/a_m.py --unit-test src/test.py -m (flagul `-m` optional (desi recomandat) in caz ca dorim si log-urile in generarea de mutanti)

### Coverage
`$ coverage run array_manipulation/main.py ; coverage html -i` (`html -i` pentru a obtine si o pagina in HTML cu raportul final obtinut)
`$ coverage run array_manipulation/test.py ; coverage html -i`

### Branch Coverage
`$ coverage run --branch array_manipulation/main.py ; coverage html -i` (flagul `--branch` pentru a vedea si la nivel de ramuri coverage report-ul)
`$ coverage run --branch array_manipulation/test.py ; coverage html -i`
