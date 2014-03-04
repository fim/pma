Domains
=======

user = mail
password = passw0rd
dbname = mail
hosts = localhost
query = SELECT domain FROM domain WHERE domain = '%s'

User
====

user = mail
password = passw0rd
dbname = mail
hosts = localhost
query = SELECT
CONCAT(SUBSTRING_INDEX(email,'@',-1),'/',SUBSTRING_INDEX(email,'@',1),'/') FROM user WHERE email = '%s' AND active=1

Alias
=====

user = mail
password = passw0rd
dbname = mail
hosts = localhost
query = SELECT destination FROM alias WHERE source = '%s' AND active=1

Transport
=========

user = mail
password = passw0rd
dbname = mail
hosts = localhost
query = SELECT transport FROM transport WHERE domain = '%s'
