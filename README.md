# Electricity Cost Chain Analysis

Analisi dei costi dell’elettricità lungo la filiera di **produzione, consumo e vendita** nei diversi paesi, con l’obiettivo di confrontare dinamiche energetiche e differenze strutturali tra stati.

Progetto sviluppato per il corso di **Fondamenti di Scienza dei Dati**.

---

## Obiettivo del progetto

Lo scopo del progetto è analizzare la relazione tra:
- produzione di energia elettrica,
- consumo di energia elettrica,
- costi e prezzi dell’elettricità (€/kWh),
- impegno delle nazioni nella transizione verso fonti energetiche pulite (green energy)

a livello **europeo**, utilizzando dataset open provenienti da fonti istituzionali.

L’analisi si concentra sulla **catena dei costi dell’elettricità**, osservando come il costo per kWh vari tra le diverse fasi e tra differenti paesi.

---

## Dataset

I dati utilizzati provengono da Ember e sono i seguenti:

1. *Yearly Electricity Data*

   Fonte: Ember – Global Electricity Data (https://ember-energy.org/data/yearly-electricity-data/)
   
   Contiene informazioni annuali sulla produzione, capacità, import/export, domanda e emissioni di energia elettrica per oltre 200 paesi e territori.

2. *European Wholesale Electricity Prices – Monthly*

   Fonte: Ember – European Wholesale Electricity Price Data (https://ember-energy.org/data/european-wholesale-electricity-price-data/)

   Contiene i prezzi mensili all’ingrosso dell’elettricità in Europa (€/MWh), aggregati per paese.

Tutti i dataset sono in formato CSV e vengono preprocessati prima dell’analisi.

---

## Setup dell’ambiente

1. Creare l'ambiente virtuale:

```python
python setup.py
```

2. Avviare Jupyter Lab:

```python
python start_jupyter_lab.py
```

---

## Stato del progetto

Il progetto è in fase di sviluppo.
Le prossime fasi includono:
- raccolta e pulizia dei dataset,
- integrazione dei dati per paese e anno

---

## Autore

Lorenzo Londero