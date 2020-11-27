#!/usr/bin/env python2
import sys
import os
import re
import uuid


EXTENSIONS = ('.csv')
UUID_PATTERN = r'\b[0-9a-f]{8}\b-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-\b[0-9a-f]{12}\b'


def parse(src_path, dst_path):
    print 'This is a parser from UUID to int.'
    for root, dirs, files in os.walk(src_path):
            for file in files:
                
                is_replaced = False
                ext = os.path.splitext(file)[1].lower()

                if len(ext) > 0 and ext in EXTENSIONS:
                    input_file_name = os.path.join(root, file)
                    tmp_file_name = os.path.join(dst_path, file) + '.tmp'
                    input_file = open(input_file_name, 'r')
                    tmp_file = open(tmp_file_name, 'w+')

                    for line in input_file:
                        found = re.search(UUID_PATTERN, line)
                        while found:
                            is_replaced = True
                            replace = str(uuid.UUID(found.group(0)).int)
                            line = line.replace(found.group(0), replace, 1)
                            found = re.search(UUID_PATTERN, line)
                        tmp_file.write(line)

                    input_file.close()
                    tmp_file.close()

                    if is_replaced:
                        output_file_name = os.path.splitext(tmp_file_name)[0] 
                        if os.path.exists(output_file_name):
                            os.remove(output_file_name)
                        os.rename(tmp_file_name, output_file_name)
                    else:
                        if os.path.exists(tmp_file_name):
                            os.remove(tmp_file_name)