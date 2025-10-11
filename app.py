from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Yeh tumhara personal data store hai
data = {
    "background": "Assalamu Alaikum! My name is Muhammad Tayyab. I am from Roshan Bheela, a village in Kasur, Punjab, Pakistan. My father, Muhammad Munir, is a teacher. I completed my early education at Govt Higher Secondary School Roshan Bheela. Later, I did my matriculation from Sadiq School Khudian Khas with 953/1100 marks, and then FSc Pre-Engineering from Piass College Kasur with 783 marks. I also love cricket and have represented my district Kasur at the district level.",
    "current_work": "I am currently pursuing a Software Engineering degree at UMT. Alongside my studies, I am learning and working on Machine Learning, Data Science, and Artificial Intelligence. My final year project is AI-based.",
    "goals": "My goals are to pursue a PhD abroad in the field of AI, establish my own software house, and eventually create an institute where I can provide free IT skills training to the youth of Pakistan.",
    "experience": "I have previously worked at a call center, done front-end development in web projects, and am currently doing an internship at Arc Technology.",
    "projects": "I have worked on web development projects, NLP projects, and machine learning projects, including those we have discussed together."
}

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"].lower()

    if "background" in user_message:
        return jsonify({"response": data["background"]})
    elif "current" in user_message:
        return jsonify({"response": data["current_work"]})
    elif "goal" in user_message:
        return jsonify({"response": data["goals"]})
    elif "experience" in user_message:
        return jsonify({"response": data["experience"]})
    elif "project" in user_message:
        return jsonify({"response": data["projects"]})
    else:
        return jsonify({
            "response": "Sorry, I don't have an answer for that. Try asking about background, current work, goals, experience, or projects."
        })

@app.route("/", methods=["GET"])
def health():
    return "TayyabBot backend is running."

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
