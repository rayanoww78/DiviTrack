from flask import Flask, render_template, jsonify
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dividends')
def get_dividends():
    # Exemple statique, à remplacer par appel réel à Budget Insight
    data = [
        {"date": "2025-03-12", "company": "TotalEnergies", "amount": 28.40},
        {"date": "2025-03-04", "company": "Air Liquide", "amount": 15.20},
        {"date": "2025-02-20", "company": "Vinci", "amount": 12.80},
    ]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
