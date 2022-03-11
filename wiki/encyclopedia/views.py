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

def search(title):
    
    q = request.Get.get('q')

    results = []

    if q in util.list_entries:
        ## TODO: clean up query
        results.append(q)

    return render(request, "encyclopedia/search.html", {
        "results": results
    })