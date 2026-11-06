import logging, random, time
from flask import Flask

logging.basicConfig(level=logging.INFO)
log = logging.getLogger("payment-service")

app = Flask(__name__)

@app.route("/pay")
def pay():
    amount = random.randint(100, 5000)
    log.info("processing payment, amount=%s", amount)
    time.sleep(random.uniform(0.1, 0.5))
    if random.random() < 0.2:
        log.error("payment declined by bank, amount=%s", amount)
        return {"status": "failed"}, 500
    log.info("payment successful, amount=%s", amount)
    return {"status": "paid"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
