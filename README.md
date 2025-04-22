# Palindrome REST API

## Brief Description of the Implementation Architecture

This is a Flask-based REST API that allows users to manage and check if submitted messages are palindromes. It leverages:

- **Flask** for the web framework.
- **Firebase Realtime Database** for storing and retrieving messages.
- **Docker** for containerization.
- **GitHub Actions** for CI/CD automation.
- **Cloud Run (GCP)** for scalable deployment.
- **Swagger** for interactive API documentation.
- **Pytest** for test coverage.

**Core Functionalities:**
- Submit new messages.
- List all messages.
- Retrieve a message by ID and determine if it's a palindrome.
- Delete a message.

---
## Project Structure

* flask-rest-api/
```
* py-api/
  |--- config/
  |    |--- __init__.py
  |    |--- config.py
  |    |--- db.py
  |--- palindrome/
  |    |--- __init__.py
  |    |--- dto.py
  |    |--- routes.py
  |    |--- services.py
  |--- static/
  |    |--- swagger.json
  |--- tests/
  |    |--- test_routes.py
  |--- main.py
```

## Sequence Diagram of the Use Cases Interactions

#### 1. Show the list of messages posted by the users
![image](https://github.com/user-attachments/assets/95cb0dcc-4608-41f8-ab97-86100387f3de)

#### 2. Allow to post new messages
![image](https://github.com/user-attachments/assets/d8ce1560-d4f3-482d-85d2-e2e72cc6e11d)

#### 3. Allow to select a given message to see extra details
![image](https://github.com/user-attachments/assets/283079d7-a34c-4782-b758-e1c571a4850c)


## How To: Build, Deploy, and Access the App.

This project is set up to automatically build and deploy Dockerized Palindrome API to **Google Cloud Run** on every push to the `main` branch using **GitHub Actions**. 

### Workflow Overview
1. As a first step the workflow authenticates with Google Cloud using a service account.
2. Builds a docker image using the CLI and pushes it to Google Artifact registery.
3. In the final step it deploys the container to Google Cloud Run.

### Running the application Locally

#### Clone the repository
```
git clone https://github.com/bhargavabhamidipati/py-api.git
cd py-api
```

#### Run locally (For Windows)
```
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py
```

### Triggering of the workflow
Once your changes are done you can push the code to main and the workflow is triggered automatically.
```
git add .
git commit -m "[commit message]"
git push origin main
```

## API Documentation

This section of the document details the available API endpoints for managing the API.

---

## Message Endpoints

Base URL: `https://py-api-450754445212.europe-north2.run.app/api/v1/`

### 1. Create a new message

*   **Method:** `POST`
*   **URL:** `/messages`
*   **Description:** Creates a new message entry. The service automatically checks if the provided content is a palindrome and stores in the database.
*   **Request Body:**
    *   **Content-Type:** `application/json`
    *   **Schema:**
        ```json
        {
          "message": "string"
        }
        ```
    *   **Example:**
        ```json
        {
          "message": "madam"
        }
        ```
*   **Success Response:**
    *   **Code:** `201 Created`
    *   **Response Description:** Returns the newly created object, including its generated ID, message, and a boolean value indicating if it's a palindrome.
    *   **Example:**
        ```json
        {
          "message_id": "[uuid]",
          "message": "madam",
          "is_palindrome": true
        }
        ```
*   **Error Responses:**
    *   **Code:** `400 Bad Request`
    *   **Condotion:** The request payload is invalid.
    *   **Example:**
        ```json
        {
          "error": "Payload validation error"
        }
        ```
    *   **Code:** `500 Internal Server Error`
    *   **Condition:** A problem occurred while trying to save the message to the database.
    *   **Example:**
        ```json
        {
          "error": "Database connection error"
        }
        ```

---

### 2. Get message by ID

*   **Method:** `GET`
*   **URL:** `/messages/{message_id}`
*   **Description:** Retrieves the details of a single message using its unique ID.
*   **URL Parameters:**
    *   `message_id` (string, required): The unique identifier of the message to retrieve.
*   **Success Response:**
    *   **Code:** `200 OK`
    *   **Response Description:** Returns the message object matching the provided ID.
    *   **Example:**
        ```json
        {
          "message_id": "[uuid]",
          "message": "madam",
          "is_palindrome": true
        }
        ```
*   **Error Responses:**
    *   **Code:** `404 Not Found`
    *   **Condition:** No message exists with the specified `message_id`.
    *   **Example:**
        ```json
        {
          "error": "Message not found"
        }
        ```
    *   **Code:** `500 Internal Server Error`
    *   **Condition:** A problem occurred while trying to read the message from the database.
    *   **Example:**
        ```json
        {
          "error": "Database connection error"
        }
        ```

---

### 3. Get all messages

*   **Method:** `GET`
*   **URL:** `/messages`
*   **Description:** Retrieves a list of all messages stored in the database.
*   **Success Response:**
    *   **Code:** `200 OK`
    *   **Response Description:** Returns a JSON array containing all message objects.
    *   **Example:**
        ```json
        [
          {
            "message_id": "[uuid]",
            "message": "madam",
            "is_palindrome": true
          },
          {
            "message_id": "[uuid]",
            "message": "JonSnow",
            "is_palindrome": false
          }
        ]
        ```
*   **Error Responses:**
    *   **Code:** `404 Not Found`
    *   **Condition:** The database query was successful, but no messages were found.
    *   **Example**
        ```json
        {
          "error": "No messages found"
        }
        ```
    *   **Code:** `500 Internal Server Error`
    *   **Condition:** A problem occurred while trying to retrieve the messages from the database.
    *   **Example:**
        ```json
        {
          "error": "Database connection error"
        }
        ```

---

### 4. Delete message by ID

*   **Method:** `DELETE`
*   **URL:** `/messages/{message_id}`
*   **Description:** Removes a message from the database using its unique ID.
*   **URL Parameters:**
    *   `message_id` (string, required): The unique identifier of the message to delete.
*   **Success Response:**
    *   **Code:** `200 OK`
    *   **Response Description:** Returns a confirmation message indicating successful deletion.
    *   **Example:**
        ```json
        {
          "message": "Message deleted successfully"
        }
        ```
*   **Error Responses:**
    *   **Code:** `404 Not Found`
    *   **Condition:** No message exists with the specified `message_id` to delete.
    *   **Content:**
        ```json
        {
          "error": "Data not found"
        }
        ```
    *   **Code:** `500 Internal Server Error`
    *   **Condition:** A problem occurred while trying to delete the message from the database.
    *   **Content:**
        ```json
        {
          "error": "Database connection error"
        }
        ```

## References used
This project was developed independently, with occasional use of public resources for guidance and reference:
1. GENAI was used to assist with debugging tips, code structure suggestions, and syntax clarification. All final code was written and understood by me.
2. Blog posts and technical articles were referenced to understand implementation approaches and best practices.
3. For Firebase integration, I referred to the Pyrebase GitHub repository and adapted relevant code snippets to fit my use case.
4. For CI/CD automation, I used GitHub Actions workflows as recommended in the official documentation, customizing them as needed for this project.
5. All tools, libraries, and workflows used are open-source and publicly accessible. No proprietary or paid tools were used.
