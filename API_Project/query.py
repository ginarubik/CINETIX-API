from cinema_utils import Error, get_db_connection, DbConnectionError
from pprint import pprint
from datetime import datetime

# Getting all bookings
def get_bookings():
    try:
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("""
                SELECT Movie_id, Movie_title, Age_restrictions, Time, Price, Seat_number, User_name
                FROM ticket_purchase
                """)
                result = cursor.fetchall()
                for i in range(len(result)):
                    result[i]['Time'] = str(result[i]['Time'])
                pprint(result)
                return result
    except Error as err:
        raise DbConnectionError(f"Failed to read data from DB: {err}")

# get_bookings()


# Finding titles that are 18+ restricted films
def get_over_18():
    try:
        with get_db_connection() as connection:
            with connection.cursor(dictionary=True) as cursor:
                cursor.execute("""
                SELECT Movie_title
                FROM ticket_purchase
                WHERE Age_restrictions = 18
                """)
                result = cursor.fetchall()
                print(result)
                return result
    except Error as err:
        raise DbConnectionError(f"Failed to read data from DB: {err}")

# get_over_18()


#  Creating a new booking for cinema tickets
def add_new_ticket(title, age_restriction, price, seat_number, username):
    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                INSERT INTO ticket_purchase (Movie_title, Age_restrictions, Price, Seat_number, User_name)"""
                """VALUES (%s, %s, %s, %s, %s)
                """, [title, age_restriction, price, seat_number, username])
                connection.commit()
                print("New ticket added!")
    except Error as err:
        raise DbConnectionError(f"Failed to read data from DB: {err}")

# An example to try creating a new booking:
# add_new_ticket("Five nights at Freddy's", 18, 6.99, "14D", "Mary Sue")


# Update customer seat
def change_seat(username, seat):
    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                UPDATE ticket_purchase
                SET Seat_number = %s, Time = %s
                WHERE User_name = %s
                """, [seat, datetime.now(), username])
                connection.commit()
                print(f"Record updated for {username}")
    except Error as err:
        raise DbConnectionError(f"Failed to read data from DB: {err}")

# change_seat("Mary Sue", "7G")


# Delete booking
def delete_booking(username):
    try:
        with get_db_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute("""
                DELETE FROM ticket_purchase
                WHERE User_name = %s
                """, [username])
                connection.commit()
                print(f"Booking deleted for: {username}")
    except Error as err:
        raise DbConnectionError(f"Unable to delete booking: {err}")

# delete_booking("Mary Sue")


# 8. Use appropriate SQL queries to interact with the database in your Flask application, and demonstrate at least two different queries.
