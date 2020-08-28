from flask import Flask, render_template, request, redirect, url_for
from tool4text import _transliterate_

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/translit_tool')
def translit_tool():
    return render_template('translit_tool.html')

@app.route('/trans', methods = ['POST'])
def trans():
    in_text = request.form['input_text']
    lang_ = request.form.getlist("outlang")
    out_text = _transliterate_(_text_, lang_[0])
    return render_template('translit_tool.html', out_text = out_text, in_text = in_text) 
    
if __name__ == '__main__':
    app.run()