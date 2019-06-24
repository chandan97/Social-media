from flask import Flask,render_template,request
from flask_corsimport CORS
from socialmedia2 import post_create,get_newposts


app =Flask(_name_)

Cors(app)

@app.route('/',method=['GET' ,'POST'])
def index():


    if request.method =='GET':
        pass

    if request.method == 'POST':
        name = request.form.get('name')
        post = request.form.get('post')
        create_post(name,post)

    post = get_posts()


    return render_template('index.html',posts=posts)


if_name_=='main':
    app.run(debug=True)
