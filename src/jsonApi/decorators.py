from flask_cors import cross_origin

authDecorator = (
    cross_origin(headers=["Content-Type", "Authorization"]),
    cross_origin(headers=["Access-Control-Allow-Origin", "*"]),
)
