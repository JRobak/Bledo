import os
from flask_sqlalchemy import SQLAlchemy
from app import create_app

app = create_app()

db_path = os.path.join(os.environ['BLEDO_DATABASE_PATH'], 'bledo_databases.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


if __name__ == '__main__':
    app.run(debug=True)