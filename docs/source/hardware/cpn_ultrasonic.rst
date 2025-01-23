    Ciao, benvenuto nella Community SunFounder Raspberry Pi & Arduino & ESP32 su Facebook! Esplora a fondo Raspberry Pi, Arduino ed ESP32 insieme ad altri appassionati.

    **Perché unirti a noi?**

    - **Supporto esperto**: Risolvi problemi post-vendita e sfide tecniche con l'aiuto della nostra community e del nostro team.
    - **Impara e condividi**: Scambia suggerimenti e tutorial per migliorare le tue competenze.
    - **Anteprime esclusive**: Accedi in anteprima agli annunci di nuovi prodotti.
    - **Sconti speciali**: Approfitta di sconti esclusivi sui nostri prodotti più recenti.
    - **Promozioni festive e giveaway**: Partecipa a concorsi e promozioni speciali.

    👉 Sei pronto a esplorare e creare con noi? Clicca [|link_sf_facebook|] e unisciti subito!

Modulo Ultrasonico
================================

.. image:: img/ultrasonic_pic.png
  :width: 400
  :align: center

* **TRIG**: Ingresso impulso di attivazione
* **ECHO**: Uscita impulso di eco
* **GND**: Massa
* **VCC**: Alimentazione 5V

Questo è il sensore di distanza ultrasonico HC-SR04, che offre una misurazione senza contatto da 2 cm a 400 cm con una precisione fino a 3 mm. Il modulo include un trasmettitore ultrasonico, un ricevitore e un circuito di controllo.

Basta collegare 4 pin: VCC (alimentazione), Trig (attivazione), Echo (ricezione) e GND (massa) per utilizzarlo facilmente nei tuoi progetti di misurazione.

**Caratteristiche**

* Tensione di lavoro: DC5V
* Corrente di lavoro: 16mA
* Frequenza di lavoro: 40Hz
* Gamma massima: 500cm
* Gamma minima: 2cm
* Segnale di ingresso trigger: impulso TTL di 10uS
* Segnale di uscita eco: segnale di livello TTL proporzionale alla distanza
* Connettore: XH2.54-4P
* Dimensioni: 46x20.5x15 mm

**Principio**

I principi di base sono i seguenti:

* Usa IO per attivare un segnale di livello alto di almeno 10us.
* Il modulo invia un burst di ultrasuoni di 8 cicli a 40 kHz e rileva se viene ricevuto un segnale di impulso.
* Echo emetterà un livello alto se un segnale viene restituito; la durata del livello alto è il tempo dall'emissione al ritorno.
* Distanza = (tempo di livello alto x velocità del suono (340 m/s)) / 2

    .. image:: img/ultrasonic_prin.jpg
        :width: 800

Formula: 

* us / 58 = distanza in centimetri
* us / 148 = distanza in pollici
* distanza = tempo di livello alto x velocità (340 m/s) / 2

**Note Applicative**

* Questo modulo non dovrebbe essere collegato mentre è alimentato. Se necessario, connettere prima il GND del modulo. In caso contrario, il funzionamento del modulo potrebbe essere compromesso.
* L'area dell'oggetto da misurare dovrebbe essere di almeno 0,5 metri quadrati e il più piatta possibile. In caso contrario, i risultati potrebbero essere influenzati.
