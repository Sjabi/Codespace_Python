# Docenten Handleiding - Python Codespace

## Overzicht

Deze repository is volledig geconfigureerd als een GitHub Codespace voor het onderwijzen van Python programmeren aan leerlingen. Wanneer een leerling een Codespace opent, krijgen ze automatisch een volledig ingerichte Python ontwikkelomgeving.

## Wat is er geïnstalleerd?

### Automatische Installatie
Wanneer een Codespace wordt gestart, worden de volgende packages automatisch geïnstalleerd:
- **pylint** - Voor code kwaliteitscontrole
- **black** - Voor automatische code formatting
- **pytest** - Voor unit testing
- **ipython** - Voor een interactieve Python shell
- **numpy** - Voor numerieke berekeningen
- **pandas** - Voor data analyse
- **matplotlib** - Voor grafieken en visualisaties

### VS Code Extensies
De volgende extensies worden automatisch geïnstalleerd:
- **Python** - De officiële Microsoft Python extensie
- **Pylance** - Geavanceerde taalserver voor Python
- **Black Formatter** - Code formatting
- **Jupyter** - Voor Jupyter notebooks
- **GitHub Copilot** - AI code assistent (indien beschikbaar)
- **Python Extension Pack** - Collectie van handige Python tools
- **IntelliCode** - AI-gestuurde code suggesties

## Bestanden voor Leerlingen

### voorbeeld.py
Bevat basisvoorbeelden van Python concepten:
- Print statements
- Variabelen
- Rekenen
- Functies
- Lijsten
- Input (als commentaar)

### oefeningen.py
Oefeningen voor leerlingen om zelf te maken:
- Functie schrijven: tel_op()
- Functie schrijven: is_even()
- Functie schrijven: vind_grootste()
- Functie schrijven: keer_om()

Alle functies hebben duidelijke docstrings en TODO markers waar leerlingen code moeten schrijven.

### snelstart.ipynb
Een interactief Jupyter notebook met:
- Stapsgewijze introductie tot Python
- Uitvoerbare code cellen
- Oefeningen die direct geprobeerd kunnen worden
- Visuele feedback

### oplossingen.py
⚠️ **Alleen voor docenten!**
- Bevat de uitgewerkte oplossingen voor alle oefeningen
- Inclusief unit tests die automatisch controleren of de oplossingen correct zijn
- Kan gebruikt worden als referentie of om leerlingen hints te geven

## De Codespace Aanpassen

### Extra Packages Toevoegen
Bewerk `.devcontainer/devcontainer.json` en voeg packages toe aan de `postCreateCommand`:
```json
"postCreateCommand": "pip install --user pylint black pytest ipython numpy pandas matplotlib jouw-package-hier"
```

### Extra VS Code Extensies
Voeg extensies toe aan de `extensions` lijst in `.devcontainer/devcontainer.json`:
```json
"extensions": [
  "ms-python.python",
  ...
  "jouw.extensie.id"
]
```

### Settings Aanpassen
Wijzig VS Code instellingen in de `settings` sectie van `.devcontainer/devcontainer.json`.

Huidige instellingen:
- Auto-save na 1 seconde
- Format on save (met Black)
- Auto-organize imports
- Pylint enabled

## Gebruik in de Klas

### Voor Leerlingen
1. Leerlingen klikken op "Code" → "Codespaces" → "Create codespace"
2. Wacht 2-3 minuten tot de omgeving geladen is
3. Open `snelstart.ipynb` voor een interactieve introductie
4. Of open `voorbeeld.py` en druk F5 om het uit te voeren
5. Begin met oefeningen in `oefeningen.py`

### Tips voor Docenten
- Leerlingen kunnen hun eigen fork maken om wijzigingen op te slaan
- Gebruik "Live Share" extensie om samen te programmeren
- Codespaces zijn gratis voor educatieve accounts
- Leerlingen kunnen maximaal 2 actieve Codespaces hebben (gratis tier)

## Veelgestelde Vragen

**Q: Worden wijzigingen van leerlingen automatisch opgeslagen?**
A: Bestanden worden auto-saved in de Codespace, maar leerlingen moeten zelf committen en pushen naar GitHub om wijzigingen permanent op te slaan.

**Q: Kunnen leerlingen thuis werken?**
A: Ja! Codespaces werkt in elke webbrowser. Geen lokale installatie nodig.

**Q: Hoeveel tijd duurt het opstarten?**
A: Eerste keer: 3-5 minuten. Daarna: 30-60 seconden.

**Q: Kan ik meer oefeningen toevoegen?**
A: Ja, voeg gewoon nieuwe .py bestanden toe met dezelfde structuur als `oefeningen.py`.

**Q: Werkt dit op Chromebooks?**
A: Ja! Codespaces werkt perfect op Chromebooks via de browser.

## Licentie

Deze educatieve repository is vrij te gebruiken en aan te passen voor onderwijsdoeleinden.
