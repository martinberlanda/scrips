const logTemplates = [
    'Processing request #{id} from IP: {ip}...',
    'Database query #{id} returned {count} rows...',
    'User {username} logged in...',
    'User {username} failed to login due to incorrect password...',
    'Packet #{id} received from IP: {ip}...',
    'Packet #{id} sent to IP: {ip}...',
    'Successfully written {size} bytes to disk...',
    'Failed to write {size} bytes to disk due to insufficient space...',
    'Started service {serviceName}...',
    'Failed to start service {serviceName} due to missing dependencies...',
    'CPU utilization at {percent}%...',
    'Memory utilization at {percent}%...',
    'Disk utilization at {percent}%...',
    'Network interface {interfaceName} up...',
    'Network interface {interfaceName} down...',
    'Connection to database {dbName} established...',
    'Connection to database {dbName} lost...',
    'Detected {count} intrusions last hour...',
    'Blocked IP: {ip} due to suspicious activity...',
    'Reboot initiated by user {username}...',
];

const ips = ['192.168.0.105', '10.0.0.3', '172.16.254.1'];
const usernames = ['root', 'admin', 'user1', 'guest'];
const serviceNames = ['sshd', 'httpd', 'mysqld', 'ftpd'];
const interfaceNames = ['eth0', 'eth1', 'wlan0', 'lo'];
const dbNames = ['mysql', 'postgres', 'oracle'];

function generateRandomLog() {
    let template = logTemplates[Math.floor(Math.random() * logTemplates.length)];

    let msg = template
        .replace('{id}', Math.floor(Math.random() * 10000))
        .replace('{ip}', ips[Math.floor(Math.random() * ips.length)])
        .replace('{count}', Math.floor(Math.random() * 1000))
        .replace('{username}', usernames[Math.floor(Math.random() * usernames.length)])
        .replace('{size}', Math.floor(Math.random() * 10000))
        .replace('{percent}', Math.floor(Math.random() * 100))
        .replace('{serviceName}', serviceNames[Math.floor(Math.random() * serviceNames.length)])
        .replace('{interfaceName}', interfaceNames[Math.floor(Math.random() * interfaceNames.length)])
        .replace('{dbName}', dbNames[Math.floor(Math.random() * dbNames.length)]);

    console.log(getCurrentTimestamp() + " " + msg);

    setTimeout(generateRandomLog, Math.random() * (200 - 50) + 10);
}

function getCurrentTimestamp() {
    return new Date().toISOString().replace(/T/, ' ').replace(/\..+/, '');
}

generateRandomLog();