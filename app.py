from flask import Flask, render_template, request, redirect, url_for
from config import Config
from models import db, Darbuotojas, Uzduotis

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()


@app.route('/', methods=['GET', 'POST'])
def home():
    search_text = request.args.get('paieskoslaukelis')
    if search_text:
        darbuotojai = Darbuotojas.query.filter(Darbuotojas.vardas.ilike(search_text + "%"))
    else:
        darbuotojai = Darbuotojas.query
    search_text = request.args.get('paieskoslaukelis')
    if search_text:
        darbuotojai = Darbuotojas.query.filter(Darbuotojas.vardas.ilike(search_text + "%"))
    if request.method == 'POST':
        vardas = request.form.get('vardolaukelis')
        pavarde = request.form.get('pavardeslaukelis')
        gim_metai = request.form.get('gimimolaukelis')
        pareigos = request.form.get('pareigulaukelis')
        skyrius = request.form.get('skyriauslaukelis')
        if vardas and pavarde:
            new_worker = Darbuotojas(vardas, pavarde, pareigos)
            db.session.add(new_worker)
            db.session.commit()
    return render_template('index.html', darbuotojai=darbuotojai)


@app.route('/darbuotojas/<int:darbuotojas_id>', methods=['GET', 'POST'])
def one_employe(darbuotojas_id):
    darbuotojas = Darbuotojas.query.get(darbuotojas_id)
    if not darbuotojas:
        return "Darbuotojas nerastas"

    if request.method == 'POST':
        pavadinimas = request.form.get('pavadinimolaukelis')
        aprasymas = request.form.get('aprasymolaukelis')
        laikas = request.form.get('laikolaukelis')
        statusas = request.form.get('statusolaukelis')
        if aprasymas and pavadinimas:
            nauja_uzduotis = Uzduotis(pavadinimas, aprasymas, laikas, statusas)
            nauja_uzduotis.darbuotojas_id = darbuotojas.id
            db.session.add(nauja_uzduotis)
            db.session.commit()
            return redirect(url_for('one_employe', darbuotojas_id=darbuotojas.id))

    return render_template('vienas_darbuotojas.html', darbuotojas=darbuotojas, )


@app.route('/darbuotojai/delete/<int:darbuotojas_id>', methods=['POST'])
def delete(darbuotojas_id):
    one_worker = Darbuotojas.query.get(darbuotojas_id)
    if one_worker:
        db.session.delete(one_worker)
        db.session.commit()
    return redirect(url_for('home'))


@app.route('/uzduotys/redaguoti/<int:uzduotis_id>', methods=['GET', 'POST'])
def edit_task(uzduotis_id):
    one_task = Uzduotis.query.get(uzduotis_id)
    if not one_task:
        return 'Užduotis negzistuoja'
    if request.method == 'GET':
        return render_template('uzduotis_update.html', uzduotis=one_task)
    elif request.method == 'POST':
        pavadinimas = request.form.get('pavadinimolaukelis')
        aprasymas = request.form.get('aprasymolaukelis')
        laikas = request.form.get('laikolaukelis')
        statusas = request.form.get('statusolaukelis')
        if aprasymas and pavadinimas:
            one_task.pavadinimas = pavadinimas
            one_task.aprasymas = aprasymas
            one_task.skirtas_laikas = laikas
            one_task.statusas = statusas
            db.session.commit()

    return redirect(url_for('home'))


@app.route('/darbuotojas/edit/<int:darbuotojas_id>', methods=['GET', 'POST'])
def edit_darbuotojas(darbuotojas_id):
    one_worker = Darbuotojas.query.get(darbuotojas_id)
    if not one_worker:
        return 'Darbuotojas negzistuoja'
    if request.method == 'GET':
        return render_template('darbuotojas_update.html', darbuotojas=one_worker)
    elif request.method == 'POST':
        vardas = request.form.get('vardolaukelis')
        pavarde = request.form.get('pavardeslaukelis')
        gim_metai = request.form.get('gimimolaukelis')
        pareigos = request.form.get('pareigulaukelis')
        skyrius = request.form.get('skyriauslaukelis')

        if vardas and pavarde:
            one_worker.vardas = vardas
            one_worker.pavarde = pavarde
            one_worker.gimimo_data = gim_metai
            one_worker.pareigos = pareigos
            one_worker.skyrius_pavadinimas = skyrius
            db.session.commit()

    return redirect(url_for('home'))


if __name__ == '__main__':
    # app.run()
    app.run(host="0.0.0.0", port=80, debug=True) # cloude

