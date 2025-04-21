from flask import Blueprint, jsonify, request, current_app
from pydantic import ValidationError
from .dto import PalindromeCreateDTO
from .services import PalindromeService

palindrome = Blueprint('palindrome', __name__)
palindrome_service = PalindromeService()

@palindrome.route('/messages', methods=['POST'])
def create_message():
    try:
        create_dto = PalindromeCreateDTO(**request.get_json())
        created_message = palindrome_service.add_message(create_dto)

        if created_message is None:
            current_app.logger.error('Database connection error during message creation')
            return jsonify({'error': 'Database connection error'}), 500

        current_app.logger.info(f'Message created successfully: {created_message}')
        return jsonify(created_message), 200

    except ValidationError as validation_error:
        current_app.logger.error(f'Payload validation error: {validation_error.errors()}')
        return jsonify({'error': 'Payload validation error'}), 400


@palindrome.route('/messages/<string:message_id>', methods=['GET'])
def read_message(message_id: str):
    message_snapshot = palindrome_service.get_message(message_id)

    if message_snapshot is None:
        current_app.logger.error('Database connection error during read')
        return jsonify({'error': 'Database connection error'}), 500

    message_data = message_snapshot.val()
    if message_data:
        current_app.logger.info(f'Message found: {message_data}')
        return jsonify(message_data), 200

    current_app.logger.info(f'Message not found: {message_id}')
    return jsonify({'error': 'Message not found'}), 404


@palindrome.route('/messages', methods=['GET'])
def read_all_messages():
    messages_snapshot = palindrome_service.get_all_messages()

    if messages_snapshot is None:
        current_app.logger.error('Database connection error')
        return jsonify({'error': 'Database connection error'}), 500

    if not messages_snapshot.val():
        current_app.logger.info('No messages found')
        return jsonify({'error': 'No messages found'}), 404

    messages_list = [message.val() for message in messages_snapshot.each()]
    current_app.logger.info('Messages retrieved successfully')
    return jsonify(messages_list), 200



@palindrome.route('/messages/<string:message_id>', methods=['DELETE'])
def remove_message(message_id: str):
    deletion_result = palindrome_service.delete_message(message_id)

    if deletion_result is None:
        current_app.logger.error('Database connection error during deletion')
        return jsonify({'error': 'Database connection error'}), 500

    if deletion_result == "Data not found":
        current_app.logger.info(f'Message not found: {message_id}')
        return jsonify({'error': deletion_result}), 404

    current_app.logger.info(f'Message deleted: {message_id}')
    return jsonify({'message': deletion_result}), 200

