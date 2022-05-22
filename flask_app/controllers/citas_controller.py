from flask  import render_template, redirect, session, request, flash
from flask_app import app

#modelo de recipe
from flask_app.models.user import User
from flask_app.models.cita import Cita


@app.route('/appointments/new')
def nueva_cita():
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        "id": session['user_id']
    }

    user = User.get_by_id(data)
    return render_template('add_appointment.html', user=user)

@app.route('/create/appointment', methods=['POST'])
def create_appointment():
    if 'user_id' not in session:
        return redirect('/')

    if not Cita.valida_cita(request.form):
        return redirect('/appointments/new')

    Cita.save(request.form)
    return redirect('/appointments')

@app.route('/appointments/edit/<int:id>')
def edit_appointment(id):
    if 'user_id' not in session:
        return redirect('/')
    
    data = {
        "id": session['user_id']
    }

    user = User.get_by_id(data)

    #necesitamos los datos de la receta
    data_cita = {
        "id":id
    }
    cita = Cita.get_by_id(data_cita)
    return render_template('edit.html', user=user, cita=cita)

@app.route('/update/cita', methods=['POST'])
def update_appointment():
    if 'user_id' not in session:
        return redirect('/')

    if not Cita.valida_cita(request.form):
        return redirect('/appointments/edit/'+request.form['id'])
    
    Cita.update(request.form)

    return redirect('/appointments')

@app.route('/appointments/delete/<int:id>')
def delete_appointment(id):
    if 'user_id' not in session:
        return redirect ('/')
    
    data = {
        "id" : id
    }

    Cita.delete(data)
    return redirect('/appointments')






