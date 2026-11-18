import datetime
from cmath import acos

from classes.data_manager import DataManager

class ReportsManager:
    def __init__(self, rooms, bookings):
        self.rooms = rooms
        self.bookings = bookings

    def count_active_bookings(self):
        active_orders = 0
        for order in self.bookings:
            if order.status == "Active":
                active_orders += 1
        return f"active orders: {active_orders}"

    def count_cancelled_bookings(self):
        cancelled_orders = 0
        for order in self.bookings:
            if order.status == "cancelled":
                cancelled_orders += 1
        return f"cancelled orders: {cancelled_orders}"

    def calculate_total_revenue(self):
        active_orders_revenue = 0.0
        for order in self.bookings:
            if order.status == "Active":
                active_orders_revenue += order.total_price
        return f"active orders revenue: {active_orders_revenue}"

    def calculate_cancellation_revenue(self):
        cancellation_revenue = 0.0
        for order in self.bookings:
            cancellation_revenue += order.cancellation_fee
        return f"cancellation revenue is: {cancellation_revenue}"

    def get_most_popular_room(self):
        rooms_used = {}
        for room in self.rooms:
            rooms_used[room.room_id] = 0
        for order in self.bookings:
            rooms_used[order.room_id] += 1
        popular = max(rooms_used, key=rooms_used.get)
        return f"Most popular room is: {popular}"

    def get_room_booking_count(self):
        rooms_used = {}
        for room in self.rooms:
            rooms_used[room.room_id] = 0
        for order in self.bookings:
            rooms_used[order.room_id] += 1
        return rooms_used

    def calculate_occupancy(self, room_id, booking_date):
        found = False
        for room in self.rooms:
            if room.room_id == room_id:
                found = True
        if not found:
            return "Couldn't find the room"
        total_time = 0
        for order in self.bookings:
            if order.room_id == room_id and order.booking_date == booking_date:
                for room in self.rooms:
                    if room.room_id == room_id:
                        total_time += room.duration
        total_time /= 60
        percentage = total_time / 12
        percentage = round(percentage * 100, 1)
        return f"active percentage is: {percentage}%"






