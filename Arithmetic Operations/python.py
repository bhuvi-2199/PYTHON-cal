from flask import Flask,request, render_template
app = Flask(__name__)


@app.route('/', methods=["GET","POST"])
def main():
    if request.method == "POST":
        a=int(request.form.get("a"))
        b=int(request.form.get("b"))
        op = request.form.get("op")
        if (op == "add"):
            ans = a+b
        elif (op == "sub"):
            ans = a-b
        elif (op == "mult"):
            ans = multiply(a,b)
        elif (op == "div"):
            ans = divide(a,b)
        elif (op == "mod"):
            ans = mod(a,b)
        else:
            ans = "Invalid"
        return render_template("index.html",ans=ans)
    else:
        return render_template("index.html",ans="")


if __name__ == '__main__':
   app.run(debug = True)
