from flask import Flask



def create_app():
    app=Flask(__name__)

    from .api import bp_api
    from .hiscores import hiscores_bp

    app.register_blueprint(bp_api, url_prefix="/api")
    app.register_blueprint(hiscores_bp)

    return app