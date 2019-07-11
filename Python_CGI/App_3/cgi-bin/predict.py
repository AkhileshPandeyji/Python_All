import cgi
from sentimentAnalysis import train,test
from storeFile import store_csv,load_csv

forms = cgi.FieldStorage()
msg = forms.getvalue("msg")

cv,reg,stopw,wnet = train()
senti = test(msg,cv,reg,stopw,wnet)

data = [msg,senti]
store_csv(data)
data_list = load_csv()

posCount = 0
negCount = 0

for i in range(len(data_list)):
    if data_list[i][1] == str(1):
        posCount+=1
    else:
        negCount+=1

print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <!--Load the AJAX API-->
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">

      // Load the Visualization API and the corechart package.
      google.charts.load('current', {'packages':['corechart']});

      // Set a callback to run when the Google Visualization API is loaded.
      google.charts.setOnLoadCallback(drawChart);

      // Callback that creates and populates a data table,
      // instantiates the pie chart, passes in the data and
      // draws it.
      function drawChart() {

        // Create the data table.
        var data = new google.visualization.DataTable();
        data.addColumn('string', 'Topping');
        data.addColumn('number', 'Slices');
        data.addRows([
          ['Positive', %s],
          ['Negative', %s],
        ]);

        // Set chart options
        var options = {'title':'Review Analysis',
                       'width':600,
                       'height':400};

        // Instantiate and draw our chart, passing in some options.
        var chart = new google.visualization.PieChart(document.getElementById('chart_div'));
        chart.draw(data, options);
      }
    </script>
</head>
<body>
<h1>Review Analysis:</h1>
<hr>
<h2>Red : Negative</h2>
<h2>Green : Positive</h2>
<hr>
<ul>
""" % (posCount,negCount))
for i in range(len(data_list)):
    if data_list[i][1] == str(0):
        color = "red"
    else:
        color = "green"

    print(""" 
    <li style="color:{};">{}
    </li>
    """.format(color,data_list[i][0]))

print("""
</ul>
<div  style="text-align:center;">
<!--Div that will hold the pie chart-->
<div id="chart_div"></div>
<div>
</body>
</html>
""")