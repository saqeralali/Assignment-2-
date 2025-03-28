try:
    #guest account creation
    print("1. Guest Account Creation:")
    guest1 = Guest(1, "Saqer", "saqer@example.com", "0501234567")
    guest2 = Guest(2, "Zayed", "zayed@example.com", "0507654321")
    guest1.create_account()
    guest2.create_account()
    print(guest1)
    print(guest2, "\n")

    #searching for available Rooms
    print("2. Searching for Available Rooms:")
    room1 = Room(101, "Single", ["Wi-Fi", "TV"], 300.0)
    room2 = Room(102, "Suite", ["Wi-Fi", "Jacuzzi"], 900.0)
    print(room1.get_room_info(), "- Available:", room1.check_availability())
    print(room2.get_room_info(), "- Available:", room2.check_availability(), "\n")

    #making a room reservation
    print("3. Making a Room Reservation:")
    booking1 = Booking(1001, guest1, room1, "2025-04-01", "2025-04-05")
    booking2 = Booking(1002, guest2, room2, "2025-04-02", "2025-04-06")
    print(booking1.make_reservation())
    print(booking2.make_reservation(), "\n")

    #booking confirmation notification
    print("4. Booking Confirmation Notification:")
    print("Confirmation: Email sent to", guest1.get_id(), "for booking", booking1.get_booking_summary())
    print("Confirmation: Email sent to", guest2.get_id(), "for booking", booking2.get_booking_summary(), "\n")

    #invoice generation for a booking
    print("5. Invoice Generation for a Booking:")
    invoice1 = Invoice(501, booking1, 1200.0, "Credit Card")
    invoice2 = Invoice(502, booking2, 3600.0, "Mobile Wallet")
    print(invoice1.generate_invoice())
    print(invoice2.generate_invoice(), "\n")

    #processing Different Payment Methods
    print("6. Processing Different Payment Methods:")
    invoice1.process_payment()
    invoice2.process_payment()
    print("Invoice 1 Status:", invoice1.get_status())
    print("Invoice 2 Status:", invoice2.get_status(), "\n")

    #displaying reservation history
    print("7. Displaying Reservation History:")
    for booking in guest1.view_reservation_history():
        print("Guest 1 History:", booking.get_booking_summary())

    for booking in guest2.view_reservation_history():
        print("Guest 2 History:", booking.get_booking_summary(), "\n")

    #cancellation of a reservation
    print("8. Cancellation of a Reservation:")
    print(booking1.cancel_reservation())
    print(booking2.cancel_reservation())
    print("Room 101 Available:", room1.check_availability())
    print("Room 102 Available:", room2.check_availability(), "\n")

except Exception as e:
    print("ERROR OCCURRED:", e)
