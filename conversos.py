import codecs

def convert_to_unicode(file_path):
    with codecs.open(file_path, 'r', 'ISO-8859-1') as f:
        lines = f.readlines()

    with codecs.open(file_path, 'w', 'utf-8') as f:
        for line in lines:
            for char in line:
                if ord(char) > 127:
                    f.write('\\u{0:04x}'.format(ord(char)))
                else:
                    f.write(char)

# Substitua 'path_to_file' pelo caminho do seu arquivo .properties
convert_to_unicode('path_to_file')