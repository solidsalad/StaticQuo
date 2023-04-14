---
title: {{ title }}
date: {{ date }}
tags:
    - prefab
    - travel
    - review
    {% for tag in tags %}
    - {{ tag }}
    {% endfor %}
---
# My experience visiting {{ place }}
Hi guys, my name is {{ name }} and i recently visited {{ place }}
{% if favActivities|length > 0 %}
these were my 5 favorite activities:
{% for activity in favActivities %}
* {{ activity }}
{% endfor %}
{% endif %}

{% if ratingOutOfTen > 7 %}
overall, i gotta say it was a realy cool place, so i'm gonna give it a 
{{ ratingOutOfTen }}/10.
{% elif ratingOutOfTen > 5 %}
I have visited nicer places, but overall it was still a pretty cool journey, so i'm gonna rate {{ place }} {{ ratingOutOfTen }}/10.
{% else %}
I have to say admit that {{ place }} wasn't as cool as i had hoped, thus, i will only give it a {{ ratingOutOfTen }}/10
{% endif %}
cya!!
