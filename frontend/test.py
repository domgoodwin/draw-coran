import uuid
#t=uuid.uuid1()
#print(t)
#print ('the unique filename is ' + str(t))


def createFilename():
	x=uuid.uuid1()
	print ('the unique filename is ' + str(x))
	Fname= str(x)+ '.png'
	return Fname


Filename= createFilename()
print (Filename)