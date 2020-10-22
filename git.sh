#!/bin/bash

if [ ! -z $1 ]; then
	git add -A
	git cam "$1"
	git push
else
	echo "No Commit Massage, USE $0 'Massage'"
fi
