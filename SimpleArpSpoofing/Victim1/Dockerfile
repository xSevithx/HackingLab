#Victim 1 Dockerfile
FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y net-tools iputils-* tcpdump python3 python3-pip apt-utils openssh-server
RUN cat /sys/class/net/eth0/address > ~/mac-address
RUN ifconfig eth0 | grep 'inet addr' | cut -d: -f2 | awk '{print $1}' > ~/ip-address
CMD ["/bin/bash"]