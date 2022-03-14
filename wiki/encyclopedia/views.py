import re
from urllib import request
from django.shortcuts import render, redirect

from markdown2 import markdown
from random import randint

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def get_page(request, title):

    q_dict = request.GET
    
    content = util.get_entry(title)

    ## Generates page not found error
    if content == None:
        content = "Error page not found 404"

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

def new_page(request):

    q_dict = request.GET

    title = q_dict['title']
    content = q_dict['content']

    util.save_entry(title, content)

    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def random(request):
    ## TODO: figure out why entry title does not display
    entries = util.list_entries()
    idx = randint(0, len(entries)-1)

    title = entries[idx]
    content = markdown(util.get_entry(title))

    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content,
    })


def create(request):

    if request.method == "POST":

        ## Fetch title and content using POST
        # title = request.POST.get('title').strip()
        # content = request.POST.get('content').strip()q_dict = request.GET

        q_dict = request.POST

        title = q_dict['title']
        content = q_dict['content']

        ## Check for empty or duplicate cases
        if title == "" or content == "":
            return render(request, "encyclopedia/create.html", {"message": "Can't save with empty field.", "title": title, "content": content})
        if title in util.list_entries():
            return render(request, "encyclopedia/create.html", {"message": "Title already exist. Try another.", "title": title, "content": content})

        ## Save entry and redirect to the new page
        util.save_entry(title, content)
        return redirect("entry", title=title)

    return render(request, "encyclopedia/create.html")

def edit(request, title):

    content = util.get_entry(title.strip())
    if content == None:
        return render(request, "encyclopedia/edit.html", {'error': "404 Not Found"})

    if request.method == "POST":

        q_dict = request.POST
        content = q_dict['content']

        ## Check for empty or duplicate cases
        if title == "" or content == "":
            return render(request, "encyclopedia/create.html", {"message": "Can't save with empty field.", "title": title, "content": content})
        
        ## Save entry and redirect to the new page
        util.save_entry(title, content)

        return redirect("entry", title=title)

    return render(request, "encyclopedia/edit.html", {'content': content, 'title': title})
