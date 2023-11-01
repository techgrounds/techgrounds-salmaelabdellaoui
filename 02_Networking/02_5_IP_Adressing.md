# IP Adressing
IP-adressen, of Internet Protocol-adressen, zijn numerieke identificaties die worden gebruikt om apparaten en computers op een computernetwerk te onderscheiden. Ze zijn essentieel voor het routeren van gegevens over het internet en binnen lokale netwerken. Er zijn twee hoofdversies van IP-adressen: IPv4 (Internet Protocol versie 4) en IPv6 (Internet Protocol versie 6).

## Key-terms 
* __IP adressen:__  
IP-adressen worden gebruikt om bronnen op internet te identificeren, zoals websites, servers en apparaten. Ze bestaan uit netwerkgedeeltes en hostgedeeltes, waarmee routers de beste route kunnen bepalen om gegevens van de bron naar de bestemming te verzenden. IP-adressen zijn essentieel voor de werking van het internet en lokale netwerken, waarbij routers, firewalls en andere netwerkapparatuur zeer efficiënt gebruik maken om gegevensverkeer te beheren en te routeren.
* __IPv4  en IPv6:__  
IPv4 is de oudere versie van IP-adressen en maakt gebruik van een 32-bits notatie, bijvoorbeeld 192.168.1.1. IPv4-adressen zijn vrijwel uitgeput vanwege de groei van internetgebruik en apparaten.  
  
  IPv4 is de nieuwere versie van IP-adressen en gebruikt een 128-bits notatie, bijvoorbeeld 2001:0db8:85a3:0000:0000:8a2e:0370:7334. IPv6 is ontworpen om het tekort aan beschikbare adressen op te lossen en biedt een vrijwel onbeperkte hoeveelheid adressen.
* __Publieke en prive IPS:__  
Publieke IP-adressen en privé IP-adressen zijn twee verschillende soorten IP-adressen die worden gebruikt in computernetwerken.   

  Het belangrijkste verschil tussen publieke en privé IP-adressen is dat publieke adressen wereldwijd uniek zijn en nodig zijn voor communicatie via het openbare internet, terwijl privé adressen worden gebruikt voor lokale communicatie binnen een privénetwerk en kunnen worden hergebruikt op vele locaties wereldwijd.

* __NAT:__  
NAT, of Network Address Translation, is een techniek die wordt gebruikt in netwerken, zoals thuisnetwerken en zakelijke netwerken, om het beheer van IP-adressen te vereenvoudigen en om meerdere apparaten binnen een privénetwerk toegang te geven tot het internet met behulp van een enkel openbaar IP-adres. NAT speelt een cruciale rol bij het omzetten van privé IP-adressen in het openbare IP-adres van de router wanneer gegevenspakketten het lokale netwerk verlaten.  

* __Statische en dynamische adressen:__  
Over het algemeen zijn statische IP-adressen handig voor apparaten die altijd bereikbaar moeten zijn via hetzelfde IP-adres, terwijl dynamische IP-adressen flexibeler zijn en zich aanpassen aan de behoeften van een netwerk met veel apparaten die vaak verbinding maken en verbreken.

## Opdracht  
Ontdek wat je publieke IP adres is van je laptop en mobiel op wifi.
Zijn de adressen hetzelfde of niet? Leg uit waarom.
Ontdek wat je privé IP adres is van je laptop en mobiel op wifi.
Zijn de adressen hetzelfde of niet? Leg uit waarom.
Verander het privé IP adres van je mobiel naar dat van je laptop. Wat gebeurt er dan?
Probeer het privé IP adres van je mobiel te veranderen naar een adres buiten je netwerk. Wat gebeurt er dan?
### Gebruikte bronnen
* https://chat.openai.com    
* https://support.microsoft.com/nl-nl/windows/uw-ip-adres-zoeken-in-windows-f21a9bbc-c582-55cd-35e0-73431160a1b9   
* https://nordvpn.com/nl/what-is-my-ip/#:~:text=Klik%20op%20%27Start%27%20%3E%20%27,naast%20%27IPv4%2Dadres%27. 

### Ervaren problemen
Geen problemen ervaren.

### Resultaat
Mijn publieke IP adres op mijn telefoon is 192.168.178.1 en die van mijn laptop ook. Ze zijn dus beide hetzelfde. Het publieke IP-adres is het IP-adres dat aan jouw thuisnetwerk is toegewezen door jouw internetprovider (ISP). Dit publieke IP-adres is uniek voor de gehele thuisnetwerk en wordt gebruikt om met het bredere internet te communiceren. Alle apparaten in de thuisnetwerk delen dit ene publieke IP-adres wanneer ze via de router verbinding maken met internet.  
  
Mijn prive IP adres van mijn telefoon is: 192.168.178.216 en die van mijn laptop is 192.168.178.240, ze zijn dus niet hetzelfde. Dit heeft te maken met het gebruik van dynamische IP-adressen en het functioneren van een DHCP-server (Dynamic Host Configuration Protocol) in het thuisnetwerk.  
  
Bij het veranderen van de IP adres van mijn mobiel naar die van mijn laptop heb ik de volgende probleem ondervonden:   

Mijn telefoon had verbindingsproblemen. Dit komt doordat er bij de router verwarring kan zijn bij het routeren van verkeer tussen apparaten met hetzelfde IP-adres, waardoor sommige apparaten mogelijk geen verbinding kunnen maken met het netwerk of internet. Dit was dus het geval bij mij.   
  
Bij het veranderen van mij prive IP adres op mijn telefoon met een IP adres van buitenaf, krijg ik dezelfde probleem met mijn internet verbinding als hierboven. 