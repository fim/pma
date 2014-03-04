Dovecot-sql config
==================

driver=mysql
connect = host=localhost dbname=mail user=mail password=passw0rd

# PgSQL
#driver = pgsql
#connect = host=localhost dbname=mail user=mail password=passw0rd

# SQLite3
#driver = sqlite
#connect = /path/to/mail.db

# /var/vmail is the root of the Virtual Maildirs
# /var/vmail/example.com/username is the homedir of vmail users
# 5000 id/gid is the details of the user owning the vmail folder
user_query = SELECT '/var/vmail/%d/%n' as var, 'maildir:/var/vmail/%d/%n' as mail, 5000 AS uid, 5000 AS gid FROM users WHERE email = '%u' and active = 1
password_query = SELECT email as user, password, '/var/vmail/%d/%n' as userdb_var, 'maildir:/var/vmail/%d/%n' as userdb_mail, 5000 as userdb_uid, 5000 as userdb_gid FROM users  WHERE email = '%u' and active = 1
