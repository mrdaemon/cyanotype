from flask import render_template
from cyanotype import app, flatpages

@app.template_filter('excerpt')
def excerpt_filter(text):
    """ Template filter that extracts the first paragraph """
    paragraphs = text.split('</p>')
    return paragraphs[0]

@app.route('/')
def home_index():
    return render_template('home.html')

@app.route('/posts/')
def get_posts():
    posts = [p for p in flatpages]
    posts.sort(key=lambda item: item['date'], reverse=True)
    return render_template('posts.html', posts=posts)

@app.route('/posts/<name>/')
def get_post(name):
    post = flatpages.get_or_404(name)
    return render_template('post.html', post=post)
