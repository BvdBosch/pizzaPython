import dns.resolver

query = "dnspython.org"
qtype = "A"
nameserver = "1.1.1.1"

resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = [nameserver]
answers = resolver.resolve(query, qtype)
for rdata in answers:
    print(rdata)