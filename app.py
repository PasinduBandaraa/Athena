import requests
from flask import Flask, request, render_template

app = Flask(__name__)
gemini_api_key = "AIzaSyDRvpk2YpApc3qFQAHeUhQOzLYZaB_8hJ8"  # Replace this with your actual API key

@app.route("/", methods=["GET", "POST"])
def chatbot():
    if request.method == "POST":
        user_input = request.form["user_input"]
        
        data = {
            "prompt": user_input,
            "languageCode": "en-US",
            "model": "gemini-2-7-4",
            "maxTokens": 150,
            "temperature": 0.7,
        }

        response = requests.post(
            f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={gemini_api_key}",
            json=data,
            headers={"Content-Type": "application/json"},
        )
        
        if response.status_code == 200:
            response_json = response.json()
            print(response_json)  # Add this line to inspect the entire response content
            if "text" in response_json:
                generated_text = response_json["text"]
                return generated_text
            else:
                return "No text found in response", 400
        else:
            return f"Error: {response.status_code} - {response.text}", 400
    else:
        return render_template("chatbot.html")

if __name__ == "__main__":
    app.run(debug=True)
