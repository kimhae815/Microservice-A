from flask import Flask, request, json
import requests

app = Flask(__name__)

# @app.route('/', methods = ['get', 'post'])
# def home():
#     data = [100, {"A": 40, "B": 25, "C": 5}]
#     response = requests.post('http://127.0.0.1:5000/statistics', json=data)
#     response.json()
#     print(response.json())
#     return Hello

@app.route('/statistics', methods = ['get', 'post'])
def next():
    data = request.json
    print(data)
    dataArray = [200, {"A": 40, "B": 25, "C": 35}]

    # number of students for each grade
    gradeA = dataArray[1]['A']*dataArray[0]//100
    gradeB = dataArray[1]['B']*dataArray[0]//100
    gradeC = dataArray[1]['C']*dataArray[0]//100

    # display statistics
    print("A: ", gradeA)
    print("B: ", gradeB)
    print("C: ", gradeC)
    result = {'A': 0, 'B': 0, 'C': 0}
    result['A'] = gradeA
    result['B'] = gradeB
    result['C'] = gradeC
    return result



if __name__ == '__main__':
    app.run(debug=True)

