PMA - Postfix Mail Accountant
=============================

This is a simple tool to help manage accounting backends for simple mail
servers (primarily tested with postfix/dovecot).

Requirements
-------------

 * Python 2.X (tested with 2.7)

Installation
-------------

Either clone locally by running:

```sh
git clone https://github.com/fim/pma
```

and then install if necessary:

```sh
python setup.py install
```

Or simply run:

```sh
pip install https://github.com/fim/pma/tarball/master
```

Usage
-----
Initialize the database:

```sh
> pma init
```

Create domains:

```sh
> pma domain add
```

Create user accounts:

```sh
> pma user add
```

Create aliases:

```sh
> pma alias add
```

Create transport rules:

```sh
> pma transport add
```

List existing records:

```sh
> pma domain list
```

Delete existing records:

```sh
> pma domain delete
```

Database Support
----------------

Currently sqlite3, mysql and psql are supported.

 - SQLite3

 Requires python compiled with sqlite support.

 Example:

 ```sh
 > pma -b sqlite -s "dbname=/etc/mail/mail.db" init
 Initializing database
 > pma -b sqlite -s "dbname=/etc/mail/mail.db" domain add
 ...
 ```

 - MySQL

 Requires python-mysql installed

 Example:

 ```sh
 > pma -b mysql -s "host=127.0.0.1;user=dbadmin;pass=dbpass;dbname=mail" init
 Initializing database
 > pma -b mysql -s "host=127.0.0.1;user=dbadmin;pass=dbpass;dbname=mail" domain add
 ...
 ```
 - PSQL

 Requires psycopg2 installed

 Example:

 ```sh
 > pma -b pgsql -s "host=127.0.0.1;user=dbadmin;pass=dbpass;dbname=mail" init
 Initializing database
 > pma -b pgsql -s "host=127.0.0.1;user=dbadmin;pass=dbpass;dbname=mail" domain add
 ...
 ```
