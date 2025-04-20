# from.dto import Palindrome
# import uuid
# from config.db import get_db_connection

# class PalindromeService:
#     def add_message(self, message:str):
#         try:
#             message_uuid = str(uuid.uuid4())
#             is_palindrome = message == message[::-1]
#             palindrome = Palindrome(message_uuid,message,is_palindrome)
#             with get_db_connection() as db:
#                 db.child("messages").child(message_uuid).set(palindrome.__dict__)
#         except Exception as e:
#             return f"an error occured:{e}"
#         return palindrome
        
#     def update_message(self,message_id:str, message:str):
#         try:
#             is_palindrome = message == message[::-1]
#             palindrome = Palindrome(message_id,message,is_palindrome)
#             with get_db_connection() as db:
#                 db.child("messages").child(message_id).update(palindrome.__dict__)
#         except Exception as e:
#             return f"an error occured:{e}"
#         return palindrome
        
#     def get_message(self,message_id:str):
#         try:
#             palindrome = None
#             with get_db_connection() as db:
#                 palindrome = db.child("messages").child(message_id).get()
#         except Exception as e:
#             return f"an error occured:{e}"
#         return palindrome

#     def get_all_messages(self):
#         try:
#             palindrome = None
#             with get_db_connection() as db:
#                 palindrome = db.child("messages").get()
#         except Exception as e:
#             return f"an error occured:{e}"
#         return palindrome
        
#     def delete_message(self, message_id:str):
#         try:
#             with get_db_connection() as db:
#                 db.child("messages").child(message_id).remove()
#         except Exception as e:
#             return f"an error occured:{e}"
#         return f"User deleted successfully"

from.dto import PalindromeCreateDTO, PalindromeResponseDTO
import uuid
from config.db import get_db_connection
from flask import current_app

class PalindromeService:
    def add_message(self, create_dto: PalindromeCreateDTO):
        try:
            message_uuid = str(uuid.uuid4())
            is_palindrome = create_dto.message == create_dto.message[::-1]
            response_dto = PalindromeResponseDTO(
                message_id=message_uuid,
                message=create_dto.message,
                is_palindrome=is_palindrome
            )
            with get_db_connection() as db:
                return db.child("messages").child(message_uuid).set(response_dto.__dict__)
            
        except Exception as e:
            current_app.logger.error(f"Database error: {e}")
            return None

    def update_message(self, message_id: str, create_dto: PalindromeCreateDTO):
        try:
            is_palindrome = create_dto.message == create_dto.message[::-1]
            response_dto = PalindromeResponseDTO(
                message_id=message_id,
                message=create_dto.message,
                is_palindrome=is_palindrome
            )
            with get_db_connection() as db:
                message_snapshot = db.child("messages").child(message_id).get()
                if message_snapshot and message_snapshot.val():
                    return db.child("messages").child(message_id).update(response_dto.__dict__)
                else:
                    return "Data not found"
            
        except Exception as e:
            current_app.logger.error(f"Database error: {e}")
            return None

    def get_message(self, message_id: str):
        try:
            with get_db_connection() as db:
                return db.child("messages").child(message_id).get()
            
        except Exception as e:
            current_app.logger.error(f"Database error: {e}")
            return None

    def get_all_messages(self):
        try:
            with get_db_connection() as db:
                return db.child("messages").get()
            
        except Exception as e:
            current_app.logger.error(f"Database error: {e}")
            return None

    def delete_message(self, message_id: str):
        try:
            with get_db_connection() as db:
                message_snapshot = db.child("messages").child(message_id).get()

                if message_snapshot and message_snapshot.val():
                    db.child("messages").child(message_id).remove()
                    return "Message deleted successfully"
                else:
                    return "Data not found"

        except Exception as error:
            current_app.logger.error(f"Database error: {error}")
            return None

