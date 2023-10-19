# TP2 : Environnement virtuel

☀️ Sur node1.lan1.tp1

```bash
[wiibleyde@node1-lan1-tp1 ~]$ ip a
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:14:7e:a7 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.11/24 brd 10.1.1.255 scope global noprefixroute enp0s8
       valid_lft forever preferred_lft forever
    inet6 fe80::a00:27ff:fe14:7ea7/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

```bash
[wiibleyde@node1-lan1-tp1 ~]$ ip r s
default via 255.255.255.0 dev enp0s8 proto static metric 100 
10.1.1.0/24 dev enp0s8 proto kernel scope link src 10.1.1.11 metric 100 
10.1.2.0/24 via 10.1.1.254 dev enp0s8 
255.255.255.0 dev enp0s8 proto static scope link metric 100 
```

```bash
[wiibleyde@node1-lan1-tp1 ~]$ ping 10.1.2.11
PING 10.1.2.11 (10.1.2.11) 56(84) bytes of data.
64 bytes from 10.1.2.11: icmp_seq=1 ttl=63 time=0.448 ms
64 bytes from 10.1.2.11: icmp_seq=2 ttl=63 time=1.17 ms
64 bytes from 10.1.2.11: icmp_seq=3 ttl=63 time=0.645 ms
64 bytes from 10.1.2.11: icmp_seq=4 ttl=63 time=0.465 ms
^C
--- 10.1.2.11 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3099ms
rtt min/avg/max/mdev = 0.448/0.681/1.166/0.290 ms
```

```bash
[wiibleyde@node1-lan1-tp1 ~]$ traceroute 10.1.2.11
traceroute to 10.1.2.11 (10.1.2.11), 30 hops max, 60 byte packets
 1  10.1.1.254 (10.1.1.254)  0.348 ms  0.325 ms  0.317 ms
 2  10.1.2.11 (10.1.2.11)  6137.768 ms !X  6137.762 ms !X  6137.708 ms !X
```

☀️ Sur router.tp1

```bash
[wiibleyde@router-tp1 ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=63 time=258 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=63 time=55.0 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=63 time=200 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=63 time=67.8 ms
^C
--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3003ms
rtt min/avg/max/mdev = 55.004/145.173/257.740/86.327 ms
```

```bash
[wiibleyde@router-tp1 ~]$ ping google.com
PING google.com (172.217.20.206) 56(84) bytes of data.
64 bytes from par10s50-in-f14.1e100.net (172.217.20.206): icmp_seq=1 ttl=63 time=52.7 ms
64 bytes from waw02s08-in-f14.1e100.net (172.217.20.206): icmp_seq=2 ttl=63 time=169 ms
64 bytes from par10s50-in-f14.1e100.net (172.217.20.206): icmp_seq=3 ttl=63 time=278 ms
64 bytes from waw02s08-in-f206.1e100.net (172.217.20.206): icmp_seq=4 ttl=63 time=113 ms
64 bytes from waw02s08-in-f206.1e100.net (172.217.20.206): icmp_seq=5 ttl=63 time=114 ms
^C
--- google.com ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4007ms
rtt min/avg/max/mdev = 52.673/145.260/277.609/75.704 ms
```

☀️ Accès internet LAN1 et LAN2

```bash
[wiibleyde@node2-lan1-tp1 ~]$ ping 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=61 time=279 ms
64 bytes from 8.8.8.8: icmp_seq=2 ttl=61 time=176 ms
64 bytes from 8.8.8.8: icmp_seq=3 ttl=61 time=111 ms
64 bytes from 8.8.8.8: icmp_seq=4 ttl=61 time=51.7 ms
^C
--- 8.8.8.8 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 51.681/154.353/278.541/84.156 ms
```

```bash
[wiibleyde@node2-lan1-tp1 ~]$ ping google.com
PING google.com (172.217.20.174) 56(84) bytes of data.
64 bytes from par10s49-in-f14.1e100.net (172.217.20.174): icmp_seq=1 ttl=61 time=68.7 ms
64 bytes from waw02s07-in-f174.1e100.net (172.217.20.174): icmp_seq=2 ttl=61 time=138 ms
64 bytes from waw02s07-in-f174.1e100.net (172.217.20.174): icmp_seq=3 ttl=61 time=64.2 ms
64 bytes from waw02s07-in-f14.1e100.net (172.217.20.174): icmp_seq=4 ttl=61 time=285 ms
^C
--- google.com ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 7086ms
rtt min/avg/max/mdev = 64.204/138.854/284.955/89.214 ms
```

☀️ Sur dhcp.lan1.tp1

```bash
[wiibleyde@dhcp-lan1-tp1 ~]$ sudo cat /etc/dhcp/dhcpd.conf
#
# DHCP Server Configuration file.
#   see /usr/share/doc/dhcp-server/dhcpd.conf.example
#   see dhcpd.conf(5) man page
#
default-lease-time 900;
max-lease-time 10800;

authoritative;

subnet 10.1.1.0 netmask 255.255.255.0 {
range 10.1.1.100 10.1.1.200;
option routers 10.1.1.254;
option subnet-mask 255.255.255.0;
option domain-name-servers 1.1.1.1;
}
```

```bash
[wiibleyde@dhcp-lan1-tp1 ~]$ sudo systemctl status dhcpd
● dhcpd.service - DHCPv4 Server Daemon
     Loaded: loaded (/usr/lib/systemd/system/dhcpd.service; enabled; preset: disabled)
     Active: active (running) since Thu 2023-10-19 11:03:17 CEST; 1min 52s ago
       Docs: man:dhcpd(8)
             man:dhcpd.conf(5)
   Main PID: 784 (dhcpd)
     Status: "Dispatching packets..."
      Tasks: 1 (limit: 4611)
     Memory: 7.1M
        CPU: 8ms
     CGroup: /system.slice/dhcpd.service
             └─784 /usr/sbin/dhcpd -f -cf /etc/dhcp/dhcpd.conf -user dhcpd -group dhcpd --no-pid

Oct 19 11:03:17 dhcp-lan1-tp1 dhcpd[784]: Config file: /etc/dhcp/dhcpd.conf
Oct 19 11:03:17 dhcp-lan1-tp1 dhcpd[784]: Database file: /var/lib/dhcpd/dhcpd.leases
Oct 19 11:03:17 dhcp-lan1-tp1 dhcpd[784]: PID file: /var/run/dhcpd.pid
Oct 19 11:03:17 dhcp-lan1-tp1 dhcpd[784]: Source compiled to use binary-leases
Oct 19 11:03:17 dhcp-lan1-tp1 dhcpd[784]: Wrote 0 leases to leases file.
Oct 19 11:03:17 dhcp-lan1-tp1 dhcpd[784]: Listening on LPF/enp0s8/08:00:27:0b:6e:0a/10.1.1.0/24
Oct 19 11:03:17 dhcp-lan1-tp1 dhcpd[784]: Sending on   LPF/enp0s8/08:00:27:0b:6e:0a/10.1.1.0/24
Oct 19 11:03:17 dhcp-lan1-tp1 dhcpd[784]: Sending on   Socket/fallback/fallback-net
Oct 19 11:03:17 dhcp-lan1-tp1 dhcpd[784]: Server starting service.
Oct 19 11:03:17 dhcp-lan1-tp1 systemd[1]: Started DHCPv4 Server Daemon.
```

*(commande faite avant le changement de hostname)*
```bash
[wiibleyde@node2-lan1-tp1 ~]$ sudo dnf install dhcp-server -y

[sudo] password for wiibleyde: 
Last metadata expiration check: 2:41:56 ago on Thu Oct 19 08:14:00 2023.
Dependencies resolved.
===================================================================================================================
 Package                    Architecture          Version                              Repository             Size
===================================================================================================================
Installing:
 dhcp-server                x86_64                12:4.4.2-18.b1.el9                   baseos                1.2 M
Installing dependencies:
 dhcp-common                noarch                12:4.4.2-18.b1.el9                   baseos                128 k

Transaction Summary
=================================================================
```

☀️ Sur node1.lan1.tp1

```bash
[wiibleyde@node1-lan1-tp1 ~]$ sudo systemctl restart NetworkManager
[wiibleyde@node1-lan1-tp1 ~]$ ip a 
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host 
       valid_lft forever preferred_lft forever
2: enp0s8: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP group default qlen 1000
    link/ether 08:00:27:14:7e:a7 brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.100/24 brd 10.1.1.255 scope global secondary dynamic noprefixroute enp0s8
       valid_lft 783sec preferred_lft 783sec
    inet6 fe80::a00:27ff:fe14:7ea7/64 scope link noprefixroute 
       valid_lft forever preferred_lft forever
```

```bash
[wiibleyde@node1-lan1-tp1 ~]$ ping 10.1.2.11
PING 10.1.2.11 (10.1.2.11) 56(84) bytes of data.
64 bytes from 10.1.2.11: icmp_seq=1 ttl=63 time=0.660 ms
64 bytes from 10.1.2.11: icmp_seq=2 ttl=63 time=1.29 ms
64 bytes from 10.1.2.11: icmp_seq=3 ttl=63 time=0.499 ms
64 bytes from 10.1.2.11: icmp_seq=4 ttl=63 time=1.06 ms
^C
--- 10.1.2.11 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3077ms
rtt min/avg/max/mdev = 0.499/0.875/1.285/0.311 ms
```

☀️ Sur web.lan2.tp1

```bash
[wiibleyde@web-lan2-tp1 ~]$ cat /var/www/site_null/index.html 
Site nul de ouf
```

```bash
[wiibleyde@web-lan2-tp1 ~]$ sudo systemctl status nginx
[sudo] password for wiibleyde: 
● nginx.service - The nginx HTTP and reverse proxy server
     Loaded: loaded (/usr/lib/systemd/system/nginx.service; enabled; preset: disabled)
     Active: active (running) since Thu 2023-10-19 11:26:48 CEST; 1min 8s ago
    Process: 785 ExecStartPre=/usr/bin/rm -f /run/nginx.pid (code=exited, status=0/SUCCESS)
    Process: 787 ExecStartPre=/usr/sbin/nginx -t (code=exited, status=0/SUCCESS)
    Process: 793 ExecStart=/usr/sbin/nginx (code=exited, status=0/SUCCESS)
   Main PID: 794 (nginx)
      Tasks: 2 (limit: 4611)
     Memory: 3.7M
        CPU: 12ms
     CGroup: /system.slice/nginx.service
             ├─794 "nginx: master process /usr/sbin/nginx"
             └─798 "nginx: worker process"

Oct 19 11:26:48 web-lan2-tp1 systemd[1]: Starting The nginx HTTP and reverse proxy server...
Oct 19 11:26:48 web-lan2-tp1 nginx[787]: nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
Oct 19 11:26:48 web-lan2-tp1 nginx[787]: nginx: configuration file /etc/nginx/nginx.conf test is successful
Oct 19 11:26:48 web-lan2-tp1 systemd[1]: Started The nginx HTTP and reverse proxy server.
```

```bash
[wiibleyde@web-lan2-tp1 ~]$ ss -tupnl | grep 80
tcp   LISTEN 0      511          0.0.0.0:80        0.0.0.0:*          
tcp   LISTEN 0      511             [::]:80           [::]:*    
```

```bash
[wiibleyde@node2-lan2-tp1 ~]$ sudo firewall-cmd --list-all
public (active)
  target: default
  icmp-block-inversion: no
  interfaces: enp0s8
  sources: 
  services: cockpit dhcpv6-client ssh
  ports: 80/tcp
  protocols: 
  forward: yes
  masquerade: no
  forward-ports: 
  source-ports: 
  icmp-blocks: 
  rich rules: 
```

☀️ Sur node1.lan1.tp1

```bash
[wiibleyde@node1-lan1-tp1 ~]$ curl site_nul.tp1
<p>OMG SUPER SITE INTERNET</p>
[wiibleyde@node1-lan1-tp1 ~]$ cat /etc/hosts
127.0.0.1   localhost localhost.localdomain localhost4 localhost4.localdomain4
::1         localhost localhost.localdomain localhost6 localhost6.localdomain6
10.1.2.12   site_nul.tp1
```

```bash
[wiibleyde@node1-lan1-tp1 ~]$ curl site_nul.tp1
<p>OMG SUPER SITE INTERNET</p>
```