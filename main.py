from crypt import methods
from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/', methods=["GET"])
def homepage():
    response = requests.get("https://api.themoviedb.org/3/movie/550?api_key=3714c210af4bfc6eb0cf27b8bf827c79")
    movies = response.json()
    return render_template("homepage.html", movies=movies)

if __name__ == '__main__':
    app.run(debug=True)
