# CyberSecurity

## table of contents

1. [setup project](#setup-project)
2. [passwords](#passwords)
3. [webpentesting](#webpentesting)

## setup project

To set up the project run the following command in the terminal:\
`git clone https://github.com/pietjuu/cyberSecurity.git` \
The projects will be stored in different directories named: passwords and webpentesting
and in every directory there will be a folder that is named wordlist with some wordlists in it.
These are optional if you prefer to use your own wordlist.

## passwords

In this direcotry there are 3 scripts:

1. create_wordlist.py
2. password_checker_brutefirce.py
3. password_checker_entropy.py

### create_wordlist.py

This script will hash every word in the file wordlist.txt
and store it in a new file called md5.txt.

### password_checker_bruteforce.py

This script will check if the password is in the wordlist. It first creates a hash out of the given password and
then checks if it can find the hash in the prevouis created wordlist. If it finds the hash it will print the password.

### password_checker_entropy.py

This script will check how random the password is.
it will give you a score, if your score is lower than 50 then you have a weak password, if your score is between 50
and 85 then you have a moderate password. If your score is between 85 and 100 then you have a strong password. And
finally if you score over 100 then you have a very strong password.

## webpentesting

In this direcotry there are 2 scripts:

1. parameter_fuzzer.py
2. subdomain_enumeration_with_scanning.py

### parameter_fuzzer.py

This script will fuzz the parameters of a given url.
It will first check if the url is valid, and then it will fuzz the parameters of the url.
It will print the url with the parameters and the status code of the url.

### subdomain_enumeration_with_scanning.py

This script will enumerate the subdomains of a given url. It will first check if the url is valid, and then it will
enumerate the subdomains of the url. ANd look for hidden directories. It will print the subdomains and the hidden
directories and files.
