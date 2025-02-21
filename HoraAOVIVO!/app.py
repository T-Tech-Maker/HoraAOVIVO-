from flask import Flask, render_template
import datetime
from flask import Response

app = Flask(__name__)

@app.route('/')
def home():
    # Obtém a hora atual
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', time=current_time)

@app.route('/clock')
def clock():
    # Endpoint para fornecer o horário em tempo real
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    return Response(current_time, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=True)
