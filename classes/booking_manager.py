from booking import Booking
from classes.validations import *

class BookingManager:
    def __init__(self, rooms, bookings, pricing_manager):
        self.rooms = rooms
        self.booking = bookings
        self.pricing_manager = pricing_manager

    def create_booking(self, customer_name, room_id, booking_date, start_time, players):
        if not is_str(customer_name):
            return "Invalid name!"
        if not is_room_id_exist(room_id):
            return "Room id doesn't exist!"
        if not check_booking_date(booking_date):
            return "Booking date passed already"
        try:
            datetime.date.strptime(booking_date, "%Y-%m-%d")
            datetime.time.strptime(start_time, "%H:%M")
        except ValueError:
            return "Date or time are invalid"
        date_and_time = datetime.datetime.combine(booking_date, start_time)




