<!DOCTYPE html>
{% load static %}
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="{% static "css/style.css" %}">
</head>
<body>
    
    <h1>Help Page!!</h1>
    <div class="dj">
        {% if access_records %}
        {% for i in access_records %}
        <ol>User_Info:
            <li>{{i.first_name}}</li>
            <li>{{i.last_name}}</li>
            <li>{{i.email}}</li>
        </ol>
        {% endfor %}
        {% else %}
        <p>No records found!!!</p>
        {% endif %}
    </div>
</body>
</html>
