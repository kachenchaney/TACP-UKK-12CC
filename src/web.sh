#!/bin/bash

RDSmountpoint="database-1.c2tochjn7qjp.us-east-1.rds.amazonaws.com"
UsernameRDS="admin"
passwordRDS="admin123"
DNSEFS="fs-0ef13ba7dec46de8b.efs.us-east-1.amazonaws.com"
EFSid="fs-0ef13ba7dec46de8b"

sudo apt update
curl -sL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install nodejs -y

sudo apt-get install rsync build-essential git mysql-client -y

sudo apt install binutils -y
git clone https://github.com/aws/efs-utils
cd efs-utils
./build-deb.sh
sudo apt-get -y install ./build/amazon-efs-utils*deb

cd /home/ubuntu
sudo mkdir efs
sudo mount -t efs -o tls $EFSid:/ efs
df -h

cd /home/ubuntu/ && git clone https://github.com/adinur21/ukk.git
cd ukk/ && npm install

npm install --save express
npm install -g nodemon
npm install -g cors
npm install -g body-parser

cd /home/ubuntu/ukk/src/model/
sudo cat <<EOF >dbConnection.js
const mySql = require("mysql")

const db = mySql.createPool({
  host: "$RDSmountpoint",
  user: "$UsernameRDS",
  password: "$passwordRDS",
  database: "cloud_api"
})

exports.db = db;
EOF

cd /home/ubuntu/efs/
sudo rsync -azP /var/log/ $DNSEFS