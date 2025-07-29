from flask import Flask, request, jsonify
from portscanner import scan_host_ports

app = Flask(__name__)

@app.route('/scan', methods=['POST'])
def scan_ports():
    data = request.get_json()
    host = data.get('host')
    ports = data.get('ports')
    if not host or not ports:
        return jsonify({'error': 'Missing host or ports'}), 400
    result = scan_host_ports(host, ports)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
