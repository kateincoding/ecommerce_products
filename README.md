# ecommerce
eCommerce of a minimarket

# API INVENTORY

First, I make a duplication of de data in a localrepostiry
chargue the script to "mysql"

Fase 0: crear una copia local del mysql en tu local

```
cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p
cat bsale_test.sql | mysql -hlocalhost -ubsale_test -pbsale_test bsale_test
```

Fase1: Backend: basemodel + api finished
* How to run

Terminal 1:
```
./run_api
```

Fase2: Web_dynamic
* How to run:
```
python3 -m web_dynamic.product_filters
```
