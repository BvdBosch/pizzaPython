import dns.resolver

query = "dnspython.org"
qtype = "A"

answers = dns.resolver.resolve(query, qtype)
for rdata in answers:
    print(rdata)