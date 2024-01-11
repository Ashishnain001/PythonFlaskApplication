Flask Application setup 
Fresh machine setup - 
copy file of Flaskapp application.
Run command- 
sudo pip install -r requirement.txt
Install or configure database (mongodb , mysql , postgres)
Note - Changes to be done in app.py file regarding username and password.
Mysql -
To install mysql -
sudo apt-get upgrade
sudo apt-get install mysql-server
sudo systemctl start mysql
sudo systemctl enable mysql

mysql -u root -p
create database cavisson; -> create db

CREATE USER 'cavisson'@'localhost' IDENTIFIED BY 'cavisson’; -> create user
Issues- 

File "/home/cavisson/.local/lib/python3.8/site-packages/MySQLdb/__init__.py", line 24, in <module>
    version_info, _mysql.version_info, _mysql.__file__
NameError: name '_mysql' is not defined

Solution - sudo apt-get install libmysqlclient-dev

ERROR 1045 (28000): Access denied for user 'cavisson'@'localhost' (using password: YES)
Login through root user - mysql -u root -p
grant all privileges on . to 'cavisson'@'localhost';
Login through cavisson user now - 
->mysql -u cavisson -p
->show databases;
->create database cavisson; -> create db
->use my_first_sql;
sudo apt-get install mysql-server
for mysql issue  create user
sudo mysql
CREATE USER 'cavisson'@'localhost' IDENTIFIED BY 'Cavisson@123';
GRANT ALL PRIVILEGES ON . TO 'cavisson'@'localhost' WITH GRANT OPTION;

To create table in mysql 
mysql -u cavisson -p <my_first_db.sql
Mongodb -
To create user
mongo admin --eval 'db.createUser({user: "cavisson", pwd: "Cavisson!", roles:["root"]})'
If new machine is there then better remove it and then install
Uninstall - How To Uninstall MongoDB
Install - https://www.digitalocean.com/community/tutorials/how-to-install-mongodb-on-ubuntu-18-04-source

Postgres -
ModuleNotFoundError: No module named 'psycopg2'
sudo apt-get install libpq-dev 
pip install psycopg2

To uninstall -
https://www.commandprompt.com/education/how-to-uninstall-postgresql-from-ubuntu/

To Install Postgres-

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04

To login without password -
psql
Now run adduser

sudo apt install postgresql postgresql-contrib
sudo systemctl start postgresql.service
sudo -u postgres createuser --interactive
Enter role as cavisson and y for superuser

Create user -
create user “username” with superuser password 'cavisson';
Create db for user -
 createdb -h localhost -p 5432 -U user database


psycopg2.OperationalError: FATAL:  password authentication failed for user "cavisson"
FATAL:  password authentication failed for user "cavisson"

Issues -

psycopg2.OperationalError: FATAL:  role "test" does not exist

sudo systemctl start postgresql.service
sudo -i -u postgres
psql
\du

CREATE ROLE new_role_name;
\du

sudo -i -u postgres
createuser --interactive

https://www.digitalocean.com/community/tutorials/how-to-use-roles-and-manage-grant-permissions-in-postgresql-on-a-vps-2#creating-roles-from-within-postgresql

