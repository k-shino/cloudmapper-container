#!/bin/bash

ACCESS_KEY="${ACCESS_KEY:-AAAAA}"
SECRET_KEY="${SECRET_KEY:-AAAAA}"
NAME="${NAME:-demo}"
ID="${ID:-123456789012}"

sed -i -e "s/AAAAA/${ACCESS_KEY}/" /root/.aws/credentials
sed -i -e "s/BBBBB/${SECRET_KEY}/" /root/.aws/credentials 

python3 cloudmapper.py configure add-account --name $NAME --id $ID --default true
python3 cloudmapper.py collect
python3 cloudmapper.py prepare --no-internal-edges
python3 cloudmapper.py webserver --public

