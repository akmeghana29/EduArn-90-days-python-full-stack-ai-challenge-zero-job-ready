from flask import Flask
from config import Config
from extensions import db
from routes.cover_letter import cover_letter_bp

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(cover_letter_bp)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
