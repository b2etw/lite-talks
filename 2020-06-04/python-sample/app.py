import logging
import os

from flask import make_response, Flask

app = Flask(__name__)

logging.basicConfig(filename="./log/app.log",
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    level=logging.DEBUG)


@app.route("/env", methods=["GET"])
def root():
    value1 = os.getenv("first")
    value2 = os.getenv("last")
    logging.info(f"first={value1}, last={value2}")
    return make_response(f"first={value1}, last={value2}", 200)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
