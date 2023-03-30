#!/bin/bash

if [ .$SERVER_ADDR = . ]
then
	SERVER_ADDR=127.0.0.1:38888
fi
cid=$1
if [ .$cid = . ]
then
    echo Please give me cid
    exit
fi

postnotify() {
    while read -r line
    do
        if [ "${line:0:14}" = 'Subject: Slurm' ]
        then
            echo $(date) $line
			curl -XPOST --data "${line:9:-1} Time $(date)" http://$SERVER_ADDR/$cid
		fi
    done
}

if [ ! -f /var/mail/$(whoami) ]
then
    mail -s 'init mail' $(whoami) </dev/null
fi

tail -f /var/mail/$(whoami) | postnotify
