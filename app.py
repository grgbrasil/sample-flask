from flask import Flask
from flask import render_template
import tabula

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route('/pdftocsv', methods=['POST', 'GET'])
def pdftocsv(request):
    if request.method == 'POST':
        f = request.files['file']
        arquivo = tabula.read_pdf(f,pages='all')
        tabula.convert_into(f, 'seuarquivo.csv', output_format='csv', pages='all')
        f.save(secure_filename(f.filename))
        return 'file uploaded successfully'
