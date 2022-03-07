from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, target_title):
    return render(request, "encyclopedia/entry.html", {
        "target_title": util.get_entry(target_title)
    })

