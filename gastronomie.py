from flask import Flask
from curs_scc_444D_gastronomie.app.routes.bouyourdi import bouyourdi_bp

app = Flask(__name__)
app.register_blueprint(bouyourdi_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)