from flask import Flask, render_template, request, redirect
from database import add_reservation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        contact = request.form['contact']
        time_slot = request.form['time_slot']
        guests = request.form['guests']

        if all([name, contact, time_slot, guests]):
            if add_reservation(name, contact, time_slot, int(guests)):
                return "Reservation added successfully!"
            else:
                return "Failed to add reservation."
        else:
            return "Please fill all fields."

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
