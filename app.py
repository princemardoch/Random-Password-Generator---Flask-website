from flask import *
from passgen import passgen

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    a = None
    b = None
    c = None
    d = None
    e = 15
    aa = 'checked'
    bb = 'checked'
    cc = 'checked'
    dd = 'checked'

    passwordgen = "Mot de passe s'affichera ici"

    if request.method == 'POST':
        a = request.form.get('az1')
        b = request.form.get('az2') 
        c = request.form.get('dgt')
        d = request.form.get('spc')
        e = int(request.form.get('longeur'))
        if e > 35:
            e = 34

        print(a,b,c,d,e)

        aa = 'checked' if a == 'True' else ''
        bb = 'checked' if b == 'True' else ''
        cc = 'checked' if c == 'True' else ''
        dd = 'checked' if d == 'True' else ''

        passwordgen = passgen(a,b,c,d,e)

    return render_template('index.html', password=passwordgen, longeur=e, aa=aa,bb=bb,cc=cc,dd=dd)

if __name__ == '__main__':
    app.run(debug=True, port=0)