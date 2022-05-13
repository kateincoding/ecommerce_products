# ecommerce
eCommerce of a minimarket

# DEPLOY
IaaS Oracle
Ubuntu Nginx gunicorn
domain:
* [http://test.katein.tech/bsale_test/](http://test.katein.tech/bsale_test/)

apis:
* [http://test.katein.tech/api/v1/status](http://test.katein.tech/api/v1/status)
* [http://test.katein.tech/api/v1/products/category/<category_id=5>](http://test.katein.tech/api/v1/5)

Listado de endpoints:
##|Endpoint|Description
---|---|---
0|[http://test.katein.tech/api/v1/status](http://test.katein.tech/api/v1/status)|Status OK if the api is working
1|[http://test.katein.tech/api/v1/stats](http://test.katein.tech/api/v1/stats)|Stats of how many products and categories exists
2|[http://test.katein.tech/api/v1/products](http://test.katein.tech/api/v1/products)|List of products
3|[http://test.katein.tech/api/v1/products/<product_id=5>](http://test.katein.tech/api/v1/products/5)|Retrieves 1 product
4|[http://test.katein.tech/api/v1/products/category/<category_id=5>](http://test.katein.tech/api/v1/products/category/5)|List of products by one category selected, in this case is an example of the category_id=5

# SET ENV

```
sudo apt update
sudo apt install mysql-server
sudo systemctl start mysql.service
sudo apt-get install libmysqlclient-dev
sudo pip3 install mysqlclient
pip3 install -r requeriments.txt
```

# API INVENTORY: python, sqlalchemy, flask

First, I make a duplication of de data in a localrepostiry
chargue the script to "mysql"

Fase 0: crear una copia local del mysql en tu local

```
cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
```
Set the enviroment variables

Porfavor, customize los valores de acuerdo a los valores que tendra en su mysql
```
export DB_USER=xxx
export DB_PASSWORD=xxxx
export DB_HOST=localhost
export DB_DATABASE=xxxx
```
Agregar datos a la base de datos:
```
cat bsale_test.sql | mysql -hlocalhost -ubsale_test -pbsale_test bsale_test
```

Fase1: Backend: basemodel + api finished
* How to run

Terminal 1:
```
./run_api
```

Fase2: Web_dynamic

# FRONTEND: JS vainilla unido a Flask

* How to run:
```
python3 -m web_dynamic.product_filters
```
