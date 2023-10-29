# Processes
Processen in Linux kunnen worden onderverdeeld in drie categorieën: Daemons (achtergrondprocessen), Services (diensten) en Programma's.

Een daemon draait op de achtergrond en is niet-interactief. Een dienst reageert op verzoeken van programma's. Een dienst kan interactief zijn. Een programma wordt uitgevoerd en gebruikt door gebruikers (bijvoorbeeld Vim).

Om verbinding te maken met externe Linux-machines (virtueel of niet), kun je ssh (secure shell) gebruiken. Om deze verbinding met je machine mogelijk te maken, moet je de ssh-dienst starten door de ssh-daemon te starten. Voordat ssh er was, was er telnet, wat in feite hetzelfde doet, behalve dat de verbinding niet versleuteld is, dus het is niet veilig. In deze oefening zullen we telnet gebruiken om onze ssh-verbinding niet te verstoren, maar het wordt niet aanbevolen voor gebruik.

Een proces is een exemplaar van draaiende code. Alle code is ergens in bestanden opgeslagen op het systeem. Om deze bestanden te vinden, kijkt Linux in de $PATH-variabele (meer hierover in een latere oefening). Elk proces heeft zijn eigen PID (Process ID, proces-ID-nummer).

## Key-terms
* __Daemons | Telnet:__  
Een "telnet daemon" in een Linux-terminal verwijst naar een dienst of programma dat de Telnet-communicatieprotocol implementeert en toegang biedt tot een systeem via het Telnet-protocol. Telnet is een oud netwerkprotocol dat wordt gebruikt voor externe toegang tot computers en servers via een opdrachtregelinterface. Een "daemon" in dit verband is een achtergrondproces dat draait en wacht op inkomende Telnet-verbindingsverzoeken.  
  
  Doormiddel van de volgende commands te gebruiken kan je de telnet Daemon instaleren, enabelen, starten en de status ervan checken:   
    
   ```
   Commando: sudo apt install inetutils-inetd
   ```   
   ```
   Commando: sudo systemct1 enable inetutils-inetd
   ```   
   ```
   Commando: sudo systemct1 start inetutils-inetd
   ```   
   ```
   Commando: sudo systemct1 status inetutils-inetd
   ```     
   Het opvragen van de PID (process ID) van de telnet kan uitgelezen worden middels het gebruik van de status commando.  
     
     Om alle actieve programma's aan te tonen kan er gebruik worden gemaakt van de volgende commando (daar vind je tevens de PID ook):   
     ```
   Commando: ps auxf
   ```   
   Om heel specifiek 1 programma aan te tonen en de PID ervan op te vragen kan er gebruik worden gemaakt van de volgende commando:   
   ```
   Commando: ps aux | grep <programma>
   ```  
   Om de memory van de programma te achterhalen kan je gebruik maken van de volgende commando: 
  
  ```
   Commando: top -p <PID>
   ```    
   Om uiteindelijk het programma te stoppen kan gebruik worden gemaakt van de volgende commando: 

   ```
   Commando: sudo kill <PID>
   ```  

* __Shell:__  
Om te achterhalen in welke shell je werkt kan je de volgende commando gebruiken: 

  ```
   Commando: echo $SHELL
   ```  
* __$PATH variabel:__


## Opdracht  
Start de telnet daemon en kom erachter wat de PID is en hoeveel geheugen die in gebruik neemt. Vervolgens kill je het proces.   

### Gebruikte bronnen
* https://chat.openai.com   
* https://www.scaler.com/topics/linux-process/ 
* https://www.baeldung.com/linux/telnet 

### Ervaren problemen
[Geef een korte beschrijving van de problemen waar je tegenaan bent gelopen met je gevonden oplossing.]

### Resultaat
[Omschrijf hoe je weet dat je opdracht gelukt is (gebruik screenshots waar nodig).]