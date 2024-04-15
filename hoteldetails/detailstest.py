#from hoteldetails import hoteldetails
#from test1 import hoteldetails1
from pprint import pprint
#from hotelsearch import SearchHotelList2
from datetime import datetime

from getdetails import getdetails

start_date = datetime.strptime("2024-04-09", '%Y-%m-%d') 
end_date = datetime.strptime("2024-04-11", '%Y-%m-%d') 
 
# Use strftime to format the dates 
# start = start_date.strftime('%Y/%m/%d') 
# end = end_date.strftime('%Y/%m/%d') 
 
# # Print the formatted dates 
# print(start) 
# print(end)

#def hoteldetails(searchId,sessionId,rooms,nights,tokenId,productId,hotelId):

#searchId= SearchHotelList2("Bur Dubai, United Arab Emirates","1","1",start,end,1,1,[9])[0]
hotelInfo=getdetails("145","TVRjeE16RTJOREkzTlY4ME5qZGZNVEE1TGpFNU9TNHhNVE11TXprPV8xMDMzOTE2","1","1","UZwI6Lm5f3QlV4PWDzR7","trx109","663949")
pprint(hotelInfo)