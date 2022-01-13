from flask import Flask, render_template, redirect
from form import MessageForm
from config import Config
from Todo import my_function 
app = Flask(
  'app',
  template_folder='templates'
)
app.config.from_object(Config)

my_message = []
def setMessage(my_To_Do_List):
  global my_message
  my_message.append(my_To_Do_List)
  print(my_message)

def my_function():
  print("my_To_Do_")
  my_To_Do_List=["clean my room, do my homework, wash my clothing, go to the mall"]

@app.route('/', methods=['GET', 'POST'])
def page_one():
  print('my_To_Do_List')
  form = MessageForm()
  print("my_To_Do_List")
  if form.is_submitted():
    print("made it")
    setMessage(form.message.data)
    return redirect('/display')
  return render_template('pageOne.html', form=form)

@app.route('/display')
def page_two():
  return render_template('pageTwo.html', my_message=my_message)

app.run(host='0.0.0.0', port=8080)
