#!/bin/bash
if [[ $EUID -ne 0 ]]; then
   echo "This script must be run as root" 
   exit 1
fi

echo "Creating network..."
docker network create sim-one

cwd=`pwd`

#Build Victim 1 Image (This will also act as a server/gateway)
cd $cwd
echo $cwd
cd $cwd/Victim1
echo "Building Victim1..."
docker build --network=sim-one -t "s1-v1" .

#Build Victim 2 Image
cd $cwd
echo $cwd
cd $cwd/Victim2
echo "Building Victim2..."
docker build --network=sim-one -t "s1-v2" .

#Build Hacker 1 Image
cd $cwd
echo $cwd
cd $cwd/Hacker1
echo "Building Hacker1..."
docker build --network=sim-one -t "s1-h1" .

#Build Vulnerable Web App
cd $cwd
echo $cwd
cd $cwd/VulnerableWebApp1
echo "Building VulnerableWebApp1..."
docker build --network=sim-one -t "s1-vwa1" .
echo "Done building images."

echo "Starting containers.."
docker run -d --rm --mac-address="00:00:00:00:00:01" --name "s1-v1" -h "s1-v1" --network="sim-one" -it --entrypoint=/bin/bash s1-v1
docker run -d --rm --mac-address="00:00:00:00:00:02" --name "s1-v2" -h "s1-v2" --network="sim-one" -it --entrypoint=/bin/bash s1-v2
docker run -d --rm --mac-address="00:00:00:00:00:03" --name "s1-h1" -h "s1-h1" --network="sim-one" -it --entrypoint=/bin/bash s1-h1
docker run -d --rm --mac-address="00:00:00:00:00:04" --name "s1-vwa1" -h "s1-vwa1" --network="sim-one" -it --entrypoint=/main.sh s1-vwa1
#docker run --rm --mac-address="00:00:00:00:00:04" --network="sim-one" -it -p 80:80 vulnerables/web-dvwa (For the vulnerable web application)
