from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = '138.41.20.102'
app.config['MYSQL_PORT'] = 53306
app.config['MYSQL_DB'] = 'w3schools'
app.config['MYSQL_USER'] = 'ospite'
app.config['MYSQL_PASSWORD'] = 'ospite'

mysql = MySQL(app)



@app.route('/')
def homepage():
    return render_template('homepage.html',titolo = "Home")
@app.route('/products')
def prodotti():
    cursor = mysql.connection.cursor()
    query = 'SELECT * FROM products'
    cursor.execute(query)
    prodotti = cursor.fetchall()
    cursor.close()
    return render_template('products.html',titolo = "Prodotti",prodotti=prodotti)
@app.route('/categories/<CatId>')
def categories(CatId):
    cursor = mysql.connection.cursor()
    query = 'SELECT * FROM categories WHERE CategoryID = %s'
    cursor.execute(query,(CatId,))
    categorie = cursor.fetchall()
    cursor.close()
    return render_template('categories.html',titolo = 'Categorie',categorie=categorie,CatId=CatId)


if __name__ == '__main__':
    app.run(debug=True)
