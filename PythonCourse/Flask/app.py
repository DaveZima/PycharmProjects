from flask import Flask, render_template, request, url_for, redirect


POSTS = {
	0: { "post_id": 0,
		 "title": "The Bad Batch",
	     "content": "Showing on Disney+" }
}

print("*********************")
print("* Flask Application *")
print("*********************")

# Start the web server running on this computer
# Using __name__ dunder method insures unique name
app = Flask(__name__)


# Called when in browser, a page is opened up with http://127.0.0.1:5000/
# decorator
@app.route('/')
def home():
	return render_template('home.html',post=POSTS)

@app.route("/post/<int:post_id>")  # Flask unique syntax  /post/@
def post(post_id):
	post = POSTS.get(post_id)
	if not post:    # post will be None if not found: not None = True
		return render_template('404.html',message=f'A post with id {post_id} was not found.')
	return render_template('post.html',post=POSTS)

# 127.0.0.1:5000/post/create?title=blabla&content=something_else
@app.route('/post/create', methods=['GET','POST'])
def create():
	# Flash returns the data into a dictionary
	# title = request.args.get('title')
	# content = request.args.get('content')

	# request.form returns hidden payload for security
	# In create.html <form action="/post/create" method="POST">

	if request.method == "POST":
		title = request.form.get('title')
		content = request.form.get('content')
		# Add new content to Python dictionary POSTS
		post_id = len(POSTS)
		POSTS[post_id] = {'id': post_id, 'title': title, 'content':content}

		# takes in the function name and prevents hard coding.
		return redirect(url_for('post', post_id=post_id))
	return render_template('create.html')



################
# Module Start #
################

if __name__ == "__main__":
	app.run(debug=True)
