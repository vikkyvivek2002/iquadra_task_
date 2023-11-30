from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


dummy_user = {'name': 'vivek vardhan', 'email': '15847vivek@gmail.com', 'password': 'vikky@v3', 'address': '123 Main St, Rajahmundry', 'dob': '10-24-2002'}

categories = {
    'Friends👨🏻‍🤝‍👩🏼': [{'name': 'Abhi', 'phone': '1234567890', 'dob': '02-15-2003', 'address': '456 Park St, Rajahmundry'},
                {'name': 'sai', 'phone': '9876543210', 'dob': '05-20-2002', 'address': '789 Oak Ave, Kakinada'},{'name': 'siva krishana', 'phone': '1234567558', 'dob': '02-25-2001', 'address': ' 3-147 mainroad, Rajahmundry'},
                {'name': 'sai venkat ', 'phone': '9456693210', 'dob': '12-04-2002', 'address': 'opsit to East83 mall, Kakinada'}],
    'Family👨🏻‍👩🏼‍👧🏻‍👦🏻': [{'name': 'Mom', 'phone': '1112223333', 'dob': '03-10-1988', 'address': '123 Main St, Rajahmundry'},{'name': 'Dad', 'phone': '5552223333', 'dob': '08-22-1985', 'address': '123 Main St, Rajahmundry'},{'name': 'Sister', 'phone': '1118883333', 'dob': '07-19-2000', 'address': '123 Main St, Rajahmundry'},{'name': 'Brother', 'phone': '888545966', 'dob': '03-10-2004', 'address': '123 Main St, Rajahmundry'}],
    'Classmates🫱🏻‍🫲🏽': [{'name': 'Raju', 'phone': '5556667777', 'dob': '08-25-2003', 'address': '555 School St , Rajahmundry'},{'name': 'Ramya', 'phone': '5556665657', 'dob': '10-05-2002', 'address': '3-145, Beside KLM , Rajahmundry'},{'name': 'Meghana', 'phone': '9996667777', 'dob': '05-31-2003', 'address': '5-225 mainroad, Rajahmundry'},{'name': 'Lucy', 'phone': '555233667', 'dob': '05-09-2003', 'address': '123 School St, Kakinada'}],
    'Crush💕': [{'name': 'Puja', 'phone': '5556664567', 'dob': '10-21-2003', 'address': '3-89 Townjunction, Rajahmundry'},{'name': 'harshi', 'phone': '2583691470', 'dob': '10-11-2003', 'address': '3-145 kb park , Rajahmundry'},{'name': 'jothi', 'phone': '9996665567', 'dob': '09-29-2003', 'address': '5-225 mainroad, Kakinada'},{'name': 'Indu', 'phone': '5569321478', 'dob': '05-10-2003', 'address': '123 mainroad, Kakinada'}],
    'work👩‍💻👨‍💻': [{'name': 'Puja', 'phone': '5556664567', 'dob': '10-21-2003', 'address': '3-89 Townjunction, Rajahmundry'},{'name': 'harish', 'phone': '2583691470', 'dob': '10-11-2003', 'address': '3-145 kb park , Rajahmundry'},{'name': 'jon', 'phone': '9996665567', 'dob': '09-29-2003', 'address': '5-225 mainroad, Kakinada'},{'name': 'Usha', 'phone': '5569321478', 'dob': '05-10-2003', 'address': '123 mainroad, Kakinada'}],
    'Relative👩🏻‍👧🏼‍👦🏻': [{'name': 'Uncle', 'phone': '5556664567', 'dob': '10-21-2003', 'address': '3-89 Townjunction, Rajahmundry'},{'name': 'Aunt', 'phone': '2583691470', 'dob': '10-11-2003', 'address': '3-145 kb park , Rajahmundry'},{'name': 'Rajesh', 'phone': '9996665567', 'dob': '09-29-2003', 'address': '5-225 mainroad, Kakinada'},{'name': 'Indu', 'phone': '5569321478', 'dob': '05-10-2003', 'address': '123 mainroad, Kakinada'}]
 
 }

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if email == "15847vivek@gmail.com" and password == "vikky@v3":
        return redirect(url_for('dashboard'))
    else:

        return redirect(url_for('index'))
        

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html', user=dummy_user, categories=list(categories.keys()))

@app.route('/profile')
def profile():
    return render_template('profile.html', user=dummy_user)

@app.route('/category/<category_name>')
def category(category_name):
    contacts = categories.get(category_name, [])
    return render_template('category.html', category_name=category_name, contacts=contacts)

@app.route('/contact/<category_name>/<contact_index>')
def contact(category_name, contact_index):
    contact = categories.get(category_name, [])[int(contact_index)]
    return render_template('contact.html', category_name=category_name, contact=contact)

if __name__ == '__main__':
    app.run(debug=True)
