from flask import Flask, render_template, request
from posts import Post
import requests

app = Flask(__name__)

posts = requests.get("https://api.npoint.io/0912c5d990db3873f519").json()
post_objects = []

for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

@app.route("/")
def homepage():
    return render_template("index.html", all_posts=post_objects)

@app.route("/post/<int:blog_id>")
def get_blog(blog_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == blog_id:
            requested_post = blog_post
    return render_template("post.html", blog=requested_post)

@app.route("/about")
def about_me():
    return render_template("about.html")

@app.route("/contact")
def contact_me():
    return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)