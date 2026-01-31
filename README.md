# Python Leeromgeving - GitHub Codespaces

Welkom bij de Python programmeeromgeving! Deze repository is speciaal ingericht om leerlingen te helpen met het leren programmeren in Python met behulp van GitHub Codespaces.

## Voor Leerlingen

### Aan de slag

1. **Open de Codespace**
   - Klik op de groene knop "Code" bovenaan deze pagina
   - Selecteer het tabblad "Codespaces"
   - Klik op "Create codespace on main" (of de actieve branch)
   - Wacht tot de omgeving is geladen (dit kan een paar minuten duren)

2. **Je eerste programma**
   - Open het bestand `voorbeeld.py` om voorbeelden te bekijken
   - Klik met de rechtermuisknop op het bestand en kies "Run Python File in Terminal"
   - Of gebruik de sneltoets: druk op `F5`

3. **Oefeningen maken**
   - Open `oefeningen.py` om te beginnen met programmeren
   - Vul de functies aan waar `# TODO: Schrijf hier je code` staat
   - Test je oplossingen door het bestand uit te voeren

### Bestanden in deze repository

- `voorbeeld.py` - Voorbeeldcode om Python te leren
- `oefeningen.py` - Oefeningen om zelf te maken
- `oplossingen.py` - Oplossingen voor de oefeningen (alleen voor docenten)

### Tips

- Gebruik de terminal onderaan het scherm om Python code uit te voeren
- Druk op `Ctrl+Space` voor code suggesties
- Als je vast zit, vraag dan hulp aan je docent
- Sla je werk regelmatig op met `Ctrl+S`

## Voor Docenten

### Codespace configuratie

Deze repository is geconfigureerd met:
- **Python 3.11** als standaard Python versie
- **VS Code extensies**:
  - Python (officiële Microsoft extensie)
  - Pylance (taalserver voor Python)
  - Black Formatter (code formatting)
  - Jupyter (voor notebooks)
  - GitHub Copilot (AI code assistent)
  - Python Extension Pack
  - IntelliCode

- **Automatisch geïnstalleerde packages**:
  - pylint (code linting)
  - black (code formatting)
  - pytest (unit testing)
  - ipython (interactieve Python shell)
  - numpy, pandas, matplotlib (data science libraries)

### De configuratie aanpassen

De Codespace configuratie staat in `.devcontainer/devcontainer.json`. Je kunt deze aanpassen om:
- Extra Python packages toe te voegen
- Andere VS Code extensies te installeren
- Instellingen te wijzigen

### Extra oefeningen toevoegen

Je kunt eenvoudig nieuwe Python bestanden toevoegen voor meer oefeningen. Gebruik dezelfde structuur als `oefeningen.py` met duidelijke docstrings en TODO commentaar.

## Licentie

Deze repository is vrij te gebruiken voor educatieve doeleinden.
