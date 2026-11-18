import datetime

from classes import booking
from classes.validations import Validations


class PriceManager:
    def calculate_price(self, room, players, booking_date):
        weekday = booking_date.weekday()
        final_price = room["price_per_player"] * players
        discount = 0
        valid = Validations()
        # if not valid.is_int(players):
        #     return "Players has to be int"
        if 4 < players <= 6:
            discount = 10
        elif players > 6:
            discount = 15
        final_price = (final_price * players) - (final_price * (discount / 100))
        if weekday == 4 or weekday == 5:
            more_discount = final_price * 0.15
            final_price -= more_discount
        return final_price

    def calculate_cancellation_fee(self, booking, current_datetime):
        cancel_price = 0.0
        now = current_datetime
        booked_time = booking.start_time
        booked_date = booking.booking_date
        booked_date = datetime.date.strptime(booked_date, "%Y-%m-%d")
        booked_time = datetime.time.strptime(booked_time, "%H:%M")
        booked = datetime.datetime.combine(booked_date, booked_time)
        if booked - now < datetime.timedelta(hours=24):
            if booked - now < datetime.timedelta(hours=6):
                if booked - now <= datetime.timedelta(minutes=1):
                    return None
                cancel_price = booking.total_price * 0.5
                return cancel_price
            cancel_price = booking.total_price * 0.25
            return cancel_price
        cancel_price = 0.0
        return cancel_price
