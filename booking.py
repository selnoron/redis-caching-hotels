# parsing
from bs4 import BeautifulSoup
import requests
# time
import datetime


class Hotel: 
    def __init__(
        self,
        id: int,
        name: str,
        price: str
    ) -> None: 
        self.id = id
        self.name = name 
        self.price = price 
 
 
class Booking: 
 
    def __init__( 
        self,
        checkin: datetime, 
        checkout: datetime, 
    ) -> None:
        self.checkin = checkin.strftime('%Y-%m-%d') 
        self.checkout = checkout.strftime('%Y-%m-%d') 
        self.url = ( 
            'https://www.putevka.com/' 
            'hotels/russia/moskva?' 
            'sort=1&id_resort=2395&' 
            f'date={self.checkin}&' 
            f'date_to={self.checkout}&' 
            'adl=2&' 
            'chd=0' 
        ) 
        response = requests.get(self.url) 
        self.html = BeautifulSoup(response.text, 'html.parser') 
 
    def get_info(self) -> list[Hotel]: 
        hotels = self.html.find_all("a", class_="product-title__link") 
        price = self.html.find_all("span", class_="found-price") 
 
        list_hotels: list[Hotel] = [] 
 
        for i in range(len(hotels)): 
            current_name = hotels[i].text.strip() 
            current_price = int(price[i].text.strip()) 
            hotel = Hotel(i, current_name, current_price) 
            list_hotels.append(hotel) 
 
        return list_hotels
    