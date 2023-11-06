# I. Simple bs program

Première partie pour mettre en place un environnement fonctionnel et deux programmes simples qui discutent à travers le réseau.

- [I. Simple bs program](#i-simple-bs-program)
    - [1. First steps](#1-first-steps)
    - [2. User friendly](#2-user-friendly)
    - [3. You say client I hear control](#3-you-say-client-i-hear-control)

## 1. First steps

🌞 **`bs_server_I1.py`**

[Fichier ici](./bs_server_I1.py)

🌞 **`bs_client_I1.py`**

[Fichier ici](./bs_client_I1.py)

🌞 **Commandes...**

```bash
[wiibleyde@bs-server TP4]$ python3 bs_server_I1.py 
Meooooo !
```

```bash
[wiibleyde@bs-client TP4]$ python3 bs_client_I1.py
Meooooo !
```

```bash
[wiibleyde@bs-server ~]$ ss -tupnl | grep 13337
tcp   LISTEN 0      1          10.1.1.10:13337      0.0.0.0:*    users:(("python3",pid=2083,fd=3))
```
## 2. User friendly

🌞 **`bs_client_I2.py`**

[Fichier ici](./bs_client_I2.py)

🌞 **`bs_server_I2.py`**

[Fichier ici](./bs_server_I2.py)

## 3. You say client I hear control

🌞 **`bs_client_I3.py`**

[Fichier ici](./bs_client_I3.py)