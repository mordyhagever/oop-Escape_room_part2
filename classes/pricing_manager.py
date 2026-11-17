import datetime

from classes import booking


class PriceManager:
    def calculate_price(self, room, players, booking_date):
        weekday = booking_date.datetime.datetime.weekday()
        final_price = room["price_per_player"] * players
        discount = 0
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
        booked_time = booking["start_time"]
        booked_date = booked_time["booking_date"]
        datetime.datetime.strptime(booked_date, "%Y-%m-%d")
        datetime.datetime.strptime(booked_time, "%H:%M")
        booked = datetime.datetime.combine(booked_date, booked_time)
        if booked - now < datetime.timedelta(hours=24):
            if booked - now < datetime.timedelta(hours=6):
                if booked - now <= datetime.timedelta(minutes=1):
                    return "can't cancel"
                cancel_price = booking["total_price"] * 0.5
                return cancel_price
            cancel_price = booking["total_price"] * 0.0
            return cancel_price
        cancel_price = 0.0
        return cancel_price
