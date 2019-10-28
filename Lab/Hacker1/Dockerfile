#Hacker 1 Dockerfile
FROM ubuntu:16.04

RUN apt-get update -y
RUN apt-get install -y net-tools iputils-* tcpdump python3 python3-pip apt-utils openssh-server

RUN apt-key adv --keyserver pool.sks-keyservers.net --recv-keys ED444FF07D8D0BF6
RUN echo 'deb http://http.kali.org/kali kali-rolling main contrib non-free' >> /etc/apt/sources.list
RUN apt-get update -m

#RUN apt-get install -y dnsenum dnsmap dnsrecon dnstracer dnswalk dotdotpwn enum4linux enumiax exploitdb fierce firewalk fragroute fragrouter golismero goofile lbd masscan metagoofil nmap p0f parsero recon-ng set smtp-user-enum snmpcheck sslsplit sslstrip sslyze thc-ipv6 theharvester tlssled urlcrazy xplico ismtp intrace hping3

#RUN apt-get install -y bbqsql bed cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch copy-router-config doona dotdotpwn greenbone-security-assistant jsql lynis nmap ohrwurm openvas-cli openvas-manager openvas-scanner oscanner sfuzz sidguesser siparmyknife sqlmap sqlninja sqlsus thc-ipv6 tnscmd10g unix-privesc-check yersinia

#RUN apt-get install -y apache-users arachni bbqsql burpsuite cutycapt davtest dirb dirbuster funkload jboss-autopwn joomscan jsql padbuster paros parsero plecost recon-ng skipfish sqlmap sqlninja sqlsus uniscan cat Dwebscarab websploit wfuzz wpscan xsser zaproxy

#RUN apt-get install -y burpsuite dnschef fiked hamster-sidejack hexinject iaxflood inviteflood ismtp mitmproxy ohrwurm protos-sip rebind responder rtpbreak rtpinsertsound rtpmixsound sctpscan siparmyknife sipp sipvicious sniffjoke sslsplit sslstrip thc-ipv6 voiphopper webscarab wifi-honey xspy yersinia

#RUN apt-get install -y cryptcat cymothoa dbd dns2tcp http-tunnel httptunnel intersect nishang polenum powersploit pwnat ridenum sbd u3-pwn webshells weevely

#RUN apt-get install -y casefile cutycapt dos2unix dradis keepnote magictree metagoofil nipper-ng pipal

#RUN apt-get install -y armitage backdoor-factory cisco-auditing-tool cisco-global-exploiter cisco-ocs cisco-torch crackle jboss-autopwn linux-exploit-suggester set shellnoob sqlmap thc-ipv6 yersinia beef-xss

#RUN apt-get install -y binwalk bulk-extractor chntpw cuckoo dc3dd ddrescue dumpzilla extundelete foremost galleta guymager iphone-backup-analyzer p0f pdf-parser pdfid pdgmail peepdf volatility xplico

#RUN apt-get install -y dhcpig funkload iaxflood inviteflood ipv6-toolkit mdk3 reaver rtpflood slowhttptest t50 termineter thc-ipv6 thc-ssl-dos

#RUN apt-get install -y acccheck burpsuite cewl chntpw cisco-auditing-tool cmospwd creddump crunch findmyhash gpp-decrypt hash-identifier john johnny keimpx maskprocessor multiforcer ncrack oclgausscrack pack patator polenum rainbowcrack rcracki-mt rsmangler statsprocessor thc-pptp-bruter truecrack webscarab wordlists zaproxy

#RUN apt-get install -y apktool dex2jar python-diStorm3 edb-debugger jad javasnoop JD OllyDbg smali Valgrind YARA

#RUN apt-get install -y android-sdk apktool arduino dex2jar sakis3g smali

RUN pip3 install --upgrade pip
RUN pip3 install scapy
ADD python/ /root/python/
RUN cd;ls *

RUN cat /sys/class/net/eth0/address > ~/mac-address
RUN ifconfig eth0 | grep 'inet addr' | cut -d: -f2 | awk '{print $1}' > ~/ip-address
CMD ["/bin/bash"]