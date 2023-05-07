import dns.resolver

query = "dnspython.org"

answers = dns.resolver.resolve(query, "A")
for rdata in answers:
    print(rdata)