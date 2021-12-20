from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/')
def hello_world():
    return '<h1> Hellooooo </h1>'

@app.route('/about')
def about():
    return 'abbout mee'