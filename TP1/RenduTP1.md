# TP1 : Maîtrise réseau du poste

- [TP1 : Maîtrise réseau du poste](#tp1--maîtrise-réseau-du-poste)
- [I. Basics](#i-basics)
- [II. Go further](#ii-go-further)
- [III. Le requin](#iii-le-requin)

# I. Basics

☀️ **Carte réseau WiFi**

```
PS C:\Users\natha> ipconfig /all

Carte réseau sans fil Wi-Fi :
   
   Adresse physique . . . . . . . . . . . : 82-30-BF-B6-57-2C
   
```

```
PS C:\Users\natha> ipconfig /all

Carte réseau sans fil Wi-Fi :
   Adresse IPv4. . . . . . . . . . . . . .: 10.33.76.195(préféré)
   
```


(fait sur https://www.site24x7.com/fr/tools/ipv4-sous-reseau-calculatrice.html)
10.33.64.0/20
```
PS C:\Users\natha> ipconfig /all

Carte réseau sans fil Wi-Fi :
    Masque de sous-réseau. . . . . . . . . : 255.255.240.0
```

☀️ **Déso pas déso**

```
10.33.64.0
```

```
10.33.79.255
```

```
4096
```

☀️ **Hostname**

```
PS C:\Users\natha> hostname
NBK-NATHAN
```

☀️ **Passerelle du réseau**

- L'adresse IP de la passerelle du réseau
```
PS C:\Users\natha> ipconfig
Carte réseau sans fil Wi-Fi :

   Passerelle par défaut. . . . . . . . . : 10.33.79.254

```

- L'adresse MAC de la passerelle du réseau
```
PS C:\Users\natha> arp -a 10.33.79.254

Interface : 10.33.76.195 --- 0x16
  Adresse Internet      Adresse physique      Type
  10.33.79.254          7c-5a-1c-d3-d8-d6     dynamique
```

☀️ **Serveur DHCP et DNS**

- l'adresse IP du serveur DHCP qui vous a filé une IP
```
PS C:\Users\natha> ipconfig
Carte réseau sans fil Wi-Fi :
   
   Serveur DHCP . . . . . . . . . . . . . : 10.33.79.254
```
- l'adresse IP du serveur DNS que vous utilisez quand vous allez sur internet

```
PS C:\Users\natha> ipconfig
Carte réseau sans fil Wi-Fi :
   
   Serveurs DNS. . .  . . . . . . . . . . : 8.8.8.8
                                       1.1.1.1
```

---

☀️ **Table de routage**

```
PS C:\Users\natha> netstat -r
    IPv4 Table de routage
    ===========================================================================
    Itinéraires actifs :
    Destination réseau    Masque réseau  Adr. passerelle   Adr. interface Métrique
            0.0.0.0          0.0.0.0     10.33.79.254     10.33.76.195     35
```

# II. Go further

☀️ **Hosts ?**
```
PS C:\Users\natha> ping b2.hello.vous

Envoi d’une requête 'ping' sur b2.hello.vous [1.1.1.1] avec 32 octets de données :
Réponse de 1.1.1.1 : octets=32 temps=14 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=15 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=11 ms TTL=57
Réponse de 1.1.1.1 : octets=32 temps=11 ms TTL=57

Statistiques Ping pour 1.1.1.1:
    Paquets : envoyés = 4, reçus = 4, perdus = 0 (perte 0%),
Durée approximative des boucles en millisecondes :
    Minimum = 11ms, Maximum = 15ms, Moyenne = 12ms
```

☀️ **Go mater une vidéo youtube et déterminer, pendant qu'elle tourne...**
```
PS C:\Users\natha> netstat -a -n -b
 [msedge.exe]
  TCP    192.168.1.28:54537     192.229.221.95:80      TIME_WAIT
  TCP    192.168.1.28:54538     20.223.46.67:443       TIME_WAIT
  TCP    192.168.1.28:54541     13.107.246.42:443      ESTABLISHED
```


- L'adresse IP du serveur auquel vous êtes connectés pour regarder la vidéo

```
13.107.246.42
```

- Le port du serveur auquel vous êtes connectés
```
443
```

- Le port que votre PC a ouvert en local pour se connecter au port du serveur distant

```
54541
```

---

☀️ **Requêtes DNS**

- À quelle adresse IP correspond le nom de domaine `www.ynov.com`
```
PS C:\Users\natha> nslookup www.ynov.com
Serveur :   dns.google
Address:  8.8.8.8

Réponse ne faisant pas autorité :
Nom :    www.ynov.com
Addresses:  2606:4700:20::ac43:4ae2
          2606:4700:20::681a:ae9
          2606:4700:20::681a:be9
          172.67.74.226
          104.26.11.233
          104.26.10.233
```
- à quel nom de domaine correspond l'IP `x`
```
PS C:\Users\natha> nslookup 174.43.238.89
Serveur :   dns.google
Address:  8.8.8.8

Nom :    89.sub-174-43-238.myvzw.com
Address:  174.43.238.89
```

---

☀️ **Hop hop hop**
```
PS C:\Users\natha> tracert www.ynov.com

Détermination de l’itinéraire vers www.ynov.com [104.26.10.233]
avec un maximum de 30 sauts :

  1    <1 ms     8 ms    <1 ms  box [192.168.1.1]
  2     6 ms     5 ms     5 ms  1.57.25.109.rev.sfr.net [109.25.57.1]
  3     6 ms     5 ms     6 ms  97.186.96.84.rev.sfr.net [84.96.186.97]
  4    13 ms    13 ms    13 ms  68.150.6.194.rev.sfr.net [194.6.150.68]
  5    13 ms    13 ms    13 ms  68.150.6.194.rev.sfr.net [194.6.150.68]
  6    13 ms    13 ms    13 ms  141.101.67.48
  7    14 ms    13 ms    14 ms  172.71.124.4
  8    14 ms    14 ms    14 ms  104.26.10.233

Itinéraire déterminé.
```

☀️ **IP publique**
```
PS C:\Users\natha> tracert 8.8.8.8

Détermination de l’itinéraire vers dns.google [8.8.8.8]
avec un maximum de 30 sauts :

  1    <1 ms    <1 ms    <1 ms  box [192.168.1.1]
```

☀️ **Scan réseau**
```
PS C:\Users\natha> arp -a

Interface : 192.168.1.28 --- 0x8
  Adresse Internet      Adresse physique      Type
  192.168.1.1           e4-5d-51-cd-01-f0     dynamique
  192.168.1.255         ff-ff-ff-ff-ff-ff     statique
  224.0.0.2             01-00-5e-00-00-02     statique
  224.0.0.22            01-00-5e-00-00-16     statique
  224.0.0.251           01-00-5e-00-00-fb     statique
  224.0.0.252           01-00-5e-00-00-fc     statique
  239.255.255.250       01-00-5e-7f-ff-fa     statique
  255.255.255.255       ff-ff-ff-ff-ff-ff     statique
```

# III. Le requin

☀️ **Capture ARP**
- [ARP.pcap](./captures/arp.pcap)

☀️ **Capture DNS**
- [DNS.pcap](./captures/dns.pcap)

☀️ **Capture TCP**
- [TP.pcap](./captures/tcp.pcap)
