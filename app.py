from flask import Flask, render_template

app = Flask(
    __name__,
    static_folder='projeto-bella-store/static',
    template_folder='projeto-bella-store'
)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
