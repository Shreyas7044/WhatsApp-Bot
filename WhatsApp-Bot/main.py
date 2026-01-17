from flask import Flask, request
from googlesearch import search
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["POST"])
def bot():
    # Receive user message
    user_msg = request.values.get('Body', '').lower()

    # Create Twilio response object
    response = MessagingResponse()

    # Modify query to search GeeksforGeeks
    query = user_msg + " geeksforgeeks.org"

    # Search and collect results
    results = []
    for url in search(query, num_results=3):
        results.append(url)

    # Send response back to user
    msg = response.message(f"📘 Results for '{user_msg}':")
    for link in results:
        response.message(link)

    return str(response)

if __name__ == "__main__":
    app.run(debug=True)
