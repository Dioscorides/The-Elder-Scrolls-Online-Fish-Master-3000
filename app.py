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
    try:
        print("Attempting to start detector")
        detector.start()
        print("Detector started successfully")
        return 'Started fishing'
    except Exception as e:
        print(f"Exception occurred while starting: {e}")
        return 'Error starting fishing', 500


@app.route('/stop', methods=['POST'])
def stop_fishing():
    try:
        print("Attempting to stop detector")
        detector.stop()  # Use the imported instance of SoundDetector
        print("Detector stopped successfully")
        return 'Stopped fishing'
    except Exception as e:
        print(f"Exception occurred while stopping: {e}")
        return 'Error stopping fishing', 500


def start_flask(**server_kwargs):
    app = server_kwargs.pop("app", None)
    server_kwargs.pop("debug", None)

    try:
        import waitress
        waitress.serve(app, **server_kwargs)
    except Exception as e:
        print(f'Error starting server: {e}')
        app.run(**server_kwargs)


if __name__ == "__main__":
    # For debugging, uncomment the following line:
    # app.run()  # Debug mode

    FlaskUI(
        app=app,
        server="flask",
        width=800,
        height=435,
        on_startup=lambda: print("Let's go fishing!"),
        on_shutdown=lambda: print("Well, that was fun!")
    ).run()
