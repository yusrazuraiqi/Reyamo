import csv
from os import write
output = open(r"index.html", 'w')
output.write("""
<!DOCTYPE html>
<html lang="en">
<head>
    <title>Reyamo</title>
    <style>
        div{
            border-radius: 5%;
            border: 3px solid black;
            width:fit-content;
            margin: 10px;
            background-color: #F0F0F0;
            box-shadow: 0 8px 16px 0 rgba(0,0,0,1);
            transition: 0.3s;
            padding: 10px;
        }
        div:hover{
            background-color: #C5C5C5;
        }
        .wrapper{
            display: flex ;
            flex-wrap: wrap;
        }
        a:link {
            text-decoration: none;
        }

        a:visited {
            text-decoration: none;
        }
        a {
            color: black;
        }

        a:hover {
            text-decoration: underline;
        }

        a:active {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <section class="wrapper">
""")
#Catgory: 0
#Name: 1
#Picture: 2
#Quantity: 3
#Price: 4
#description: 5
#Supplier: 6
#link: 7
hello = open(r'reyamo.csv')
myFile = list(csv.reader(hello))[1:]
for record in myFile:
    if record[0] == "":
        break
    output.write(f"""    <a href="{record[7]}" > <div>
        <h1> Catgory: {record[0]}</h1>
        <h2> Name: {record[1]}</h2>
        <img src="{record[2]}" width="300" height="300">
        <p> <b>Quantity: </b>{record[3]} </p>
        <p> <b>Price: </b>{record[4]} </p>
        <p> <b>Description: </b>{record[5]} </p>
        <!-- <p> <b>Supplier: </b>{record[6]} </p> -->
    </div></a>""")
output.write("""
</section>
</body>
</html>
""")
output.close()
