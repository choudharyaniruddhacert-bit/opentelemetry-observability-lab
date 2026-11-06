import logging, random, time, requests
from flask import Flask

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("order-service")

app = Flask(__name__)

@app.route("/order")
def order():
    log.info("order received")
    time.sleep(random.uniform(0.05, 0.2))
    r = requests.get("http://payment-service:5001/pay", timeout=5)
    if r.status_code != 200:
        log.error("order failed: payment returned %s", r.status_code)
    else:
        log.info("order placed successfully")
    return {"order": "placed", "payment": r.json()}, r.status_code

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
