import os
import requests
from flask import Flask, request

app = Flask(__name__)

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

@app.route("/tv", methods=["POST"])
def tv():
    data = request.get_json(silent=True) or {}
    text = data.get("message", "Alerta TradingView")

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    requests.post(url, json={
        "chat_id": CHAT_ID,
        "text": text
    })

    return {"ok": True}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
