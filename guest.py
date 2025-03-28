class Guest:
    """
    Represents a hotel guest with contact details and loyalty points.
    """

    def __init__(self, guest_id: int, name: str, email: str, phone: str):
        self.__guest_id = guest_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__loyalty_points = 0
        self.__reservation_history = []

    def create_account(self):
        print(f"Account created for {self.__name}.")

    def update_profile(self, name: str = None, email: str = None, phone: str = None):
        if name:
            self.__name = name
        if email:
            self.__email = email
        if phone:
            self.__phone = phone

    def add_to_history(self, booking):
        self.__reservation_history.append(booking)

    def view_reservation_history(self):
        return self.__reservation_history

    def get_id(self):
        return self.__guest_id

    def get_loyalty_points(self):
        return self.__loyalty_points

    def add_loyalty_points(self, points: int):
        self.__loyalty_points += points

    def __str__(self):
        return f"Guest {self.__guest_id}: {self.__name}, Email: {self.__email}, Phone: {self.__phone}"