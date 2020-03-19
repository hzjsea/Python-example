#!/bin/sh
state="established"
timestamp=`date "+%d/%b/%Y:%X"`
tmpfile="h"
hostname=$(hostname)

echo "'"  > $tmpfile.json
#ss2 -4itn state $state | awk '{ if(NR > 1 && $3 !~ /127.0.0.1/ && $4 !~ /192.168./) {
# 直接过滤端口为 80 443 8100 状态为established的接口
ss2 -4itn state $state dport = :80 or sport = :80 or dport = :443 or sport = :433 or sport = :8100 or dport = :8100 |
awk '{ if(NR > 1 && $3 !~ /127.0.0.1/ ) {
		line=$0; getline; if($0~/minrtt/) print line""$0
  	}
}' |
awk '{
	split($3,src,":"); Saddress=$3;
	split($4,dst,":"); Daddress=dst[1];Dport=dst[2];
	node_type="network-attack";
        split($8,a,"[:/]");
        split($13,b,"[:/]");
        if ($0 ~ /retrans:/){
                split($0,c,"retrans:");
                gsub("/.*","",c[2]);
                Retrans=c[2]
        }else{
                Retrans=0
        };
        if ($0 ~ /send/){
                split($0,d,"send");
                gsub("bps.*","",d[2]);
                if(d[2] ~ /K/) {
                        gsub("K","",d[2]);
                        Send=d[2]/1000
                }
                else if(d[2] ~ /M/) {
                        gsub("M","",d[2]);
                        Send=d[2]
                }
                else {
                        Send=d[2]
                }
        }; 
        print(Daddress,Saddress,a[2],b[2],Retrans,Send)
}' |
awk '{
    a[$2]++;d[$2]=$1;rtt[$2]+=$3;cwnd[$2]+=$4;retrans[$2]+=$5;send[$2]+=$6
    }END{
        for (i in a){ 
            z=split(i,q,":")
            nums=0
            if (retrans[i]/a[i] != 0) {
                    nums=int(retrans[i]/a[i]+1)
                    }
            else{
                nums=retrans[i]/a[i]
          }
            printf("{\
\"Daddress\":\"%s\", \
\"Saddress\": \"%s\",\
\"SPort\": \"%s\",\
\"rtt\": %d,\
\"cwnd\": %d,\
\"Retrans\": %d,\
\"send\": %d,\
\"total\": %d,\
\"line_state\": \"%s\",\
\"type\": \"%s\",\
\"node_type\": \"%s\",\
\"timestamp\": \"%s +0800\",\
\"hostname\": \"%s\"\
}\n",
                    d[i],q[1],q[2],rtt[i]/a[i],cwnd[i]/a[i],nums,send[i]/a[i],a[i],"ESTAB","bbr","network-attack","'$timestamp'","'$hostname'")}
}' >> $tmpfile.json

echo "'" >> $tmpfile.json
