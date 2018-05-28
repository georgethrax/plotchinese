def print_unicode_list(a):
    print str(a).decode('unicode-escape')


def print_str_list(a):
    print str(a).decode('string-escape')


def print_list(a, decode_type = 'unicode-escape'):
	print str(a).decode(decode_type)

    
if __name__ == '__main__':
	langs = [
		'Hello, world!',
		'你好，世界！',
		'こんにちは世界',
		u'Hello, world!',
		u'你好，世界！',
		u'こんにちは世界'
	]
	print(langs)
	print_unicode_list(langs)
	print_str_list(langs)
	print_list(langs)
