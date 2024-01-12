from flask import Flask, render_template
import requests


app = Flask(__name__)

blog_url = "https://api.npoint.io/4240b875ee72579cd4f6"
all_posts = requests.get(blog_url).json()
print(all_posts)

@app.route("/")
def home():
    return render_template("index.html", posts=all_posts)

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/<page>/<num>")
def detail_page(page, num):
    print(num)
    int_num = int(num)
    return render_template("post.html", full_post=all_posts, number=int_num)



if __name__ == "__main__":
    app.run(debug=True)


