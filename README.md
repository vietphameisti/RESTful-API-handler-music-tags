# RESTful API handle music tags
RESTful API with the Python Django Rest Framework to manage music tags. 
>The Django Rest Framework provides powerful model serialization, display data using standard function-based views.
<br>The relational database management system (RDBMS) which I used is SQLite, 
this is an open-source, zero-configuration, self-contained, stand-alone, transaction relational database engine designed to be embedded into an application.

<br>To run the program, please following steps:
>
_1. Download, clone the git code_
<br>_2. Install Django framework by using the command "$ pip install Django" in terminal (or window powershell)_
<br>_3. Install Django RESTful framework by using the command "$ pip install djangorestframework" in terminal (or window powershell)_
<br>_4. Open the terminal, move to the code folder, run this command "$ python manage.py runserver 0.0.0.0:8000" 
to start the server at 0.0.0.0 IP address and port 8000_
<br>_5. Using the Postman tool (or another tools) to compose and send HTTP requests and visualize the responses_
<br>_Example:_
>GET method: 0.0.0.0:8000/tracks/?tags=rock,meaningful
             <br>or 0.0.0.0:8000/export/
             <br>POST method: 0.0.0.0:8000/artist/ and the input JSON following format: {
"artist_name":"The Beatles",
"artist_tag":[3]
}
