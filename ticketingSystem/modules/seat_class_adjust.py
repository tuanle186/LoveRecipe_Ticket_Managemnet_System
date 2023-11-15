import pickle

class Layout:
    def __init__(self, zoneA, zoneB, zoneC):
        self.__zoneA = zoneA
        self.__zoneB = zoneB
        self.__zoneC = zoneC
        self.__max_size = 294

    def get_count(self):
        return self.__zoneA.get_count() + self.__zoneB.get_count() + self.__zoneC.get_count()
    
    def get_max_size(self):
        return self.__max_size
    
    def is_full(self):
        return self.get_count() == self.__max_size
    
    def get_zoneA(self):
        return self.__zoneA
    
    def get_zoneB(self):
        return self.__zoneB
    
    def get_zoneC(self):
        return self.__zoneC

    def print(self):
        # print("\nZone A:")
        self.__zoneA.print()
        # print("\nZone B:")
        self.__zoneB.print()
        # print("\nZone C:")
        self.__zoneC.print()

    def book_seats(self, to_be_booked_seats, email, name, phone):
        for seat in to_be_booked_seats:
            if not seat.get_is_booked():
                id = seat.get_id()
                if self.__zoneA.check_id(id):
                    self.__zoneA.set_count(self.__zoneA.get_count() + 1)
                elif self.__zoneB.check_id(id):
                    self.__zoneB.set_count(self.__zoneB.get_count() + 1)
                else:
                    self.__zoneC.set_count(self.__zoneC.get_count() + 1)
            seat.book(email, name, phone)
        
    def clear_seats(self, to_be_cleared_seats):
        for delSeat in to_be_cleared_seats:
            if delSeat.get_is_booked():
                id = delSeat.get_id()
                if self.__zoneA.check_id(id):
                    self.__zoneA.set_count(self.__zoneA.get_count() - 1)
                elif self.__zoneB.check_id(id):
                    self.__zoneB.set_count(self.__zoneB.get_count() - 1)
                else:
                    self.__zoneC.set_count(self.__zoneC.get_count() - 1)
                delSeat.clear()

    def save_changes(self):
        with open('C:/Programming/ticketingSystem/data/layout.pkl', 'wb') as file:
            pickle.dump(self, file)

    def get_seat_obj(self, id):
        list = self.__zoneA.get_seat_list() + self.__zoneB.get_seat_list() + self.__zoneC.get_seat_list()
        for seat in list:
            if seat.get_id() == id:
                return seat
            

class Zone:
    def __init__(self, seat_list, count, max_size):
        self.__seat_list = seat_list
        self.__count = count
        self.__max_size = max_size
    
    def get_empty_seats(self, n):
        empty_seats = []
        for seat in self.__seat_list:
            if len(empty_seats) == n:
                break
            if not seat.get_is_booked():
                empty_seats.append(seat)
            else:
                empty_seats.clear()
        return tuple(empty_seats)
    
    def get_seat_list(self):
        return self.__seat_list
    
    def get_count(self):
        return self.__count
    
    def get_max_size(self):
        return self.__max_size
    
    def get_remain(self):
        return self.__max_size - self.__count
    
    def set_count(self, count):
        self.__count = count
    
    def is_full(self):
        return self.__count == self.__max_size
    
    def print(self):
        for seat in self.__seat_list:
            seat.print()

    def check_id(self, id):
        for seat in self.__seat_list:
            if seat.get_id() == id:
                return True
        return False


class Seat:
    def __init__(self, id, is_premium, is_booked=False, email='', name='', phone=''):
        self.__id = id
        self.__is_premium = is_premium
        self.__is_booked = is_booked
        self.__email = email
        self.__name = name
        self.__phone = phone
    
    def book(self, email, name, phone):
        self.__is_booked = True
        self.__email = email
        self.__name = name
        self.__phone = phone

    def clear(self):
        self.__is_booked = False
        self.__email = ''
        self.__name = ''
        self.__phone = ''

    def print(self):
        type = "Premium" if self.__is_premium else "Standard"
        if self.__is_booked:
            print(self.__id)
        else:
            print(self.__id)

    def get_id(self):
        return self.__id
    
    def get_is_premium(self):
        return self.__is_premium
    
    def get_is_booked(self):
        return self.__is_booked
    
    def get_email(self):
        return self.__email
    
    def get_name(self):
        return self.__name
    
    def get_phone(self):
        return self.__phone