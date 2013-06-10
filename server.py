#!/usr/bin/python 

from flask import Flask, jsonify, render_template, request
import random

app = Flask(__name__)

@app.route('/_add_numbers')
def add_numbers():
    print "_add_numbers"
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)



@app.route('/')
def index():
    print "index route"
    data=[{"message": "Tokyo"}, {"message": "AC"}]
    return render_template('index.html', navigation=data)  


@app.route('/template_test')
def template_test():
    print "template_test"
    #data=[{"data": [49.9, 54.4], "message": "Tokyo"}, {"data": [42, 30.4], "message": "AC"}]
    #return render_template('index.html', navigation=data) 

    print random.randint(1, 100)

    rand_list= [{"name":"abc", "count":99}, {"name":"xyz", "count":5}, {"name":"fred", "count":123}, {"name":"foo", "count":69}, {"name":"bar", "count":101}, {"name":"thing", "count":random.randint(1,100)}]
    
    result = render_template('layout.html', a_random_string="Heey, what's up!", a_random_list=rand_list)

    print result
    return result




if __name__ == "__main__":
    app.run(port=7000)