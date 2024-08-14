This is the github repository of a Team Project of the University of Mannheim.
The goal of this project is to analyze a dataset of tweets about the topic Climate Change using Computer Vision and Natural Language Processing techniques.


# GUI Instructions:

start Port tunneling with the following command:
ssh -L 5173:localhost:5173 username@wifo5-33.informatik.uni-mannheim.de
where 5173 is replaced by the port on which vue.js is running and username is replaced by your actual username
Then you can access the GUI in the browser on your local machine on the adress localhost:5173

# Backend Instructions

start Flask Backend with command:
flask run --port=5001

# Documentation
The Backend revcieves a http request args for the columns and search words to be filtered.
The argument "all_content" describe values that all columns will be filtered for (other selected comlumns/values get ignored then, its in a seperate if clause)
The argument "custom" is meant to hand over parameters for a custom search/aggregation at a later time, that can then be easily implemented in python in the flask app.py
