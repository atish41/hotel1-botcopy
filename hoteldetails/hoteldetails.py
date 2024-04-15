import http.client
import json
conn = http.client.HTTPSConnection("vgtechdemo.com")


def hoteldetails(searchId,sessionId,rooms,nights,tokenId,productId,hotelId):
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
    response=json.loads(data.decode('utf-8'))

    result={}

    try:
        details=response['data'][0]['details'][0]
        result['searchId']=searchId
        #result['price']=details['price']
        #result['sessionId']=details['sessionId']
        ###result['hotelId']=details['hotelId']
        #result['ratebasisId']=details['ratebasisId']
        #result['netPrice']=details['netPrice']
        result['hotelName']=details['hotelName']
        result['images']=details['images']
        result['description']=details['description']
        result['rating']=details['rating']
        result['description1']=details['roomrate']['description']
        result['roomtype']=details['roomrate']['roomtype']
        result['netprice']=details['roomrate']['netprice']
        result['maxOccupancyPerRoom']=details['roomrate']['maxOccupancyPerRoom']
        result['cancellationPolicy']=details['cancellationPolicy']
        result['roomImages']=details['roomrate']['roomImages']
        result['facilities']=details['roomrate']['facilities']

        return result
    
    except IndexError:
        return "hotel details not found" 


    #print(data.decode("utf-8"))
    '''try:
        details=response['data'][0]['details'][0]
        result['searchId']=searchId
        #result['price']=details['price']
        #result['sessionId']=details['sessionId']
        ###result['hotelId']=details['hotelId']
        #result['ratebasisId']=details['ratebasisId']
        result['netPrice']=details['netPrice']
        result['hotelName']=details['hotelName']
        result['images']=details['images']
        result['description']=details['description']
        result['rating']=details['rating']
        result['description1']=details[0]['description']
        result['roomtype']=details[0]['roomtype']
        result['netprice']=details[0]['netprice']
        result['maxOccupancyPerRoom']=details[0]['maxOccupancyPerRoom']
        result['cancellationPolicy']=details['cancellationPolicy']
        result['roomImages']=details[0]['roomImages']
        result['facilities']=details[0]['facilities']

        return result
    
    except IndexError:
        return "hotel details not found" '''