from flask import Flask,render_template, redirect,request
import detect

app = Flask(__name__)

@app.route("/")
def start():
	return render_template("index.html")

@app.route("/",methods = ["POST"])
def pred():
	if request.method == "POST":
		f = request.files["userfile"]
		path = f"./static/{f.filename}"
		f.save(path)
		pred = detect.pred_img(path)
		result_dic = {
		"image":path,
		"pred":pred
		}
		return render_template("index.html",your_result=result_dic)


if __name__ == "__main__":
	app.run(debug=False,host="0.0.0.0")	