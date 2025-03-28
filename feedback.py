class Feedback:
    """
    Represents feedback provided by a guest after their stay.
    """

    def __init__(self, feedback_id: int, guest, rating: int, comments: str):
        self.__feedback_id = feedback_id
        self.__guest = guest
        self.__rating = rating
        self.__comments = comments

    def submit_feedback(self) -> str:
        return f"Thank you Guest {self.__guest.get_id()} for your feedback!"

    def get_feedback_summary(self) -> str:
        return f"Feedback #{self.__feedback_id} by Guest {self.__guest.get_id()} - Rating: {self.__rating}/5, Comments: {self.__comments}"

    def __str__(self):
        return self.get_feedback_summary()