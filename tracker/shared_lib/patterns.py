import re


SA_UNIQ_PATTERN = re.compile(r'Duplicate entry \'(?P<value>[\w\-_\.@]+)\' for key \'(?P<field_name>[\w\-_]+)\'$')
