from flask import Flask


app = Flask(__name__)
visits = 0


@app.get("/")
def home():
    global visits
    visits += 1
    print(f"Request received. Counter: {visits}", flush=True)

    return f"""
    <!doctype html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Render Counter</title>
      </head>
      <body>
        <main>
          <h1>Render Counter</h1>
          <p>This process has handled {visits} request(s).</p>
          <p>Reload the page to increase the counter.</p>
        </main>
      </body>
    </html>
    """
