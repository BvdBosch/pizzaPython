import dns.resolver
import argparse

parser = argparse.ArgumentParser(
    prog="DNS Resolver",
    description="Resolved DNS queries",
    epilog="Nog in te vullen"
)

parser.add_argument("-q", "--query", required=True)

args = parser.parse_args()

def dns_query(query, qtype, nameserver):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [nameserver]
    answers = resolver.resolve(query, qtype)
    for rdata in answers:
        print(rdata)

dns_query(query=args.query, qtype = "A", nameserver = "1.1.1.1")