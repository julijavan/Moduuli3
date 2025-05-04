from flask import Flask, request

app = Flask(__name__)

@app.route('/alkuluku/<int:num>')
def tarkista_alkuluku(num):
    num = int(num)
    is_prime = True
    for n in range(2, num):
        if num % n == 0:
            is_prime = False
            break
        else:
            is_prime = True

    vastaus = {
        "Number": num,
        "isPrime": is_prime
    }
    return request(vastaus)

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=3000)
