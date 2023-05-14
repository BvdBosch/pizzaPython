import requests
import configparser

config = configparser.ConfigParser()
config.read('example.ini')

# https://docs.greynoise.io/docs/using-the-greynoise-community-api
def checkGraynoise(ip):
    url = config['GREYNOISE']['BaseUrl'] + ip

    # Greynoise allows anonymouse lookups
    if config['GREYNOISE']['ApiKey']:
        headers = {
        'key': '{{' + config['GREYNOISE']['ApiKey'] + '}}'
        }
        return requests.request("GET", url, headers=headers)
    else:
        return requests.request("GET", url)


print(checkGraynoise('51.91.185.74').text)