Twitter-Coke
============

How to run the app:
===================

In the root folder of the project is the "server" file.
In a terminal window, navigate to the folder where that files located.
At the command prompt type:
python server.py

This'll start the server application - ctrl+c to exit.

Dependancies:
Python 2.7
Jinja2
SQLAlchemy

Once the server is running, in a new browser window open the url : 
http://127.0.0.1:7000/

If no content displayed, click on the "Fetch more messages" button.
Click to keep refreshing the page.



How to retrieve data stored in database:
========================================

After running the application and refreshing a few times, a database will have been generated in the working directory of the server application i.e. "tweet.db".
To query the raw results, open a new terminal and startup the Python interpreter. Then run the following example code;

from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

engine = create_engine("sqlite:///tweet.db")

Session = sessionmaker(bind=engine)

session = Session()

data = session.execute('select * from tweet')

for item in data:

   print item

