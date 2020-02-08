
from flask_restful import reqparse

library_parser = reqparse.RequestParser()
library_parser.add_argument("name", required=True, help="Important: {error_msg}!!!")
