const net = require('net');

var app_version = '1.0',
		port = 23423;

async function handler(socket, body){
	socket.write(body+'\r\n');
}

(async () => {
	try{
		console.log('echo_server_tcp_socket v'+app_version);
		var server = net.createServer(function(socket) {
			var body = '';
			socket.on('data', function(data) {
				var data = String(data);
				var ex = data.split(/\n/);
				var len = ex.length;
				for(var i = 0; i < len; i++){
					if(ex[i] ){
						body += ex[i];
						if(i + 1 < len){
							handler(socket, body);
							body = '';
						}
					}
				}
			});
		});
		server.listen('127.0.0.1:'+port);
		server.on('listening', function() {
			console.log('listening 127.0.0.1:'+port+'...');
		});
	}catch(err){
		var err = (err.stack ? String(err.stack) : err);
		console.log(err.replace(/\r?\n/g, ' '));
	}
})();


