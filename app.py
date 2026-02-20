import os
from flask import Flask, render_template

app = Flask(__name__)

# Backend base URL, e.g. https://your-backend.azurewebsites.net
BACKEND_BASE_URL = os.getenv("BACKEND_BASE_URL", "").rstrip("/")

@app.get("/")
def home():
    # Pass backend URL to template (JS will call it)
    return render_template("index.html", backend_base_url=BACKEND_BASE_URL)

@app.get("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", "8000"))
    app.run(host="0.0.0.0", port=port, debug=True)