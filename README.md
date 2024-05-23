# Bus Ticket Booking System

This project is a simple bus ticket booking system implemented using Streamlit for the front-end and MongoDB for the back-end. The system allows users to book tickets, view bookings, and delete bookings by bus number. Additionally, there is an admin page for managing buses.

## Features

- **Admin Page**
  - Add new buses
  - View all buses

- **User Page**
  - Book a ticket
  - View all bookings
  - Delete a booking by bus number

## Requirements

- Python 3.7+
- MongoDB

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/bus-ticket-booking-system.git
   cd bus-ticket-booking-system
Install the required Python packages

bash
Copy code
pip install streamlit pymongo
Set up MongoDB

Make sure you have MongoDB installed and running on your local machine. You can download MongoDB from here.

Run the application

bash
Copy code
streamlit run app.py
File Structure
Copy code
.
├── app.py
├── README.md
└── requirements.txt
app.py: The main application file that contains the Streamlit code.
README.md: This readme file.
requirements.txt: List of Python dependencies.
Usage
Admin Page
Add a Bus

Enter the bus number, departure location, destination, and date.
Click the "Add Bus" button to add the bus to the system.
View Buses

Click the "Show Buses" button to display all the buses available in the system.
User Page
Book a Ticket

Enter your name, select a bus number from the dropdown, and provide departure, destination, and date.
Click the "Book Ticket" button to book the ticket.
View Bookings

Click the "Show Bookings" button to display all the bookings made.
Delete a Booking

Enter the bus number for which you want to delete the booking.
Click the "Delete Booking" button to delete the booking.
MongoDB Operations
book_ticket: Adds a new booking to the bookings collection.
get_bookings: Retrieves all bookings from the bookings collection.
delete_booking: Deletes a booking from the bookings collection based on the bus number.
add_bus: Adds a new bus to the buses collection.
get_buses: Retrieves all buses from the buses collection.
