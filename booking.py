class Booking:
    """
    Represents a room booking made by a guest.
    """

    def __init__(self, booking_id: int, guest, room, check_in: str, check_out: str):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__room = room
        self.__check_in = check_in
        self.__check_out = check_out

        #automaticaly add to guest history
        guest.add_to_history(self)
        #mark room as unavailable
        room.set_availability(False)

    def make_reservation(self):
        return f"Reservation confirmed for Guest {self.__guest.get_id()} in Room {self.__room.get_room_number()} from {self.__check_in} to {self.__check_out}"

    def cancel_reservation(self):
        self.__room.set_availability(True)
        return f"Booking {self.__booking_id} has been cancelled."

    def get_booking_summary(self):
        return f"Booking {self.__booking_id}: Guest {self.__guest.get_id()}, Room {self.__room.get_room_number()}, {self.__check_in} to {self.__check_out}"

    def __str__(self):
        return self.get_booking_summary()