import requests



def check():
    url = "http://master.versionoms.yunwms.com/default/svc/web-service"

    payload = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<SOAP-ENV:Envelope xmlns:SOAP-ENV=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:ns1=\"http://www.example.org/Ec/\">\n    <SOAP-ENV:Body>\n        <ns1:callService>\n            <paramsJson>\n                {\n                    \"pageSize\":\"2\",\n                    \"page\":1\n                }\n            </paramsJson>\n            <appToken>cbd534ca9f15aa992b9f6f1bc0296613</appToken>\n            <appKey>781133391fe6a3947617e4056b1ba54c</appKey>\n            <service>getWarehouse</service>\n        </ns1:callService>\n    </SOAP-ENV:Body>\n</SOAP-ENV:Envelope>"
    headers = {
      'Content-Type': 'text/xml; charset=utf-8',
      'SOAPAction': '"callService"',
      'Cookie': 'PHPSESSID=66dmi38cti8mt5hioeu9i7srms'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)


def check2():
    print("hello world!")

if __name__ == '__main__':
    check2()