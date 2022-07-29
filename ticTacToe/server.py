from src import api
from src.utils import config

api.run(
    host="0.0.0.0",
    port=config.PORT,
    debug=False,
)