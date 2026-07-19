from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "id": 1,
        "title": "My First Blog Post",
        "date": "July 10, 2026",
        "author":"Meghana",
        "content": "This is my very first blog post. I am learning Flask and it is going really well. Building web apps with Python feels great."
    },
    {
        "id": 2,
        "title": "What I Learned This Week",
        "date":"July 14, 2026",
        "author": "Meghana",
        "content": "This week I learned about Flask routes, templates, and Jinja2. I also built a notes app and now a blog. Python web development is fun."
    },
    {
        "id": 3,
        "title": "Why I Like Python",
        "date": "July 19, 2026",
        "author":"Meghana",
        "content": "Python is simple, readable, and powerful. From CLI projects to web apps, it covers everything. It is the best language to start with."
    }
]

@app.route("/")
def home():
    return render_template("home.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    current_post = next((p for p in posts if p["id"] == post_id), None)
    if current_post is None:
        return "Post not found", 404
    return render_template("post.html", post=current_post)

if __name__ == "__main__":
    app.run(debug=True)
