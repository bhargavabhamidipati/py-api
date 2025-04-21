from pydantic import BaseModel, Field

class PalindromeCreateDTO(BaseModel):
    message: str = Field(default=..., min_length=1)

class PalindromeResponseDTO(BaseModel):
    message_id: str
    message: str
    is_palindrome: bool
