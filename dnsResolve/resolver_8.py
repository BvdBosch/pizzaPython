import dns.resolver
import argparse

parser = argparse.ArgumentParser(
    prog="DNS Resolver",
    description="Resolves DNS queries",
    epilog="Nog in te vullen"
)

parser.add_argument("-q", "--query", required=True, help="The domain you want to resolve")
parser.add_argument("-t", "--type", default="A", help="The record type you want resolve, deafults to A")
parser.add_argument("-ns", "--name-server", default="1.1.1.1", help="The nameserver you wan to use to resolve against. Needs to be an IP address, defaults to 1.1.1.1")
parser.add_argument("-ans", "--use-auth-ns", action="store_true", help="Set this options to resolve against an authorative name server for the specified domain. Resolves this nameserver against the name server specified in the ns option.")

args = parser.parse_args()

def get_soa(query, nameserver):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [nameserver]
    return str(resolver.resolve(query, "SOA")[0].mname)[:-1]

def dns_query(query, qtype, nameserver):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [nameserver]
    return resolver.resolve(query, qtype)

def print_respons(response):
    for rdata in response:
        print(rdata)

if args.use_auth_ns:
    soa_nameserver = dns_query(query=get_soa(args.query, args.name_server), qtype="A", nameserver=args.name_server)
    response = dns_query(query=args.query, qtype=args.type, nameserver=str(soa_nameserver[0]))
    print_respons(response)
else:
    print_respons(dns_query(query=args.query, qtype=args.type, nameserver=args.name_server))