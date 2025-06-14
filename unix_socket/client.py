# -*- coding: utf-8 -*-

import re
import socket
import traceback


result = b''
err = ''
echo_server_unix_socket = '/tmp/echo_server_unix_socket.sock'
data = 'Hello world!'

try:
	
	sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
	sock.settimeout(5)
	sock.connect(echo_server_unix_socket)
	sock.sendall((data+'\n').encode('utf-8'))
	
	while True:
		_data = sock.recv(1024)
		if len(_data) == 0:
			break
		result += _data
		try:
			if re.search(b'(\r|\n|\r\n)$', _data):
				break
		except Exception:
			pass
	result = result.decode('utf-8')

except Exception:

	print('err:', re.sub('\r?\n', '', traceback.format_exc().strip()))

finally:
	
	try:
		sock.close()
	except:
		pass

print('result:', result)


