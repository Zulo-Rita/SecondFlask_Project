from app import app, db, Darbuotojas, Uzduotis

with app.app_context():
    db.create_all()

    # Darbuotojai
    darbuotojas1 = Darbuotojas('Petras', 'Petraitis', 'Dev')
    darbuotojas2 = Darbuotojas('RiRi', 'Riraite', 'programuotojas')
    darbuotojas3 = Darbuotojas('RoRo', 'RoRo', 'junior')


    # užduotys – skirtingi kiekvienam darbuotojui

    uzduotis1 = Uzduotis('Aplikacijos architektūra', 'Sukurti bendrą sisteminę struktūrą', '3mėn', 'Pradžia')
    uzduotis1.darbuotojas = darbuotojas1
    uzduotis2 = Uzduotis('Architektūros įgyvendinimas', 'Įdiegti architektūros sprendinius', '14mėn', 'Vystymas')
    uzduotis2.darbuotojas = darbuotojas1

    uzduotis3 = Uzduotis('Duomenų bazės projektavimas', 'Sukurti lenteles ir ryšius tarp jų', '4mėn', 'Analizė')
    uzduotis3.darbuotojas = darbuotojas2
    uzduotis4 = Uzduotis('REST API kūrimas', 'Sukurti API prieigą sistemai', '6mėn', 'Kūrimas')
    uzduotis4.darbuotojas = darbuotojas2

    uzduotis5 = Uzduotis('UI testavimas', 'Testuoti vartotojo sąsają', '2mėn', 'Testavimas')
    uzduotis5.darbuotojas = darbuotojas3
    uzduotis6 = Uzduotis('Kodo dokumentavimas', 'Parengti kodo dokumentaciją', '1mėn', 'Pabaiga')
    uzduotis6.darbuotojas = darbuotojas3

    # Įrašymas į DB
    db.session.add_all([
        darbuotojas1, darbuotojas2, darbuotojas3
        ])

    db.session.commit()
