#!/usr/bin/env python2
import sys
import os
import re
import uuid


EXTENSIONS = ('.csv')
UUID_PATTERN = '\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b'


def parse(src_path, dst_path):
    print 'This is a parser from UUID to int.'
    for root, dirs, files in os.walk(src_path):
            for file in files:
                is_replaced = False
                ext = os.path.splitext(file)[1].lower()
                if len(ext) > 0 and ext in EXTENSIONS:
                    i_name = os.path.join(root, file)
                    o_name = os.path.join(dst_path, file) + '.tmp'
                    fi = open(i_name, 'r')
                    fo = open(o_name, 'w+')

                    for line in fi:
                        found = re.search(r'\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b', line)
                        while found:
                            is_replaced = True
                            replace = str(uuid.UUID(found.group(0)).int)
                            line = line.replace(found.group(0), replace, 1)
                            found = re.search(r'\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b', line)
                        fo.write(line)

                    fi.close()
                    fo.close()
                    if is_replaced:
                        if os.path.exists(os.path.splitext(o_name)[0]):
                            os.remove(os.path.splitext(o_name)[0])
                        os.rename(o_name, os.path.splitext(o_name)[0])
                    else:
                        if os.path.exists(o_name):
                            os.remove(o_name)