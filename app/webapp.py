import os
import logging
import flask
from robostat.web.app import create_app

app = create_app(
        import_name=__name__,
        config_pyfile=os.environ["ROBOSTAT_CONFIG"]
)

app.register_blueprint(flask.Blueprint("public", __name__,
    static_folder="../public",
    static_url_path=""
))

if app.debug:
    logging.basicConfig(format="%(asctime)s %(levelname)s %(name)s %(message)s", level=logging.DEBUG)
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

    # Tää siks että rssserv yms pyörii eri portissa localhostissa
    @app.after_request
    def disable_cors(response):
        response.headers["Access-Control-Allow-Origin"] = "*"
        return response

    @app.route("/")
    def index():
        return flask.send_file("../public/index.html")
