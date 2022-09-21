from flask import Flask, jsonify
from flask_cors import CORS
from flask_talisman import Talisman
from post_factory import PostFactory

app = Flask(__name__)

csp = {
    'default-src': '\'self\''
}
# talisman = Talisman(app, content_security_policy=csp)

# Enable Cross Origin Resource Sourcing (CORS) policies
CORS(app, resources={"/*": {"origins": "http://localhost:3000"}})


@app.route("/")
def index():
    """Root URL response"""
    app.logger.info("Request for Root URL")
    return (jsonify(name="Data Retrieval Service", version="1.0"), 200)


@app.route("/posts", methods=["GET"])
def get_data():
    """Returns forum post data"""
    data = PostFactory.generate(5)
    return jsonify(data)
