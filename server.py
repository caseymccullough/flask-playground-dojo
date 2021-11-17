from flask import Flask, render_template
app = Flask(__name__)

@app.route('/play')
def default():
   return render_template('index.html', num=3, color="skyblue")

@app.route('/play/<int:num>')
def numOnly(num):
   return render_template('index.html', num= int(num), color='skyblue')

@app.route('/play/<num>/<color>')
def colorAndNum(num, color):
   return render_template('index.html', num= int(num), color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.