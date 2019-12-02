const client = require('./rpc_client');

// invoke 'add'
client.add(1, 2, result => { console.assert(result === 3) });

// invoke "logNewsClickForUser"
client.logNewsClickForUser('test_user', 'test_news');
