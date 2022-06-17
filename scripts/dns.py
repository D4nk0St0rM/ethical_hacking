#!/bin/python3
sudo pip3 install dnspython 
import dns.zone
import dns.resolver

ns_servers = []
def dns_zone_xfer(address):
    ns_answer = dns.resolver.query(address, 'NS')
    for server in ns_answer:
        print("[*] Found NS: {}".format(server))
        ip_answer = dns.resolver.query(server.target, 'A')
        for ip in ip_answer:
            print("[*] IP for {} is {}".format(server, ip))
            try:
                zone = dns.zone.from_xfr(dns.query.xfr(str(ip), address))
                for host in zone:
                    print("[*] Found Host: {}".format(host))
            except Exception as e:
                print("[*] NS {} refused zone transfer!".format(server))
                continue

dns_zone_xfer('megacorpone.com')