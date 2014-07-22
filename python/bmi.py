"""===========================================================================
	BMI is a useful measurement of one's weight relative to their height.  It 
	has huge problems.  Criticisms include that it does not account for 
	gender differences as well as differences of frame/build.  Nonetheless, it 
	remains a decent tool for figuring how appropriate your weight is for you.  

	This is my first iteration of what I hope will become a web app.  
==========================================================================="""

def bmi(height,weight):
	bmi = ((float(weight) / (height * height))*703)
	if bmi < 18.5:
		return str(bmi)+" : "+"underweight"
	elif bmi >= 18.5 and bmi < 25.0:
		return str(bmi)+" : "+"normal weight"
	elif bmi >= 25.0 and bmi < 30:
		return str(bmi)+" : "+"overweight"
	elif bmi >= 30.0 and bmi < 35.0:
		return str(bmi)+" : "+"obesity I"
	elif bmi >= 35.0 and bmi < 40:
		return str(bmi)+" : "+"obesity II"
	else:
		return str(bmi)+" : "+"extreme obesity"

#print bmi(76,195)
#print bmi(66,195)
#print bmi(80,140)
