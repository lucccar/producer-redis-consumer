from flask import Flask, request, jsonify, abort
from flask_cors import CORS
from rq import Queue

from producer.constants import conn
from producer.base.write import write_txt


app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

q = Queue(connection=conn)


@app.route("/process", methods = ["POST"])
def process():
    try:
        json = request.json

        if json == None:
            return "Invalid Input", 400

        job = q.enqueue_call(
            func=write_txt, args=(json,), result_ttl=5000
        )

        return jsonify(job.get_id()), 200
    
    except:
        abort(500, "Some unknown error occurred'")

    

if __name__ == "__main__":

    app.run(host="0.0.0.0", port="5000")