import dns.resolver

def dns_query(query, qtype, nameserver):
    resolver = dns.resolver.Resolver(configure=False)
    resolver.nameservers = [nameserver]
    answers = resolver.resolve(query, qtype)
    for rdata in answers:
        print(rdata)

dns_query(query="dnspython.org", qtype = "A", nameserver = "1.1.1.1")