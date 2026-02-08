from flask import Flask, request, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os
from vector_store import astra_vector_store
from gemini import extract_answer

load_dotenv() 

PORT = os.getenv("PORT")


app = Flask(__name__)
CORS(app)


@app.route("/api/ask", methods=["POST"])
def ask():
    data = request.json

    company = data.get("company")
    year = data.get("year")
    question = data.get("question")

    if not company or not year or not question:
        return jsonify({"error": "Missing data"}), 400

    # 🔹 Vector search
    docs = astra_vector_store.similarity_search(
        query=question,
        k=8,
        filter={
            "company": company.lower(),
            "year": year
        }
    )

    if not docs:
        return jsonify({"answer": "NOT FOUND"})

    retrieved_text = "\n\n".join([doc.page_content for doc in docs])

    # 🔹 Gemini extraction
    answer = extract_answer(question, retrieved_text)

    return jsonify({
        "answer": answer
    })


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # fallback = 10000
    app.run(host="0.0.0.0", port=port, debug=False)

