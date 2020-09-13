
import cv2
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def home():
    
    print("fc sh: oblong")
    return render_template("index.html")



@app.route("/oblong")
def oblong():

    img=cv2.imread("C:\Users\Maggie\Documents\Python\img.jpg")
    cv2.imwrite("C:\Users\Maggie\Documents\Python\pic.jpg",img)
    return render_template("oblong.html")


    
if __name__ == "__main__":
    app.run(debug=True)
  #We made two new changes



    
