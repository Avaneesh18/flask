from flask import Flask, jsonify , request 
app = Flask(__name__)
task = [
    {
        'id': 1 ,
        'title': u'buy grocery',
        'description': u'Milk , Cheese, Butter',
        'done': False
    },
    {
        'id' : 2,
        'title': u'learn python',
        'description': u'need to find a good python tutorial',
        'done': False 
    }
]
@app.route("/add-data",methods = ["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status": "error",
            "message": "pls provide the data"         
        },400)

    task = {
        'id': tasks[-1]['id']+1,
        'title': request.json['title'],
        'description': request.json.get('desccription',""),
        'done': False
    }
    tasks.append(task)
    return jsonify({
        "status": "success",
        "message": "task added successfuly"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data": "tasks"
    })

if (__name__ == "__main__"):
    app.run(debug=True)