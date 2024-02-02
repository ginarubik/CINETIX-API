#1.Come up with a unique creative problem or scenario and show real-life expected use of the database
#11.Document how to run your API in a markdown file including editing the config file, any installation requirements up until how to run the code and what is supposed to happen.

Our team built CINETIX, a simple cinema ticket booking system with three main API endpoints: 

1. /age (app.py) 
2. /booking (app.py)
3. /delete-booking (app.py)

Real-Life Use:

The database stores information about movie titles, age restrictions, showtimes, prices, seat numbers and user names. The three API endpoints are for retrieving movie showings by age restrictions, adding new bookings, and updating existing bookings.

Use Scenario of Database:

In the SQL schema the ticket_purchase table stores information about movie showings. Each row represents a booked ticket with details: movie title, age restrictions, showtime, price, seat number and the booker user's name.

Database Connection and Utility:

The cinema_config module contains configuration information for connecting to the MySQL database.
The cinema_utils module includes utility functions for connecting to the database, handling exceptions, and executing SQL queries.

How to Run the API:

Python and Flask packages need to be installed.
Configure the database connection by editing the cinema_config.py file with your database credentials.
Create the MySQL database named "Movies" and the ticket_purchase table as described in the schema provided.
Run the Flask application using app.py. This will start the API server on port 5000.
You can then use the main.py script to interact with the API. This script allows users to view available movie showings, make new bookings, and potentially update or delete existing bookings.

Unique Problem:

There are some issues and missing parts in the provided code, such as the /update-booking and /delete-booking endpoints, and incomplete functionality in main.py. These can be further developped and tested to handle errors and exceptions.
