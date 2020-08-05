#! /usr/bin/env bash

arch=$1
mirror="http://ftp.uk.debian.org/debian/dists/stable"

if [[ -z $arch ]]; then
    echo "Please supply the architecture as a parameter."
    exit 1
fi

( echo "Rank Files Package"
  curl -s "${mirror}"/main/Contents-"${arch}".gz \
    | gunzip \
    | awk '{print $2}' \
    | sort \
    | uniq -c \
    | sort -rnk 1 \
    | head \
    | awk '{ printf "%d\t%s\n", NR, $0 }' \
  ) \
    | column -t
