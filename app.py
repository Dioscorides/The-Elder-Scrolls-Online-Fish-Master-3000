from flask import Flask
from flask import render_template
from flaskwebgui import FlaskUI
from sound_detector import detector

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("index.html")


@app.route('/start', methods=['POST'])
def start_fishing():
    detector.start()  # Use the imported instance of SoundDetector
    return 'Started fishing'


@app.route('/stop', methods=['POST'])
def stop_fishing():
    detector.stop()  # Use the imported instance of SoundDetector
    return 'Stopped fishing'


def start_flask(**server_kwargs):
    app = server_kwargs.pop("app", None)
    server_kwargs.pop("debug", None)

    try:
        import waitress

        waitress.serve(app, **server_kwargs)
    except:
        app.run(**server_kwargs)


if __name__ == "__main__":
    # app.run() # Debug mode

    FlaskUI(
        app=app,
        server="flask",
        width=800,
        height=400,
        on_startup=lambda: print("Let's go fishing!"),
    ).run()
