from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Architect',
        'location': 'Vilnius, Lithuania',
        'salary': '6k$'
    },
    {
        'id': 2,
        'title': 'Tester',
        'location': 'Kaunas, Lithuania',
        'salary': '4k$'
    },
    {
        'id': 3,
        'title': 'Programmer',
        'location': 'Kaunas, Lithuania',
    },
    {
        'id': 4,
        'title': 'Manager',
        'location': 'Klaipeda, Lithuania',
        'salary': '4.5k$'
    }


]

@app.route("/")
def hello_world():
    return render_template("home.html",
                           jobs=JOBS,
                           company_name='Laurynas')
@app.route("/api/jobs")
def list_jobs():
    return jsonify(JOBS)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
