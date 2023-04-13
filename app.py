# redis 
import redis 
# time 
import time 
import datetime 
# Flask 
import flask 
# local files 
from booking import Booking, Hotel 
# json format
import pickle
 
 
app: flask.app.Flask = flask.Flask(__name__) 
booking = Booking( 
    datetime.datetime(2023, 5, 1), 
    datetime.datetime(2023, 5, 7) 
) 
r = redis.Redis( 
    host='127.0.0.1', 
    port=6379, 
    decode_responses=False
) 
hotel_list: list[Hotel] = booking.get_info()
 
 
@app.route('/') 
def main_page() -> flask.Response: 
    return flask.render_template( 
        'index.html', 
        hotels=hotel_list 
    ) 

@app.route('/<int:id>')
def choosen_hotel_page(id: int) -> flask.Response:
    if not r.get(f'{id}'):
        r.set(f'{id}', pickle.dumps(hotel_list[id]))
    return flask.render_template( 
        'index2.html', 
        hotels=pickle.loads(r.get(f'{id}'))
    ) 
     
 
if __name__ == '__main__': 
    app.run( 
        host='localhost', 
        port=8080, 
        debug=True 
    )