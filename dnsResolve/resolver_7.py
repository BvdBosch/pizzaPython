import dns.resolver
import argparse

parser = argparse.ArgumentParser(
    prog="DNS Resolver",
    description="Resolved DNS queries",
    epilog="Nog in te vullen"
)

parser.add_argument("-q", "--query", required=True)
parser.add_argument("-t", "--type", default="A")
parser.add_argument("-ns", "--name-server", default="1.1.1.1")

args = parser.parse_args()

def dns_query(query, qtype, nameserver):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [nameserver]
    answers = resolver.resolve(query, qtype)
    for rdata in answers:
        print(rdata)

dns_query(query=args.query, qtype=args.type, nameserver=args.name_server)