# Define the function to get hotel details
import http.client
import json
conn = http.client.HTTPSConnection("vgtechdemo.com")


def hoteldetails(searchId, sessionId, rooms, nights, tokenId, productId, hotelId):
    # Create the payload
    payload = f"""{{
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

    # Send the request
    conn.request("POST", "/gopaddiberlin/gopaddiberlinbkend/web/hotels/detail", payload, headers)
    res = conn.getresponse()
    data = res.read()
    response = json.loads(data.decode('utf-8'))

    result = {}

    try:
        # Extract hotel details from the response
        details = response['data'][0]['details'][0]
        result['searchId'] = searchId
        result['hotelName'] = details['hotelName']
        result['images'] = details['images']
        result['description'] = details['description']
        result['rating'] = details['rating']
        result['description1'] = details['roomrate']['description']
        result['roomtype'] = details['roomrate']['roomtype']
        result['netprice'] = details['roomrate']['netprice']
        result['maxOccupancyPerRoom'] = details['roomrate']['maxOccupancyPerRoom']
        result['cancellationPolicy'] = details['cancellationPolicy']
        result['roomImages'] = details['roomrate']['roomImages']
        result['facilities'] = details['roomrate']['facilities']

        return result

    except IndexError:
        return "Hotel details not found"


# Example usage of the function
searchId = "141"
sessionId = "TVRjeE16RTFOVGczTUY4Mk16ZGZNVEE1TGpFNU9TNHhNVE11TXprPV8xMDMzODc0"
rooms = "1"
nights = "1"
tokenId = "CuGqRMtcASphoK1a7YWr"
productId = "trx109"
hotelId = "129956"

# Call the function with the required parameters
hotel_details = hoteldetails(searchId, sessionId, rooms, nights, tokenId, productId, hotelId)
print(hotel_details)
