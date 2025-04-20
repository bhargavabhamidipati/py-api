# class Palindrome:
#     def __init__(self, message_id:str,message:str, is_palindrome:bool):
#         self.message_id=message_id
#         self.message = message
#         self.is_palindrome = is_palindrome

from pydantic import BaseModel, Field

class PalindromeCreateDTO(BaseModel):
    message: str = Field(default=..., min_length=1)

class PalindromeResponseDTO(BaseModel):
    message_id: str
    message: str
    is_palindrome: bool
