from flask import Flask, render_template, jsonify
import divi_maker
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dividends')
def get_dividends():
    # Exemple statique, à remplacer par appel réel à Budget Insight
    data = [
        {"date": "2025-03-12", "company": "TotalEnergies", "amount prediction for 2025": divi_maker.get_divi("TTE")},
        {"date": "2025-03-04", "company": "Apple", "amount": divi_maker.get_divi("AAPL")},
        {"date": "2025-02-20", "company": "Vinci", "amount": divi_maker.get_divi("AMZN")},
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
