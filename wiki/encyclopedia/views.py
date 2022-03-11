import re
from urllib import request
from django.shortcuts import render

from markdown2 import markdown

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_page(request, title):

    content = util.get_entry(title)

    if content == None:
        content = "Error page not found"
    content = markdown(content)
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content,
    })

def search(request):
    
    q_dict = request.GET
    q = q_dict['q']

    results = []
    entries = util.list_entries()

    for entry in entries:
        if q.capitalize().find(entry.capitalize()) != -1: 
            results.append(entry)

    return render(request, "encyclopedia/search.html", {
        "query": q,
        "results": results,
    })