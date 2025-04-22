from.dto import PalindromeCreateDTO, PalindromeResponseDTO
import uuid
from config.db import get_db_connection
from flask import current_app

class PalindromeService:

    """
    Service class to handle the business logic for palindrome message operations.
    Includes creation, retrieval, listing, and deletion of messages.
    """

    def add_message(self, create_dto: PalindromeCreateDTO):
        """
        Add a new message to the database and determine if it's a palindrome.

        Args:
            create_dto (PalindromeCreateDTO): The message data from the client.

        Returns:
            dict: Stored message dictionary on success.
            None: On failure.
        """

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

    def get_message(self, message_id: str):
        """
        Retrieve a single message from the database by ID.

        Args:
            message_id (str): UUID of the message to retrieve.

        Returns:
            Firebase snapshot: Message data if found.
            None: On failure or if not found.
        """
        try:
            with get_db_connection() as db:
                return db.child("messages").child(message_id).get()
            
        except Exception as e:
            current_app.logger.error(f"Database error: {e}")
            return None

    def get_all_messages(self):
        """
        Retrieve all messages stored in the database.

        Returns:
            Firebase snapshot: All messages data.
            None: On database error.
        """
        try:
            with get_db_connection() as db:
                return db.child("messages").get()
            
        except Exception as e:
            current_app.logger.error(f"Database error: {e}")
            return None

    def delete_message(self, message_id: str):
        """
        Delete a message from the database by ID.

        Args:
            message_id (str): UUID of the message to delete.

        Returns:
            str: Success or error message.
            None: On database error.
        """
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

