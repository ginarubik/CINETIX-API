from flask import Flask, jsonify, request
from query import get_bookings, add_new_ticket, change_seat, delete_booking

app = Flask(__name__)


# Get all bookings
@app.route('/')
def all_bookings():
    return jsonify(get_bookings()), 200


# Add a new film booking to the data set
@app.route('/add-booking', methods=["POST"])
def ticket_add():
    new_booking = request.get_json()
    add_new_ticket(new_booking['title'], new_booking['age_restriction'], new_booking['price'],
                   new_booking['seat_number'], new_booking['username'])
    return get_bookings(), 201


# Update the film booking
@app.route('/update-booking/<username>', methods=["PUT"])
def update_booking(username):
    new_data = request.get_json()
    change_seat(username, new_data['seat'])
    return get_bookings()


# Delete the film booking
@app.route('/delete-booking/<username>', methods=["DELETE"])
def delete_film_booking(username):
    delete_booking(username)
    return get_bookings()


if __name__ == '__main__':
    app.run(debug=True, port=8080)

# 2. Implement API endpoints with appropriate functionality
# 3. Implement one additional endpoint of your choice (POST or GET but with a different implementation)
# 10. Have correct but minimal imports per file (do not import things you do not use in the file)
