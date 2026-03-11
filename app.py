from flask import Flask, render_template

app = Flask(__name__)

menu = [
    {"name": "Chicken Biryani", "price": "₹220"},
    {"name": "Mutton Biryani", "price": "₹320"},
    {"name": "Butter Chicken", "price": "₹260"},
    {"name": "Paneer Butter Masala", "price": "₹200"},
    {"name": "Tandoori Chicken", "price": "₹280"},
    {"name": "Veg Fried Rice", "price": "₹150"}
]

@app.route("/")
def home():
    return render_template("index.html", menu=menu)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
