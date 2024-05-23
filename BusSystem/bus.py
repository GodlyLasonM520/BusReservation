import streamlit as st
from pymongo import MongoClient

# MongoDB connection details
MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "bus_ticket_booking_db"

# Backend: MongoDB Operations
class BusTicketDB:
    def __init__(self, uri, db_name):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        self.bookings_collection = self.db['bookings']
        self.buses_collection = self.db['buses']

    def book_ticket(self, name, bus_number, departure, destination, date):
        booking = {
            "name": name,
            "bus_number": bus_number,
            "departure": departure,
            "destination": destination,
            "date": date
        }
        self.bookings_collection.insert_one(booking)

    def get_bookings(self):
        return list(self.bookings_collection.find())

    def delete_booking(self, bus_number):
        self.bookings_collection.delete_one({"bus_number": bus_number})

    def add_bus(self, bus_number, departure, destination, date):
        bus = {
            "bus_number": bus_number,
            "departure": departure,
            "destination": destination,
            "date": date
        }
        self.buses_collection.insert_one(bus)

    def get_buses(self):
        return list(self.buses_collection.find())
# Initialize database connection
db = BusTicketDB(MONGO_URI, DB_NAME)

st.title("Bus Ticket Booking System")

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Admin", "User"])

if page == "Admin":
    st.header("Admin Page")
    
    # Form to add a bus
    st.subheader("Add a Bus")
    bus_number = st.text_input("Bus Number")
    departure = st.text_input("Departure")
    destination = st.text_input("Destination")
    date = st.date_input("Date")

    if st.button("Add Bus"):
        db.add_bus(bus_number, departure, destination, date.strftime("%Y-%m-%d"))
        st.success("Bus added successfully")

    # Display all buses
    st.subheader("View Buses")

    if st.button("Show Buses"):
        buses = db.get_buses()
        if buses:
            for bus in buses:
                st.write(f"Bus Number: {bus['bus_number']}, Departure: {bus['departure']}, Destination: {bus['destination']}, Date: {bus['date']}")
        else:
            st.write("No buses found.")

elif page == "User":
    st.header("User Page")

    # Form to book a ticket
    st.subheader("Book a Ticket")
    name = st.text_input("Name")
    bus_number = st.selectbox("Bus Number", [bus['bus_number'] for bus in db.get_buses()])
    departure = st.text_input("Departure")
    destination = st.text_input("Destination")
    date = st.date_input("Date")

    if st.button("Book Ticket"):
        db.book_ticket(name, bus_number, departure, destination, date.strftime("%Y-%m-%d"))
        st.success("Ticket booked successfully")

    # Display all bookings
    st.subheader("View Bookings")

    if st.button("Show Bookings"):
        bookings = db.get_bookings()
        if bookings:
            for booking in bookings:
                st.write(f"ID: {booking['_id']} - Name: {booking['name']}, Bus Number: {booking['bus_number']}, Departure: {booking['departure']}, Destination: {booking['destination']}, Date: {booking['date']}")
        else:
            st.write("No bookings found.")

    # Delete a booking
    st.subheader("Delete Booking")
    delete_bus_number = st.text_input("Bus Number to Delete Booking")

    if st.button("Delete Booking"):
        try:
            db.delete_booking(delete_bus_number)
            st.success("Booking deleted successfully")
        except Exception as e:
            st.error(f"Error: {e}")