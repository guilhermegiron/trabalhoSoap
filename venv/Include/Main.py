from suds.client import Client
import requests

## Trazer o prefixo de telefone do Brasil Por Isso Passa a Tag BR
url = "http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso"

# Retorna o Prefixo de Telefone passando Sigla BR (Brasil)
payload = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
            <soap:Envelope xmlns:soap=\"http://schemas.xmlsoap.org/soap/envelope/\">
                <soap:Body>
                    <CountryIntPhoneCode xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
                        <sCountryISOCode>BR</sCountryISOCode>
                    </CountryIntPhoneCode>
                </soap:Body>
            </soap:Envelope>"""


#Retorna a capital do Pais passando Sigla PT
payload2 = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
<soap12:Envelope xmlns:soap12=\"http://www.w3.org/2003/05/soap-envelope\">
  <soap12:Body>
    <CapitalCity xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
      <sCountryISOCode>PT</sCountryISOCode>
    </CapitalCity>
  </soap12:Body>
</soap12:Envelope>
"""

#Lista todos os Paises
payload3 = """<?xml version=\"1.0\" encoding=\"utf-8\"?>
<soap12:Envelope xmlns:soap12=\"http://www.w3.org/2003/05/soap-envelope\">
  <soap12:Body>
    <ListOfCountryNamesByName xmlns=\"http://www.oorsprong.org/websamples.countryinfo\">
    </ListOfCountryNamesByName>
  </soap12:Body>
</soap12:Envelope>
"""

# headers
headers = {
    'Content-Type': 'text/xml; charset=utf-8'
}


# Requisicoes
response = requests.request("POST", url, headers=headers, data=payload)
response2 = requests.request("POST", url, headers=headers, data=payload2)
response3 = requests.request("POST", url, headers=headers, data=payload3)


# print da requisicao 1
print(response.text)

# print da requisicao 2
print(response2.text)

# print da requisicao 3
print(response3.text)