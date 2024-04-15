from flask import Flask,request
from pprint import pprint
from getdetails import getdetails
from imagelist import imgfinder
#from ages import ageconverter
#from datetime import datetime
#from ratingconverter import starRating
#from timeconverter import convert_date_fromat
app=Flask(__name__)

@app.route('/')
def demo():
    return 'this returns hotel search details'

@app.route('/',methods=['POST'])
def hotelhook():
    req=request.get_json(force=True)
    pprint(req)
    sessionInfo=req['sessionInfo']
    parameters=sessionInfo['parameters']
    searchId=parameters['searchId']
    sessionId=parameters['sessionId']
    rooms=str(parameters['rooms'])
    nights=parameters['nights']
    tokenId=parameters['tokenid']
    productId=parameters['productId']
    hotelId=parameters['hotelId']

#def getdetails(searchId,sessionId,rooms,nights,tokenId,productId,hotelId):

    response=getdetails(searchId,sessionId,rooms,nights,tokenId,productId,hotelId)
    roomrates=response['data'][0]['details'][0]['roomrates']

    response = {
        "fulfillmentResponse": {
            "messages": [
                {
                    "text": {
                        "text": [
                            "Here are the details for you"
                        ]
                    }
                },
                {
                    "responseType": "RESPONSE_TYPE_UNSPECIFIED",
                    "channel": "",
                    "payload": {
                        "botcopy": [
                            {
                                "carousel": [
                                    {
                                        "action": { 
                                      "buttons": [ 
                                        { 
                                          "action": { 
                                            "message": { 
                                              "command": "Book Now", 
                                              "type": "training", 
                                              "parameters": {
                                                    "productId": i["productId"],
                                                    "rateBasisId": i["rateBasisId"],
                                                    "netPrice":i["netPrice"]}
                                            } 
                                          }, 
                                          "title": "Book Now" 
                                        } 
                                      ] 
                                    },
                                        "body": f'''Fair type {i["fareType"]}
                                        Facilites include {', '.join(str(x) for x in i["facilities"])}
Cancellation policy {i["cancellationPolicy"]}''',
                                        "image": {
                                            "alt": "Image of rooms",
                                            "url": imgfinder(i.get("roomImages"))
                                        },
                                        "subtitle": f"""💵 NGN {i['netPrice']}""", 
                                        "title": i["roomType"]
                                    } for i in roomrates
                                ]
                            }
                        ]
                    }
                }
            ]
        }
    }
    return response





    '''sessionInfo=req['sessionInfo']
    parameters=sessionInfo['parameters']
    destination=parameters['destination_city'] if parameters['destination_city'] else parameters['destination2']
    rooms=parameters['rooms']
    nights=parameters['nights']
    startDate=parameters['start-date']
    #startDate=startDate.replace("-","/")
    endDate=parameters['end-date']
    #endDate=endDate.replace("-","/")
    startDate = datetime.strptime(startDate, '%Y-%m-%d')
    endDate = datetime.strptime(endDate, '%Y-%m-%d')
    start = startDate.strftime('%Y/%m/%d')
    end = endDate.strftime('%Y/%m/%d')
    adults=parameters['adults']
    children=parameters['children']
    child_age=parameters['ages']
    child_age=ageconverter(child_age)
    if (children!=0) and (child_age==''):
        for i in range(int(children)):
            child_age.append('7')
    total_people=int(adults)+int(children)


    
#def getdetails(searchId,sessionId,rooms,nights,tokenId,productId,hotelId):


#def SearchHotelList1(city, rooms, nights,startDate, endDate, adults, children, ages):

    response=SearchHotelList2(destination,rooms,nights,start,end,adults,children,child_age)
    if response!='No hotels found':
        searchId,hotel_list=response[0],response[1]
        hotel_list=hotel_list[:7]
        response={
            "fulfillmentResponse":{
                "messages":[
                    {
                        "text":{
                            "text":[
                                f"Click on above options to book!"
                            ]
                        }
                    },
                    {
                        "responseType":"RESPONSE_TYPE_UNSPECIFIED",
                        "channel":"",


                        #Union field message can be only one of the following:
                        "payload":{

                            "botcopy":[
                                {
                                    "carousel": [
                                        {
                                            "action":{
                                                "message":{
                                                    "type":"training",
                                                    "command":"book now",
                                                    "parameters":{
                                                        "searchId":f"\"{searchId}\"",
                                                        "hotelId":i["hotelId"],
                                                        "hotelName":i['hotelName'],
                                                        "hotelRating":i['hotelRating'],
                                                        "locality":i['locality'],
                                                        "nights":i['nights'],
                                                        "rooms":i['rooms'],
                                                        "totalPrice":i['totalPrice']
                                                    }
                                                }
                                            },
                                            "body":f"{starRating(i['hotelRating'])}",
                                            "image":{
                                                "alt":"Image of Activity",
                                                "url":i['image']
                                            },
                                            "subtitle":f"NGN {i['totalPrice']}",
                                            "title":i['hotelName']
                                        } for i in hotel_list
                                    ]
                                }
                            ]
                        }

                    }
                ]
            }
        }
        
        return response
    else:
        nohotels={
            "fulfillmentResponse":{
                "messages":[
                    {
                        "text":{
                            "text":[
                                f"Sorry! we couldn't find any hotels in {destination} between {start} and {end}."
                            ]
                        }
                    },
                    {
                      "responseType": "RESPONSE_TYPE_UNSPECIFIED",
                      "channel": "",

                      #Union field message can be only one of the following:
                      "payload": {
                              "botcopy": [
                                {
                                  "suggestions": [
                                    {
                                      "action": {
                                        "message": {
                                          "command": "I want to change search details",
                                          "type": "training"
                                        }
                                      },
                                      "title": "Would you like to change search details?"
                                    }
                                  ]
                                }
                              ]
                            }

                    }
                    ]
            }
        }
        return nohotels'''
    

    return ""


if __name__=="__main__":
    app.run(debug=True,port=8080)