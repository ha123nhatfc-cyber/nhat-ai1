from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="YOUR_API_KEY")

chat_history = []

AI_NAME = "NHAT AI"

@app.route("/")
def index():
    return render_template("index.html", ai_name=AI_NAME)

@app.route("/chat", methods=["POST"])
def chat():

    user_message = request.json["message"]

    # chặn tạo ảnh hoặc video
    if "tạo ảnh" in user_message.lower() or "video" in user_message.lower():
        return jsonify({"reply": "Xin lỗi, tôi chỉ trả lời văn bản."})

    chat_history.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=chat_history
    )

    reply = response.choices[0].message.content

    chat_history.append({"role": "assistant", "content": reply})

    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True)
