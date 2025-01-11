# FastAPI
A demo program of the Python FastAPI library


Project dependencies are managed via Pipenv.  See https://pipenv.pypa.io for more information or troubleshooting.ex


# Instructions for running program 
This program has two distinct components-
1. The Server: Where the API structure exists (ie, the custom build)
2. The Client: Where the API is called

To execute both the Server side and the client side within a single IDE requires special handling as follows
1. The Server side must be executed first.  This 'Turns on' the API
2. Both the Server and Client run configurations must be set up to allow parallel instances

via PyCharm-
1. Create configurations for server.py/client.py 
2. In edit configurations, click on "Modify options"
3. In Modify options select " Allow multiple instances"
4. Note: In the run terminal you can split the views to watch them side by sid

via Visual Studio Code
1. Open server.py/client.py
2. Navigate to run or debug
3. Click the drop-down
4. Select 'Run in dedicated terminal'

# Browser links for running program
1. Home Page: http://127.0.0.1:8000
2. Interactive API documentation: http://127.0.0.1:8000/docs
3. Greeting: http://127.0.0.1:8000/greeting
4. Personal Greeting: http://127.0.0.1:8000/personal_greeting?username=<value_here>
5. User Profile: http://127.0.0.1:8000/user_profile?id=<value_here>