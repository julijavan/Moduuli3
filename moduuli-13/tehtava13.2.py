import mysql.connector

from flask import Flask

app = Flask(__name__)


@app.route('/airport/<code>')
def airport_name(code):
    yhteys = mysql.connector.connect(
        database='flight_game',
        user='eliell2',
        password='gr0ups',
        autocommit=True)

    sql = f"select ident, name, municipality from airport where ident = %s"
    kursori = yhteys.cursor()
    kursori.execute(sql,(code,))
    tulos = kursori.fetchone()
    if tulos:
        answer = {
            'ICAO': tulos[0],
            'Name': tulos[1],
            'Location': tulos[2]
        }
        return answer

if __name__ == '__main__': app.run(use_reloader=True, host='127.0.0.1', port=3000)