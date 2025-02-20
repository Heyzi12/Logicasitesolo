import sqlite3

class DBManager():
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = None
        self.cursor = None

    def open_db(self):
        self.conn = sqlite3.connect(self.dbname)#створюємо з'єднання з базою даних
        self.cursor = self.conn.cursor()# створити вказівник на базу даних

    def get_categories(self):
        self.open_db()
        self.cursor.execute('''SELECT * FROM categories''')# виконуємо запит
        data = self.cursor.fetchall()# отримуємо відповідь і зберігаємо у зміну data
        self.conn.close()# закриваємо базу даних
        return data
    
    def get_articles(self):
        self.open_db()
        self.cursor.execute('''SELECT * FROM articles''')
        data = self.cursor.fetchall()
        self.conn.close()
        return data
    
    def get_price(self):
        self.open_db()
        self.cursor.execute('''SELECT * FROM price''')
        data = self.cursor.fetchall()
        self.conn.close()
        return data
    
    def get_price_by_id(self, price_id):
        self.open_db()
        self.cursor.execute('''SELECT * FROM price WHERE id=?''',[price_id])
        data = self.cursor.fetchone()
        self.conn.close()
        return data

    def get_users(self):
        self.open_db()
        self.cursor.execute('''SELECT * FROM users''')
        data = self.cursor.fetchall()
        self.conn.close()
        return data
    
    def get_articles_by_category(self, categori_id):
        self.open_db()
        self.cursor.execute('''SELECT * FROM articles WHERE category_id=?''', [categori_id])# виконуємо запит
        data = self.cursor.fetchall()# отримуємо відповідь і зберігаємо у зміну data
        self.conn.close()
        return data
    
    def get_ops(self):
        self.open_db()
        self.cursor.execute('''SELECT * FROM ops''')
        data = self.cursor.fetchall()
        self.conn.close()
        return data
    
    def get_article_by_id(self, article_id):
        self.open_db()
        self.cursor.execute('''SELECT * FROM articles WHERE id=?''', [article_id])# виконуємо запит
        data = self.cursor.fetchone()# отримуємо відповідь і зберігаємо у зміну data
        self.conn.close()
        return data