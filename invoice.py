class Invoice:
    """
    Represents the invoice for a booking, including payment details.
    """

    def __init__(self, invoice_id: int, booking, total_amount: float, payment_method: str):
        self.__invoice_id = invoice_id
        self.__booking = booking
        self.__total_amount = total_amount
        self.__payment_status = "Pending"
        self.__payment_method = payment_method

    def generate_invoice(self) -> str:
        return (
            f"Invoice #{self.__invoice_id}\n"
            f"Booking: {self.__booking.get_booking_summary()}\n"
            f"Total: AED {self.__total_amount:.2f}\n"
            f"Payment Method: {self.__payment_method}\n"
            f"Status: {self.__payment_status}"
        )

    def process_payment(self) -> bool:
        self.__payment_status = "Paid"
        return True

    def get_status(self) -> str:
        return self.__payment_status

    def __str__(self):
        return self.generate_invoice()