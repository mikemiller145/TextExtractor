# TextExtractor
Webapp that finds most common names mentioned in a text file and their frequency.

# Overview
This application is designed to recieve a text file such as a move script, article, etc...
Parse through the file extracting a list of all of the people mentioned in the file and displaying the most frequently mentioned.

# How to install
1. Clone this repository `https://github.com/mikemiller145/TextExtractor.git`.
2. Create virtual environment: `python -m venv TextExtractor\venv`.
3. Activate virtual environment: `TextExtractor\venv\Scripts\activate.bat`.
4. Once the virtual envoronment is active, install the required packages from `TextExtractor\TextExtractor\requirements.txt`.
5. Like this `pip install -r TextExtractor\TextExtractor\requirements.txt`. (Update: make to use Python 3.7 or earlier or the dependencies will not install correctly)
6. One of the packages: `spacy` requires a model: `en_core_web-sm` to run properly.
7. To load this model type: `python -m spacy download en_core_web_sm`.

8. This project is not connected to a database.
9. The virtual environment has msqlclient already installed, but you connect any databse of your choice.
10. To establish database connection edit `TextExtractor\TextExtractor\TextExtractor\settings.py`, go to the Django documentation for more detail.
11. Then once the database is setup run `manage.py makemigrations` and then `manage.py migrate` to create the correct tables
12. You should be good to go! :)

# What I Learned
1. Django Framework
2. MySQL
3. Sending data in transit(JSON)
4. More experience with HTML, CSS, and JS

