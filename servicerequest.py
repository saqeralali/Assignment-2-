class ServiceRequest:
    """
    Represents a guest’s request for additional services like housekeeping or transportation.
    """

    def __init__(self, request_id: int, guest, request_type: str):
        self.__request_id = request_id
        self.__guest = guest
        self.__request_type = request_type
        self.__status = "Pending"

    def submit_request(self) -> bool:
        self.__status = "Submitted"
        return True

    def update_status(self, new_status: str):
        self.__status = new_status

    def get_request_details(self) -> str:
        return f"Request #{self.__request_id}: {self.__request_type} for Guest {self.__guest.get_id()} - Status: {self.__status}"

    def __str__(self):
        return self.get_request_details()