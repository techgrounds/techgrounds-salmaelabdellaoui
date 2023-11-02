# Network Detection
Netwerkdetectie met behulp van nmap en Wireshark zijn twee verschillende benaderingen voor het analyseren van een netwerk:

__Nmap (Network Mapper):__  

* Functie: Nmap is een krachtige netwerkscanner die wordt gebruikt om hosts en services in een netwerk te ontdekken en te analyseren.
* Werkwijze: Het scant het netwerk op basis van opgegeven doelen en poorten om te achterhalen welke hosts en services actief zijn.
* Gebruik: Het wordt vaak gebruikt voor netwerkdetectie, beveiligingsevaluaties en systeembeheer.  

__Wireshark:__  

* Functie: Wireshark is een netwerkprotocolanalyzer waarmee je netwerkverkeer kunt vastleggen en analyseren.
* Werkwijze: Het "luistert" naar het netwerkverkeer en ontleedt de pakketten om inzicht te bieden in de communicatie tussen apparaten en de gebruikte protocollen.
* Gebruik: Het wordt vaak gebruikt om netwerkproblemen op te lossen, beveiligingslekken op te sporen en de communicatie tussen apparaten te begrijpen.  

Beide tools zijn waardevol voor netwerkanalyse, maar ze hebben verschillende toepassingen. Nmap wordt vooral gebruikt om hostinformatie en open poorten te ontdekken, terwijl Wireshark dieper in het netwerkverkeer duikt om de communicatie tussen apparaten te begrijpen. Ze vullen elkaar aan om een uitgebreider beeld van een netwerk te geven.

## Key-terms
__Nmap (Network Mapper):__   
NMap staat voor “Network MAPper” en is een opensource netwerkscanner. NMap is van origine gemaakt als poortscanner voor Linux systemen.  
  
Nmap wordt vaak gebruikt voor:

* Het identificeren van open poorten
* Netwerk inventarisatie en network mapping
* Security testing van network devices zoals firewalls
* Identificeren van nieuwe servers
* Vinden van vulnerabilities in het netwerk  
  
NMap kan IP adressen, ranges en hostnames scannen
NMap kan overweg met IPv4 en IPv6, NMap kan (vooral v.a. versie 7) gebruikt worden om DOS aanvallen te lancerenen en NMap kan doelcomputers exploiten. 


## Opdracht  
  
Open Wireshark op je Windows/MacOS-machine. Analyseer wat er gebeurt wanneer je een internetbrowser opent. (Tip: je zult merken dat Zoom voortdurend pakketten over het netwerk verzendt. Je kunt Zoom gedurende een minuut uitschakelen of op zoek gaan naar de pakketten die door de browser worden verzonden tussen de pakketten die door Zoom worden verzonden.)  

### Gebruikte bronnen
* https://nl.wikipedia.org/wiki/Nmap   
* https://jarnobaselier.nl/nmap-commandos-en-scripts/   
* https://chat.openai.com  

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
Om met Nmap te werken moet het eerst gedownload worden mijn VM linux. Door middel van de volgende commando's kan je het downloaden:

```
sudo apt update
sudo apt install nmap
```  
