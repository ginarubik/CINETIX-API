import requests
import json

base_url = 'http://127.0.0.1:5000'

def get_info_by_name(_customer):
    result = requests.get(url=f"{base_url}/User_name/{_customer}",
                          headers={'content-type': 'application/json'})
    return result.json()


#  first client side API end point call, gets age restricted info

def get_age(_age):
    result = requests.get(url=f"{base_url}/age_restrictions/{_age}",
                          headers={'content-type': 'application/json'})
    return result.json()

#  second API call point adds new bookings 

def add_new_booking(title,age,time,price,seat,user):

    booking = {
        "Movie_title": title,
        "Age_restrictions": age,
        "Time": time,
        "Price": price,
        "Seat_number": seat,
        "User_name": user
    }

    result = requests.put(url=f"{base_url}/booking",
                          headers={'content-type': 'application/json'},
                          data=json.dumps(booking))

    return result.json()

def display_booking(records):
    print("{Movie_title},{Time},{Seat_number},{User_name}")



def run():
    print('############################')
    print('Hello, welcome to CINETIX!!')
    print('############################')
    print()
    customer = input('What is your name?')
    print()
    bookings = get_info_by_name(customer)
    print('####### Your order #######')
    print()
    display_booking(bookings)
    print()
    place_booking = input('Would you like to book another showing (y/n)?  ')

    book = place_booking == 'y'


#  sort above first 
    if book:
         customer = input('Enter your name:')
         movie = input('Choose your movie : ')
         time = input('Choose time? : ')
         add_new_booking( movie, time, customer)
         print("Booking is Successful")
         print()
         bookings = add_new_booking()
         display_booking(bookings)

         print()
         print('See you soon!')

if __name__ == '__main__':
    run()

#4.Implement client-side for the 3 API endpoints
#9.In main.py have a run() function/call the functions to simulate the planned interaction with the API, this could include welcome statements, displaying ,etc.(booking example)
