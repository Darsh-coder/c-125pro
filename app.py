from flask import Flask,jsonify,request
from classifer import getpred

app = Flask(__name__)
@app.route("/predict-alpha",methods = ["POST"])
def pred_data():
    image = request.files.get("aplha")
    prediction = getpred(image)
    return jsonify({
        "prediction":prediction

    }),200

if __name__ == "__main__":
    app.run(debug = True)
