import http.client
import json
from pprint import pprint

conn = http.client.HTTPSConnection("vgtechdemo.com")

#payload = "{\"searchId\":\"143\",\"sessionId\":\"TVRjeE16RTJNVEE0TjE4ME1EZGZNVEE1TGpFNU9TNHhNVE11TXprPV8xMDMzOTAw\",\"rooms\":\"1\",\"nights\":\"1\",\"tokenId\":\"FWZVozv2l8OJmtwYDgeK\",\"productId\":\"trx109\",\"hotelId\":\"129956\"}"
'''searchId="143"
sessionId="TVRjeE16RTJNVEE0TjE4ME1EZGZNVEE1TGpFNU9TNHhNVE11TXprPV8xMDMzOTAw"
rooms="1"
nights="1"
tokenId="FWZVozv2l8OJmtwYDgeK"
productId="trx109"
hotelId="129956" '''

def getdetails(searchId,sessionId,rooms,nights,tokenId,productId,hotelId):

    payload=f"""{{
            "searchId":"{searchId}",
            "sessionId":"{sessionId}",
            "rooms":"{rooms}",
            "nights":"{nights}",
            "tokenId":"{tokenId}",
            "productId":"{productId}",
            "hotelId":"{hotelId}"
        }}"""



    headers = {
        'Token': "gopaddi@v1",
        'Userid': "10"
        }

    conn.request("POST", "/gopaddiberlin/gopaddiberlinbkend/web/hotels/detail", payload, headers)

    res = conn.getresponse()
    data = res.read()

    #print(data.decode("utf-8"))
    response=json.loads(data.decode("utf-8"))

    return response

#hotel_get_details=response[0]

'''if response['data']:
    hotel_get_details=response[0]
else:
    print("no data found in resposen['data']list")'''
#pprint(response)

#getinfo=getdetails("143","TVRjeE16RTJNVEE0TjE4ME1EZGZNVEE1TGpFNU9TNHhNVE11TXprPV8xMDMzOTAw","1","1","FWZVozv2l8OJmtwYDgeK","trx109","129956")
#pprint(getinfo)