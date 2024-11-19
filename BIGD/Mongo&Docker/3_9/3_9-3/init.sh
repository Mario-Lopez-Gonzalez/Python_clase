#!/bin/bash


sudo docker exec configsvr1 sh -c "mongosh < /scripts/configserver-init.js"
sudo docker exec shard1a sh -c "mongosh < /scripts/shard1-init.js"
sudo docker exec shard2a sh -c "mongosh < /scripts/shard2-init.js"
sleep 20
sudo docker exec router1 sh -c "mongosh < /scripts/router-init.js"
