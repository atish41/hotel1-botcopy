#from hotelsearch1 import SearchHotelList1
from pprint import pprint
#from hotelcity import GetHotelCity
from datetime import datetime
from hotelsearch import SearchHotelList2
#city=GetHotelCity("delhi")[0]

#print(city)
# Convert the strings to datetime objects 
start_date = datetime.strptime("2024-04-09", '%Y-%m-%d') 
end_date = datetime.strptime("2024-04-11", '%Y-%m-%d') 
 
# Use strftime to format the dates 
start = start_date.strftime('%Y/%m/%d') 
end = end_date.strftime('%Y/%m/%d') 
 
# Print the formatted dates 
print(start) 
print(end)


searchId,result,_ = SearchHotelList2("Bur Dubai, United Arab Emirates","1","1",start,end,1,1,[9])
pprint(result)
pprint("this is the search id for hotel search",searchId)
#def SearchHotelList1(city, startDate, endDate, adults, children, ages, rooms, nights,room_No):
#city="Bur Dubai, United Arab Emirates"
#rooms="1"
#nights="1"
#startDate="2024/04/07"
#endDate="2024/04/10"
#adults=1
#children=1
#ages=9