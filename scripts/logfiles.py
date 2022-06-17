#!/bin/python3

import re

# regex for .jsfiles
rgx_js = re.compile(r'([A-Za-z0-9._-]+\.js)')

if __name__ == '__main__':
    '''
    Open logfile, search for regex line by line
    and add founds to set(). Print sorted set().
    '''

    with open('access_log.txt', 'r') as logfile:
        js_files = set()

        for line in logfile:
            _found = re.search(rgx_js, line)
            if _found:
                    js_files.add(_found.group())

        for i in sorted(js_files):
            print(i)