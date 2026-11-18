from classes.booking_manager import BookingManager
from classes.data_manager import DataManager
from classes.pricing_manager import PriceManager
from classes.reports_manager import ReportsManager
from classes.validations import Validations
import datetime
from classes.booking import Booking
from classes.room import Room


class EscapeRoomSystem:
    def __init__(self):
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
        self.rooms = rooms_list
        self.bookings = books_list
        self.data_manager = DataManager()
        self.booking_manager = BookingManager(self.rooms,  self.bookings, PriceManager())
        self.report_manager = ReportsManager(self.rooms, self.bookings)

    def save_data(self):
        DataManager().save_bookings(self.bookings)
        DataManager().save_rooms(self.rooms)

    def print(self):
        valid = Validations()
        print("""
        ====================
             MAIN MENU
        ====================
        1. Orders manager
        2. Reports
        3. Exit
                    """)
        choose = input()
        while not valid.main_choose_checker(choose):
            choose = input("Only a number from the menu: ")
        choose = int(choose)
        return choose

    def run(self):
        valid = Validations()
        choose = self.print()
        while choose != 3:
            if choose == 1:
                print("""
    ====== NEW ORDER MENU =====
    1. Create a new order
    2. Show all bookings
    3. Search booking by ID
    4. Show a client's booking
    5. Search booking by date
    6. Change booking details
    7. Cancel order
    8. return to main menu
                """)
                order_choose = input()
                while not valid.reports_choose_checker(order_choose):
                    order_choose = input("Only a number from the menu: ")
                order_choose = int(order_choose)
                if order_choose == 1:
                    print("===== CREATING NEW ORDER =====")
                    customer_name = input("Enter customer name: ")
                    room_id = input("Enter room id: ")
                    print("Enter booking date: ")
                    year = input("Year: ")
                    month = input("Month: ")
                    day = input("Day: ")
                    date = f"{year}-{month}-{day}"
                    print("Enter game time: ")
                    hour = input("Hour: ")
                    minutes = input("Minutes: ")
                    start_time = f"{hour}:{minutes}"
                    players = input("Enter number of players: ")
                    print(self.booking_manager.create_booking(customer_name, room_id, date, start_time, players))
                elif order_choose == 2:
                    self.booking_manager.show_all_bookings()
                elif order_choose == 3:
                    booking_id = input("Enter booking id: ")
                    print(self.booking_manager.get_booking_by_id(booking_id))
                elif order_choose == 4:
                    client = input("Enter customer name: ")
                    print(self.booking_manager.get_customer_booking(client))
                elif order_choose == 5:
                    print("Enter booking date: ")
                    year = input("Year: ")
                    month = input("Month: ")
                    day = input("Day: ")
                    date = f"{year}-{month}-{day}"
                    print(self.booking_manager.get_booking_by_date(date))
                elif order_choose == 6:
                    print("====== UPDATING BOOKING ======")
                    book_id = input("Enter booking id: ")
                    print("Enter booking date: ")
                    year = input("Year: ")
                    month = input("Month: ")
                    day = input("Day: ")
                    date = f"{year}-{month}-{day}"
                    print("Enter game time: ")
                    hour = input("Hour: ")
                    minutes = input("Minutes: ")
                    start_time = f"{hour}:{minutes}"
                    players = input("Enter number of players: ")
                    print(self.booking_manager.update_booking(book_id, date, start_time, players))
                elif order_choose == 7:
                    booking_id = input("Enter room id: ")
                    print(self.booking_manager.cancel_booking(booking_id, datetime.datetime.now()))


            elif choose == 2:
                print("""
    What report do you want?
    1. Number of active bookings
    2. Number of cancelled bookings
    3. All revenue from active bookings
    4. all cancellations fee
    5. Most popular room
    6. Orders number in each room
    7. Active percentage in one room
    8. Return
                        """)
                report_choose = input()
                while not valid.reports_choose_checker(report_choose):
                    report_choose = input("Only a number from the menu: ")
                report_choose = int(report_choose)
                if report_choose == 1:
                    print(self.report_manager.count_active_bookings())
                elif report_choose == 2:
                    print(self.report_manager.count_cancelled_bookings())
                elif report_choose == 3:
                    print(self.report_manager.calculate_total_revenue())
                elif report_choose == 4:
                    print(self.report_manager.calculate_cancellation_revenue())
                elif report_choose == 5:
                    print(self.report_manager.get_most_popular_room())
                elif report_choose == 6:
                    print(self.report_manager.get_room_booking_count())
                elif report_choose == 7:
                    room_id = input("Enter room id for the math: ")
                    print("Enter date for the math: ")
                    year = input("Year: ")
                    while not valid.is_int(year):
                        year = input("Only a number: ")
                    month = input("Month: ")
                    while not valid.is_int(month):
                        month = input("Only a number: ")
                    day = input("Day: ")
                    while not valid.is_int(day):
                        day = input("Only a number: ")
                    date = datetime.date(int(year), int(month), int(day))
                    print(self.report_manager.calculate_occupancy(room_id, date))
            choose = self.print()
        return "Finished progress!!!"

