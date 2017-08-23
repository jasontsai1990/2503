from flask import Flask, request, abort
from commom import func
from urls.admin import admin

app = Flask(__name__)

app.register_blueprint(admin)
app.add_template_filter(func.test, 'test')

@app.before_request
def before_request():
    try:
        request.cookies['login']
    except:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True)