ChatbotAPI Django Project
This Django project, ChatbotAPI, is designed to create a RESTful API with a basic chatbot functionality. The API includes endpoints for sending messages to the chatbot and retrieving chat history.

Getting Started
Setting up the Django Project
Create a new Django project called "ChatbotAPI."

Copy code
django-admin startproject ChatbotAPI
Create a Django app called "chatbot" within the project.

Copy code
python manage.py startapp chatbot
Set up a SQL database and configure it in your Django project.

Running the Django REST API
The Django REST API includes the following endpoints:

/api/chat/: A POST endpoint for sending messages to the chatbot.
/api/chat/history/: A GET endpoint that retrieves the chat history.
To run the API:

Apply migrations.

Copy code
python manage.py makemigrations
python manage.py migrate
Start the development server.

Copy code
python manage.py runserver
Access the API at http://127.0.0.1:8000/api/.

Chatbot Implementation
The chatbot is implemented using a Language Model (LLM) and interacts with user messages. It maintains conversation history and provides responses.

Postman Collection
A Postman collection is provided for testing the API endpoints. Import it into your Postman environment to run test scenarios.

Test Scenarios
Sending a message to the chatbot (POST /api/chat/):

Send a POST request to /api/chat/ with a message in the request body.
Verify the response from the chatbot.
Retrieving the chat history (GET /api/chat/history/):

Send a GET request to /api/chat/history/.
Check the response for the chat history.
API Documentation
API documentation is automatically generated using Django Rest Framework's documentation generator. Access it by visiting /api/docs/ in your browser when the development server is running. The documentation provides details on making API requests, understanding responses, and using the endpoints effectively.

Postman Test Scripts
Test scripts in Postman are included to validate API responses, ensuring that chatbot responses are relevant and consistent with the provided test scenarios.

Feel free to modify this README as needed for your project, adding additional sections or details if required.