from flask import Flask, render_template, request, url_for
import time

app = Flask(__name__, static_url_path='/static')

times = []
total_time = 0

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method=="POST":
        if request.form['tap'] == '⍝':
            time1 = time.time() * 1000
            times.append(time1)

    return render_template('index.html')

@app.route('/calculate')
def calculate():
    try:
        bpm = 0
        total_time = 0
        difference = []

        for x, y in zip(times[0::], times[1::]):
            difference.append(y-x)

        total_time = sum(difference)
        average = total_time/len(difference)
        bpm = round(60000/average,1)
        times.clear()

        return render_template('bpm.html', bpm=bpm)

    except(ZeroDivisionError):
        return render_template('notap.html')

if __name__ == '__main__':
    app.run(debug=True)
