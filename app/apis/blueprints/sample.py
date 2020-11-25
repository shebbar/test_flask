from flask import Blueprint, request, jsonify, g, render_template

bp = Blueprint("sample", __name__, url_prefix="/api/sample/v1")

@bp.route("/test", methods=["GET"])
def sample_test():
    try:
        return render_template('run.html')
    except Exception as e:
        print("error is ", str(e))

@bp.route("/run", methods=["POST"])
def sample_run():
    try:
        print("inside")
        print("request = ", request)
        topology = request.form['topology']
        testSuite = request.form['suite']
        resultSet = {}
        resultSet['topology'] = topology
        resultSet['testSuite'] = testSuite
        return render_template('sample.html', resultSet=resultSet)
    except Exception as e:
        print("error is ", str(e))
