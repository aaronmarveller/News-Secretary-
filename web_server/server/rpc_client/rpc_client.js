const jayson = require('jayson');

// create a client
const client = jayson.client.http({
	port: 4040,
	hostname: 'localhost'
});

function add(a, b, callback) {
	client.request('add', [a, b], (err, response) => {
		if (err) throw err;
		console.log(response.result);
		callback(response.result);
	});
}

function logNewsClickForUser(userId, newsId) {
	client.request('logNewsClickForUser', [userId, newsId], (err, response) => {
		if (err) throw err;
		console.log(response.result);
	});
}

module.exports = {
	add: add,
	logNewsClickForUser: logNewsClickForUser
}
