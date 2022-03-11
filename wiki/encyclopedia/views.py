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

    q_dict = request.GET
    
    if q_dict['title'] != None:
        title = q_dict['title']
        content = q_dict['content']

        util.save_entry(title, content)
    else:
        content = util.get_entry(title)

    ## Generates page not found error
    if content == None:
        content = "Error page not found"

    ## Convert markdown content to html page
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
        if q.capitalize() in entry.capitalize(): 
            results.append(entry)

    return render(request, "encyclopedia/search.html", {
        "query": q,
        "results": results,
    })

def create(request):
    return render(request, "encyclopedia/create.html")