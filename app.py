from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hasil", methods=["GET","POST"])
def predict():
    if request.method == 'POST':
        data = {
            "ips1": [float(request.form.get("ips1"))],
            "ips4": [float(request.form.get("ips4"))],
            "pemrograman_berorientasi_objek": [request.form.get("pemrograman_berorientasi_objek")]
        }
        
        prediction = model.predict(data)
        
        return render_template("result.html", result=prediction[0])
    else:
        return render_template("index.html")