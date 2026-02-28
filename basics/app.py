from flask import Flask  # importing the flask module

app = Flask(__name__) # creating an instance of th flask class

@app.route("/") # defining a route for the home page

def home():
    return "task flow backedn running!!!" #retruning a response when the home page is acces

if __name__ == "__main__":
    app.run(debug=True) #running the flask application in debug mode
