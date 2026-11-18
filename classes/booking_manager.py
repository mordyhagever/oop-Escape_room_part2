from bisect import insort_left

from booking import Booking
from classes.room import Room
from classes.validations import *
from classes.pricing_manager import PriceManager
import datetime

class BookingManager:
    def __init__(self, rooms, bookings, pricing_manager):
        self.rooms = rooms
        self.booking = bookings
        self.pricing_manager = pricing_manager

    def get_next_id(self):
        all_jsons = DataManager()
        loads = all_jsons.load_bookings()
        if not loads:
            return "R001"
        last_one = loads[-1]
        last_digits = last_one["booking_id"][3:]
        last_digits = int(last_digits)
        next_digit = last_digits + 1
        if next_digit < 10:
            return "B00" + str(next_digit)
        elif 10 < next_digit < 100:
            return "B0" + str(next_digit)
        else:
            return "B" + str(next_digit)


    def create_booking(self, customer_name, room_id, booking_date, start_time, players):
        valid = Validations()
        jsons = DataManager()
        if not valid.is_str(customer_name):
            return "Invalid name!"
        if not valid.is_room_id_exist(room_id):
            return "Room id doesn't exist!"
        try:
            booking_date = datetime.date.strptime(booking_date, "%Y-%m-%d")
            start_time = datetime.time.strptime(start_time, "%H:%M")
        except ValueError:
            return "Date or time are invalid"
        if not valid.check_booking_date(booking_date):
            return "Booking date passed already"
        date_and_time = datetime.datetime.combine(booking_date, start_time)
        if not valid.check_start_time(date_and_time, self.rooms, self.booking, room_id):
            return "Time isn't valid!"
        if not valid.check_players(players, room_id, self.rooms):
            return "Invalid number of players!"
        order = {}
        room = valid.find_room_by_id(room_id)
        calc_price = PriceManager()
        order["booking_id"] = self.get_next_id()
        order["customer_name"] = customer_name
        order["room_id"] = room_id
        order["booking_date"] = datetime.datetime.strftime(date_and_time, "%Y-%m-%d")
        order["start_time"] = datetime.datetime.strftime(date_and_time, "%H:%M")
        order["players"] = players
        order["total_price"] = calc_price.calculate_price(room, players, date_and_time.date())
        order["status"] = "active"
        order["cancellation_fee"] = 0.0
        order1 = order
        order = Booking.from_dict(order)
        self.booking.append(order)
        jsons.save_bookings(self.booking)
        return "Created successfully", order1


    def get_booking(self, booking_id):
        for book in self.booking:
            if book.booking_id == booking_id:
                return book
        return None

    def get_customer_booking(self, customer_name):
        all_customer_orders = []
        for order in self.booking:
            if order.customer_name == customer_name:
                all_customer_orders.append(order)
        if all_customer_orders:
            return all_customer_orders
        return None

    def get_booking_by_date(self, booking_date):
        all_date_orders = []
        for order in self.booking:
            date = datetime.date.strptime(order.booking_date, "%Y-%m-%d")
            if date == booking_date:
                all_date_orders.append(order)
        if all_date_orders:
            return all_date_orders
        return None

    #check_room_availability, i did in Validation class

    def update_booking(self, booking_id, booking_date, start_time, players):
        valid = Validations()
        room_id = None
        if not valid.is_booking_id_exist(booking_id):
            return "Booking id doesn't exist!"
        books = DataManager()
        loads = books.load_bookings()
        for order in loads:
            if order["booking_id"] == booking_id:
                room_id = order["room_id"]
        try:
            booking_date = datetime.date.strptime(booking_date, "%Y-%m-%d")
            start_time = datetime.time.strptime(start_time, "%H:%M")
        except ValueError:
            return "Date or time are invalid"
        if not valid.check_booking_date(booking_date):
            return "Booking date passed already"
        date_and_time = datetime.datetime.combine(booking_date, start_time)
        if not valid.check_start_time(date_and_time, self.rooms, self.booking, room_id, booking_id):
            return "Time isn't valid!"
        if not valid.check_players(players, room_id, self.rooms):
            return "Invalid number of players!"
        found = False
        for order in self.booking:
            if order.booking_id == booking_id:
                order.booking_date = datetime.datetime.strftime(date_and_time, "%Y-%m-%d")
                order.start_time = datetime.datetime.strftime(date_and_time, "%H:%M")
                order.players = players
                order1 = order.to_dict()
                found = True
        if not found:
            return "Couldn't find it"
        DataManager().save_bookings(self.booking)
        return "Updated successfully", order1

    def cancel_booking(self, booking_id, current_datetime):
        fee= None
        for order in self.booking:
            if order.booking_id == booking_id:
                order.status = "cancelled"
                fee = PriceManager().calculate_cancellation_fee(order, current_datetime)
                order.cancellation_fee = fee
        DataManager().save_bookings(self.booking)
        if fee is None:
            return "Couldn't cancel"
        return f"cancelled successfully, fee is {fee}"






pricing = PriceManager()
books_list = DataManager().load_bookings()
rooms_list = DataManager().load_rooms()
object_book_list = []
for order in books_list:
    order = Booking.from_dict(order)
    object_book_list.append(order)
object_room_list = []
for room in rooms_list:
    room = Room.from_dict(room)
    object_room_list.append(room)
books_list = object_book_list
rooms_list = object_room_list

me = BookingManager(rooms_list, books_list, pricing)
# print(me.update_booking("B009", "2026-11-18", "17:11", 3))
# print(me.create_booking("Mordy", "R001", "2027-02-01", "17:00", 5))
print(me.cancel_booking("B009", datetime.datetime.now()))
#
#


