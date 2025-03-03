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

@app.route("/BOSCH_BGS05X240")
def Bosch():
    categories = db.get_categories()
    articles = db.get_articles()
    price = db.get_price()
    return render_template ("BOSCH_BGS05X240.html", categories=categories , articles = articles , price = price)

@app.route("/BOSCH_BGS05X240/haract")    
def Bosch_haract():
    categories = db.get_categories()
    articles = db.get_articles()
    price = db.get_price()
    ops = db.get_ops()
    return render_template ("BOSCH_BGS05X240_haract.html", categories=categories , articles = articles , price = price , ops=ops)

@app.route("/Beko_CEG7304X")
def BEko():
    categories = db.get_categories()
    articles = db.get_articles()
    price = db.get_price()
    return render_template ("Beko_CEG7304X.html", categories=categories , articles = articles , price = price)

@app.route("/Beko_CEG7304X/haract")    
def BEko_haract():
    categories = db.get_categories()
    articles = db.get_articles()
    price = db.get_price()
    ops = db.get_ops()
    return render_template ("Beko_CEG7304X_haract.html", categories=categories , articles = articles , price = price , ops=ops)

@app.route("/<int:product_id>")
def product_page(product_id):
    categories = db.get_categories()
    article = db.get_article_by_id(product_id)
    price = db.get_price_by_id(article[8])
    return render_template ("product.html", categories=categories , article = article , price = price)

@app.route("/<int:product_id>/<int:ops_id>")
def ops_page(product_id, ops_id):
    categories = db.get_categories()
    article = db.get_article_by_id(product_id)
    ops = db.get_ops_by_id(ops_id)
    return render_template ("product_haract.html", categories = categories , article = article , ops = ops)

@app.route("/category/<int:category_id>")
def category_page(category_id, product_id):
    
    categories = db.get_categories(category_id)
    articles = db.get_articles_by_category(product_id)
    print(categories)
    return render_template("category.html", categories=categories , articles=articles , category_name = categories[category_id][1])

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True # автоматичне оновлення шаблонів
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу в режимі налагодження

