from flask import Flask, render_template, jsonify





app = Flask(__name__)

JOBS=[
    {
    'id':1,
    'title':'Data Analyst',
    'loaction':'Bangulore, India',
    'salary':'Rs. 10,00,00'
    },
    {
    'id':2,
    'title':'Data Scientist',
    'loaction':'Bangulore, India',
    'salary':'Rs. 15,00,00'
    },
    {
    'id':3,
    'title':'Frontend Engineer',
    'loaction':'Remote',
    'salary':'Rs. 12,00,00'
    },
    {
    'id':4,
    'title':'Backend Enginner',
    'loaction':'Bangulore, India',
    'salary':'Rs. 20,00,00'
    }

]





@app.route("/")
def hello_jovian():
    return render_template('home.html', 
                           jobs=JOBS, 
                           company_name='Jovian')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__=="__main__":
    app.run(debug=True)
