import cgi
from sklearn.preprocessing import StandardScaler
import numpy as np

forms = cgi.FieldStorage()
bedrooms = forms.getvalue("bedrooms")
bathrooms = forms.getvalue("bathrooms")
area = forms.getvalue("area")
waterfront = forms.getvalue("waterfront")
predict = None

B = np.asarray([ 0.0, -0.11423837,  0.07026181,  0.67984695,  0.19174395]).reshape(-1,1)
X = np.asarray([1,bedrooms,bathrooms,area,waterfront]).reshape(-1,1)
sc = StandardScaler()
X = sc.fit_transform(X)
X = X.T
ypred = X.dot(B)
predict = sc.inverse_transform(ypred)
predict = predict[0][0]
waterf = None
if waterfront == str(0):
        waterf = "No"
elif waterfront == str(1):
        waterf = "Yes"


print('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
<div>
    <H1>Values of Data:</h1>
    <h2>Bedrooms:{}</h2>
    <h2>Bathrooms:{}</h2>
    <h2>Sq Feet Area:{}</h2>
    <h2>Waterfront:{}</h2>
</div>
<div>
    <h1>Value of Prediction:</h1>
    <h2>Price:{}</h2>
</div>
</body>
</html>
'''.format(bedrooms,bathrooms,area,waterf,predict))