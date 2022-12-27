from flask import Blueprint, render_template
from posts import Post
import requests

views = Blueprint(__name__, "views")

# Use requests to get blog posts 

posts = requests.get("https://api.npoint.io/0912c5d990db3873f519").json()
post_objects = []

for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)

# Set Routes

@views.route("/")
def homepage():
    return render_template("index.html", all_posts=post_objects)

@views.route("/<int:blog_id>")
def get_blog(blog_id):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == blog_id:
            requested_post = blog_post
    return render_template("post.html", blog=requested_post)

@views.route("/about")
def about_me():
    return render_template("about.html")

@views.route("/contact")
def contact_me():
    return render_template("contact.html")