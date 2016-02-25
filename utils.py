import codecs

MALE_LABEL = 'M'
FEMALE_LABEL = 'F'


def read_lines(file_name):
    return codecs.open(file_name, encoding='utf-8').read().splitlines()
