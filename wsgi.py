from app import app

application = app

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(__import__('os').environ.get("PORT", 5000)))
