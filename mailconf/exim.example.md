Exim Configuration
==================

${lookup mysql{SELECT domain FROM domain WHERE domain ='${quote_mysql:$domain}' AND active=1}{$value}fail}
