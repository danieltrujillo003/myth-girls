from django.shortcuts import render
from chicas.forms import new_entryForm 
from django.http import HttpResponseRedirect, HttpResponse
from chicas.models import new_entry 

def story(request):
    """story = "Habia una vez un barco chiquito\
 Habia una vez un chiquito barco\
 Habia una vez un chiquito barco\
 Tan chiquito, tan chiquito que no podia navegar"
    #story_list = story.split()
    spaces_index = []
    story2 = story
    spaces = story.find(" ")
    story_list2 = []
    spaces_index2 = []
    story3 = ""
    i=0
    #anyt = ""

    while len(story2) > 10:
        spaces_index.append(spaces)
        #lalalalalalala
        story2 = story[spaces+1:]
        spaces += (story2.find(" ")+1)
        #story = underlined.story.find(" ")


    for index in spaces_index:
        index2 = index + 1
        #anyt += each_space

    for char in story:
        story_list2.append(char)

    for char in story_list2:
        if char = " ":
            story_list2[story_list2.index(char)] = "<span> </span>"
"""
    if request.method == 'POST':
        form = new_entryForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/chicas/story/')
        else:
            print form.errors
    else:
        form = new_entryForm()

    
        entry_list = new_entry.objects.filter(space__in="modal1")

    return render(request, 'chicas/story.html', {'entry': form, 'entries': entry_list})