This readme contains instructions to run the M2A2app.py Flask application

setup:
To run this application, you must have Anaconda installed. Download it here: https://www.anaconda.com/download
Then you will open your Anaconda prompt and run these commands:
1. make an app directory with: mkdir flask_app && cd flask_app
2. create a virtual environment with: Python -m venv venv
3. Activate VE: venv/Script/activate
4. Install Flask with: pip install Flask
5. Install pytest with: pip install pytest

run:
1. download M2A2app.py and put it in your flask_app folder
2. open it in your Anaconda prompt and run by typing: python M2A2app.py
3. It will return a url to you. Append "/hello" to the end an search it in a browser. You should see the GET message on the screen

test:
1. Download the test_values.json and put it in the same folder you activated Flask in
2. open a new Anaconda prompt window and run: curl -X POST http://127.0.0.1:5000/sum -H "Content-Type: application/json" -d @test_values.json
3. In this same window, run: pytest test_M2A2app.py
You should see The results of the test at the bottom of the prompt window
