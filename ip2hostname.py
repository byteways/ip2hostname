#!/usr/bin/env python
# -*- coding : UTF-8 -*-

import commands
import sys

IP_LIST = 'ip_list.txt'
OUT_FILE = 'output.txt'

import time
def get_hostname_by_ip(ip):
    """
    get_hostname_by_ip
    :param ip:
    :return:
    """
    hostname = 'localhost'
    try:
        output = commands.getoutput('nslookup ' + ip)
        if output.count('name') > 0:
            print output
            try:
                hostname = output[output.index('name') + 7: -2]
            except Exception as e:
                # hostname = output[output.index('名称') + 7: -2]
                pass

    except Exception as e:
        pass

    return hostname


if __name__ == '__main__':

    if len(sys.argv) > 1:
        IP_LIST = sys.argv[1]
    with open( IP_LIST, 'r') as infile:
        for line in infile:
            time.sleep(1)
            print 'line', line
            line = line.replace('\r', '').replace('\n', '')
            hostname = get_hostname_by_ip(line)

            if hostname.count('localhost') > 0:
                time.sleep(10)
                hostname = get_hostname_by_ip(line)

            row = line + '\t' + hostname + '\r\n'
            with open(OUT_FILE, 'a+') as outfile:
                outfile.write(row)
