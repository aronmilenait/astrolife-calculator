from flask import Flask, render_template, request

app = Flask(__name__)

def drake_equation(R_star, f_p, n_e, f_l, f_i, f_c, L):
    return R_star * f_p * n_e * f_l * f_i * f_c * L

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/drake-equation', methods=['GET', 'POST'])
def drake_equation_route():
    error = None
    N = None
    if request.method == 'POST':
        try:
            R_star = float(request.form['R_star'])
            f_p = float(request.form['f_p'])
            n_e = float(request.form['n_e'])
            f_l = float(request.form['f_l'])
            f_i = float(request.form['f_i'])
            f_c = float(request.form['f_c'])
            L = float(request.form['L'])
            N = drake_equation(R_star, f_p, n_e, f_l, f_i, f_c, L)
        except ValueError:
            error = "Please enter valid numbers for all fields."
    return render_template('drake.html', N=N, error=error)

if __name__ == '__main__':
    app.run(debug=True)
