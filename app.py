from flask import Flask
from db import engine, Base
from routes.student_routes import router as student_router
from routes.chat_routes import router as chat_router

app = Flask(__name__)
Base.metadata.create_all(bind=engine)

app.register_blueprint(student_router)
app.register_blueprint(chat_router)

if __name__ == "__main__":
    app.run(debug=True)
