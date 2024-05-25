from flask import Flask, jsonify


def registerErrorHandler(app: Flask):

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify(error="Bad Request"), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify(error="Unauthorized"), 401

    @app.errorhandler(403)
    def forbidden(error):
        return jsonify(error="Forbidden"), 403

    @app.errorhandler(404)
    def not_found(error):
        return jsonify(error="Not Found"), 404

    @app.errorhandler(405)
    def method_not_allowed(error):
        return jsonify(error="Method Not Allowed"), 405

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify(error="Internal Server Error"), 500

    @app.errorhandler(502)
    def bad_gateway(error):
        return jsonify(error="Bad Gateway"), 502

    @app.errorhandler(503)
    def service_unavailable(error):
        return jsonify(error="Service Unavailable"), 503

    @app.errorhandler(504)
    def gateway_timeout(error):
        return jsonify(error="Gateway Timeout"), 504
    
