from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)


app.config['MYSQL_HOST'] = "138.41.20.102"
app.config['MYSQL_PORT'] = 53306  
app.config['MYSQL_USER'] = "ospite"
app.config['MYSQL_PASSWORD'] = "ospite"
app.config['MYSQL_DB'] = "w3schools"
mysql = MySQL(app)
@app.route('/')
def homepage():
    return render_template('homepage.html',titolo ="home")

@app.route('/products')
def products():
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM products"
    cursor.execute(query)
    miao = cursor.fetchall()
    cursor.close()
   
    return render_template('products.html',titolo = "products",miao=miao)

@app.route('/categories/<int:catID>')
def categories(catID):
    cursor = mysql.connection.cursor()
    query = "SELECT * FROM categories"
    cursor.execute(query)
    miao = cursor.fetchall()
    miao2 = []
    for i in miao:
        if int(i[0]) == catID:
            miao2.append(i)
    cursor.close()
    return render_template('categories.html',titolo ="categories",catID=catID,miao2=miao2)


if __name__ == '__main__':
    app.run(debug=True)
