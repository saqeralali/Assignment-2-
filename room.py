class Room:
    """
    Represents a hotel room with details such as room number, type, amenities, price, and availability.
    """

    def __init__(self, room_number: int, room_type: str, amenities: list, price_per_night: float, is_available: bool = True):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__amenities = amenities
        self.__price_per_night = price_per_night
        self.__is_available = is_available

    def check_availability(self) -> bool:
        return self.__is_available

    def get_room_info(self) -> str:
        return f"Room {self.__room_number}: {self.__room_type}, AED {self.__price_per_night}/night, Amenities: {', '.join(self.__amenities)}"

    def set_availability(self, available: bool):
        self.__is_available = available

    def get_price(self) -> float:
        return self.__price_per_night

    def get_room_number(self) -> int:
        return self.__room_number

    def __str__(self):
        return self.get_room_info()