from flask import Flask, jsonify

app = Flask(__name__, template_folder='templates', static_folder='static')
