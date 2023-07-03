from flask import Flask, request, jsonify
import uuid
from bson import ObjectId
import random
import string

app = Flask(__name__)

@app.route('/generate_id', methods=['GET'])
def generate_id():
    id_type = request.args.get('type')  
    count = int(request.args.get('count', 1))  # Get the count of IDs to generate (default: 1)

    if id_type == 'uuid':
        ids = [str(uuid.uuid4()) for _ in range(count)]
    elif id_type == 'objectid':
        ids = [str(ObjectId()) for _ in range(count)]
    elif id_type == 'numeric':
        ids = [str(i) for i in range(count)]
    elif id_type == 'random_string':
        ids = [''.join(random.choices(string.ascii_letters + string.digits, k=10)) for _ in range(count)]
    elif id_type == 'web_key':
        ids = [''.join(random.choices(string.ascii_letters + string.digits + "-_", k=32)) for _ in range(count)]
    else:
        return jsonify({'error': 'Invalid ID type'})

    return jsonify({'ids': ids})

if __name__ == '__main__':
    app.run(debug=True)
