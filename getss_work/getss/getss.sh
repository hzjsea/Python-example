#!/bin/bash
DIR="/root/getss/"
chmod +x $DIR/command/split
chmod +x $DIR/command/ss091226
cp $DIR/command/split /usr/bin/
mkdir -p $DIR/{log,tmpfiles}
$DIR/command/ss091226 -itn >  $DIR/log/all.txt

python $DIR/general_json.py > $DIR/log/log.txt

#curl -XPOST http://chopper.x.upyun.com:4000/v2/log/repo/cdn-common  -H 'Apikey:1ndT12Jj85UsXQdat2KOMBEiiT28rsIQ' -H "Content-Type:application/json" -T $DIR/log/log.txt -v -D-
