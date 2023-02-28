from models import engine, Asmuo, Bankas, Saskaita
from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()


def is_valid_input(input_str):
    try:
        input_num = int(input_str)
        if input_num <= 0:
            return False
        else:
            return True
    except ValueError:
        return False


while True:
    pasirinkimas = int(
        input(
            "1 - įveskite vartotoją\n2 - įveskite banką\n3 - įveskite sąskaitą\n4 - įveskite pajamas/išlaidas\n6 - peržiūrėti vartotojus\n7 - peržiūrėti bankus\n8 - peržiūrėti sąskaitas\n9 - išeiti iš programos"
        )
    )
    # ---------------------------------------------------------------------------------------
    if pasirinkimas == 1:
        # susirenki data
        vardas = input("Įveskite vardą ")
        pavarde = input("Įveskite pavardę ")
        asmens_kodas = int(input("Įveskite asmens kodą "))
        el_pastas = input("Įveskite el. pašto adresą ")
        # assignini inputted data to a Asmou class from models.py
        asmuo = Asmuo(
            vardas=vardas,
            pavarde=pavarde,
            asmens_kodas=asmens_kodas,
            el_pastas=el_pastas,
        )
        # pridedi i sesija
        session.add(asmuo)
        # pushini i db
        session.commit()
    # ---------------------------------------------------------------------------------------
    if pasirinkimas == 2:
        pavadinimas = input("Įveskite banko pavadinimą ")
        adresas = input("Įveskite adresą ")
        banko_kodas = input("Įveskite banko kodą ")
        swift_kodas = input("Įveskite SWIFT kodą ")
        bankas = Bankas(
            pavadinimas=pavadinimas,
            adresas=adresas,
            banko_kodas=banko_kodas,
            swift_kodas=swift_kodas,
        )
        session.add(bankas)
        session.commit()
    # ---------------------------------------------------------------------------------------
    if pasirinkimas == 3:
        numeris = input("Įveskite sąskaitos numerį ")
        balansas = 0
        vartotojai = session.query(Asmuo).all()
        for vartotojas in vartotojai:
            print(vartotojas)
        vartotojo_id = int(input("Pasirinkite vartotojo ID "))
        bankai = session.query(Bankas).all()
        for vienas in bankai:
            print(vienas)
        banko_id = int(input("Pasirinkite banko ID "))
        saskaita = Saskaita(
            numeris=numeris,
            balansas=balansas,
            asmuo_id=vartotojo_id,
            bankas_id=banko_id,
        )
        session.add(saskaita)
        session.commit()
    # ---------------------------------------------------------------------------------------
    if pasirinkimas == 4:
        saskaitos = session.query(Saskaita).all()
        for viena in saskaitos:
            print(viena)
        saskaitos_id = int(input("Pasirinkite sąskaitos ID "))
        pasirinkta_saskaita = session.query(Saskaita).get(saskaitos_id)
        irasas = float(input("Įveskite pajamas/išlaidas (su -) "))
        pasirinkta_saskaita.balansas += irasas
        session.commit()
    # ---------------------------------------------------------------------------------------
    if pasirinkimas == 6:
        vartotojai = session.query(Asmuo).all()
        for vartotojas in vartotojai:
            print(vartotojas)
    # ---------------------------------------------------------------------------------------
    if pasirinkimas == 7:
        bankai = session.query(Bankas).all()
        for vienas in bankai:
            print(vienas)
    # ---------------------------------------------------------------------------------------
    if pasirinkimas == 8:
        saskaitos = session.query(Saskaita).all()
        for viena in saskaitos:
            print(viena)
    # ---------------------------------------------------------------------------------------
    if pasirinkimas == 9:
        print("Programa baigta ")
        break
