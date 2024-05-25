from flask import Flask, jsonify
from api.ibge import IBGE

app = Flask(__name__)

@app.route('/SelfResearchAPI/ibge/pesquisa', methods=['GET'])
def get_ibge_data():
    ibge = IBGE()
    try:
        data = ibge.get_pesquisas()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)