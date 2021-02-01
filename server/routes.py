from flask import render_template, redirect
from server import app, db
from server.forms import DataForm
from server.models import Data, Count

@app.route('/')
def index():
    number = Count.query.get('count')
    if (number):
        count=number.count
    else:
        count=0
    return render_template('index.html', count=count)


@app.route('/test')
def test():
    data = Data.query.all()
    return render_template('test.html', data=data)


@app.route('/add_data', methods=['GET', 'POST'])
def add_data():
    form = DataForm()
    if form.validate_on_submit():
        print(form.text.data)
        data = Data(text=form.text.data)
        db.session.add(data)
        db.session.commit()
        return redirect('/test')
    return render_template('add_data.html', form=form)
