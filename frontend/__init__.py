from flask import Flask, render_template, request
import uuid

import boto3

app = Flask(__name__)

def createFilename():
	x=uuid.uuid1()
	print ('the unique filename is ' + str(x))
	Fname= str(x)+ '.png'
	return Fname


Filename= createFilename()
#print (Filename)

@app.route('/')
def index():
	return render_template("index.html")
    
@app.route('/upload', methods=['POST'])


def upload():
    s3 = boto3.resource('s3')
#bucket name can be changed to whatever 

    s3.Bucket('awsbucketkiran').put_object(Key=Filename, Body=request.files['myfile'])

    return render_template("uploaded.html")

if __name__ == '__main__':
    app.run(debug=True)


