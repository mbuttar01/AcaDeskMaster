from flask import Flask, render_template
from datetime import datetime
from collections import deque
from client import recv

app = Flask(__name__)

classhwtest = [['History', '8:30 - 9:20', '11/22/19', '11/14/19, 11/20/19'],
               ['Math', '9:30 - 10:20', '11/22/19', ' '],
               ['PE', '10:30 - 11:20', ' ', ' '],
               ['Lunch', '11:30 - 12:30', ' ', ' ']]
classtime = ['Math', '9:30AM', '9:35AM']

bathroom = deque(['Johnny', 'Adam', 'Sebastian'])
data = None




@app.route('/')
def preswipe():
    global data
    data = recv('1008')
    print(data)
    return render_template('main.html', school="Manhattan College")


@app.route('/swiped')
def swiped1():
    return render_template('swiped1.html', name=eval(data), sched=classhwtest)


@app.route('/swiped2')
def swiped2():
    classtime.append(datetime.strptime(classtime[1], '%I:%M%p'))
    classtime.append(datetime.strptime(classtime[2], '%I:%M%p'))
    print(classtime[3])
    print(classtime[4])
    return render_template('swiped2.html', name=eval(data), classtime=classtime)


@app.route('/test')
def test():
    return render_template('react.html')
