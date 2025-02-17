from flask import Flask, render_template
from db_scripts import DBManager

app = Flask(__name__)# Створюємо веб–додаток Flask
db = DBManager("catalog.db")


@app.route("/login")  # Вказуємо url-адресу для виклику функції
def login():
    users = db.get_users()
    print(users)
    return render_template("login.html", users = users) # html-сторінка, що повертається у браузер


@app.route("/")
def index():
    categories = db.get_categories()
    articles = db.get_articles()

    print(categories)
    return render_template("index.html", categories = categories , articles = articles)
    
@app.route("/Play_Station")    
def Ps():
    categories = db.get_categories()
    articles = db.get_articles()
    price = db.get_price()
    return render_template("Ps_5_Pro.html", categories=categories , articles = articles , price = price)

@app.route("/Play_Station/haract")    
def Ps_haract():
    categories = db.get_categories()
    articles = db.get_articles()
    price = db.get_price()
    ops = db.get_ops()
    return render_template ("Ps_5_Pro_haract.html", categories=categories , articles = articles , price = price , ops=ops)


if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True # автоматичне оновлення шаблонів
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу в режимі налагодження

