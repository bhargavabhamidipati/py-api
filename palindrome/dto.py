from pydantic import BaseModel, Field

class PalindromeCreateDTO(BaseModel):
    """
    Data Transfer Object for creating a new palindrome message.

    Attributes:
        message (str): The input message string to be stored and evaluated.
                       Must be at least 1 character long.
    """
    message: str = Field(default=..., min_length=1)

class PalindromeResponseDTO(BaseModel):
    """
    Data Transfer Object for returning a palindrome message response.

    Attributes:
        message_id (str): Unique identifier for the message.
        message (str): The original message.
        is_palindrome (bool): Used to store bool value. It
                            is true if message is palindrome else false.
    """
    message_id: str
    message: str
    is_palindrome: bool
