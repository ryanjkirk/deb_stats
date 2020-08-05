#!/usr/bin/env python3

import argparse
import urllib.request
import gzip
import subprocess
import os

# hard code mirror location
mirror = 'http://ftp.uk.debian.org/debian/dists/stable'

# define our command-line options and parse them
desc = 'Rank top 10 deb packages by number of files for a particular architcture'
parser = argparse.ArgumentParser(description=desc)
parser.add_argument('-a', '--arch',
                    type=str,
                    help='Define your target system architecture; e.g., amd64',
                    required=True)

# set arg as a var
args = parser.parse_args()
arch = args.arch

# concatenate supplied argument to create full url to fetch
full_url = mirror + '/main/Contents-' + arch + '.gz'

# TODO: use tempfile module instead of this
tmp_file1 = './tmp-Contents'
tmp_file2 = tmp_file1 + '.gz'

def rmtmpfiles():
    if os.path.exists(tmp_file1):
        os.remove(tmp_file1)
    if os.path.exists(tmp_file2):
        os.remove(tmp_file2)

rmtmpfiles()

# retrieve Contents file and save to tmp location
urllib.request.urlretrieve(full_url, tmp_file2)

# shell out to read and sort the file (requires bash syntax)
# TODO: pass tmpfile var to shell (or rewrite in pure python)
shell_cmd = '''
    gunzip "./tmp-Contents.gz"
    ( echo "Rank Files Package"
        cat tmp-Contents \
        | awk '{print $2}' \
        | sort \
        | uniq -c \
        | sort -rnk 1 \
        | head \
        | awk '{ printf "%d\\t%s\\n", NR, $0 }' \
    ) \
    | column -t
'''
subprocess.run([shell_cmd, tmp_file2], shell=True, executable='/bin/bash')

rmtmpfiles()
