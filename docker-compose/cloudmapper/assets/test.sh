#!/bin/bash

if [ $# -eq 0 ]; then
    echo "cidr: too few arguments" 1>&2
    echo "cidr [add|remove] CIDR CIDR_NAME" 1>&2
    exit 1
fi

if test $1 != "add" -a $1 != "remove" ; then
  echo No order is specified.
  exit 1
fi



