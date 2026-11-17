import datetime
from os.path import curdir

from pip._internal import self_outdated_check


class Booking:
    def __init__(self, booking_id, customer_name, room_id, booking_date, start_time, players, total_price, status, cancellation_fee):
        self.booking_id = booking_id
        self.customer_name = customer_name
        self.room_id = room_id
        self.booking_date = booking_date
        self.start_time = start_time
        self.players = players
        self.total_price = total_price
        self.status = status
        self.cancellation_fee = cancellation_fee

    def cancel(self, fee):
        self.cancellation_fee = fee
        self.status = "cancelled"


    def update_details(self, booking_date, start_time, players, total_price):
        self.booking_date = booking_date
        self.start_time = start_time
        self.players = players
        self.total_price = total_price

    def to_dict(self):
        booking = {}
        booking["booking_id"] = self.booking_id
        booking["customer_name"] = self.customer_name
        booking["room_id"] = self.room_id
        booking["booking_date"] = self.booking_date
        booking["start_time"] = self.start_time
        booking["players"] = self.players
        booking["total_price"] = self.total_price
        booking["status"] = self.status
        booking["cancellation_fee"] = self.cancellation_fee
        return booking

    @classmethod
    def from_dict(cls, booking):
        return cls(booking["booking_id"], booking["customer_name"], booking["room_id"], booking["booking_date"],
                   booking["start_time"], booking["players"], booking["total_price"], booking["status"], booking["cancellation_fee"])


