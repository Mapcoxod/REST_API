from flask import Flask, jsonify, request
from datetime import date, timedelta

app = Flask(__name__)
# client = app.test_client()

my_list = [
    {
        'iin': ''
    }
]

err = [
    {
        'message': 'iin alredy in list'
    }
]


'''функция высчитывает возраст и возвращает его'''
def old_year(iin):
    global my_list
    year = None
    if int(iin[6:7]) == 1 or int(iin[6:7]) == 2:
        year = '18'
    elif int(iin[6:7]) == 3 or int(iin[6:7]) == 4:
        year = '19'
    elif int(iin[6:7]) == 5 or int(iin[6:7]) == 6:
        year = '20'
    birth_date = date(int(year + iin[:2]), int(iin[2:4]), int(iin[4:6]))
    age = (date.today() - birth_date) // timedelta(days=365.2425)
    my_list = [
        {
            'iin': iin,
            'age': age
        }
    ]
    return my_list


@app.route('/people/<string:iin>', methods=['GET'])
def get_list(iin):
    return jsonify(old_year(iin))


@app.route('/people', methods=['POST'])
def update_list():
    global my_list
    data = request.json
    my_list.append(data)
    return jsonify(old_year(data['iin']))


if __name__ == "__main__":
    app.run()
