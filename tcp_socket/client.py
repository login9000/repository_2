# -*- coding: utf-8 -*-

import re
import socket
import traceback
import time


result = b''
err = ''
port = 23423
data = 'Hello world!'
counter_request = 0

_t3 = time.time()
_counter_request = 0
_number_of_requests_per_second = 0
_d_min = 10
_d_max = 0
y = 0
_d_sum = 0
is_first_second = False

for _ in range(1000):

	try:
		
		result = b''
		err = ''
		_t1 = time.time()

		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(5)
		sock.connect(('127.0.0.1', port))
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

		_t2 = time.time()

		counter_request += 1
		_counter_request = counter_request

		y += 1

		d = _t2 - _t1
		_d_sum += d

		if _d_min > d:
			_d_min = d

		if _d_max < d:
			_d_max = d

		if time.time() - _t3 >= 1: # 
			is_first_second = True
			_t3 = time.time()
			print('min: '+str(_d_min)+', max: '+str(_d_max)+', average: '+str((_d_sum) / y)+', number of requests per second: '+str(_counter_request - _number_of_requests_per_second))
			print('result:', result)
			print('------------------------------------------')
			_number_of_requests_per_second = _counter_request
			y = 0
			_d_sum = 0

	except Exception:

		print('err:', re.sub('\r?\n', '', traceback.format_exc().strip()))
		break

	finally:
		
		try:
			sock.close()
		except:
			pass

if not is_first_second:
	print('min: '+str(_d_min)+', max: '+str(_d_max)+', average: '+str((_d_sum) / y)+', number of requests per second: '+str(_counter_request - _number_of_requests_per_second))
	print('result:', result)
	print('------------------------------------------')

