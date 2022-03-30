import random

from django.shortcuts import render, redirect

from . import util
from . import  forms
from .forms import NewEntryForm, NewEditForm
import markdown2


def index(request):
        q = request.GET.get('q')
        entries = util.list_entries()
        if q:
            entries=[e for e in entries if q.lower() in e.lower()]
        if q in util.list_entries():
            return redirect('singleEntry', q)
        return render(request, "encyclopedia/index.html", { "entries":entries
})

def creatEntry (request):
    if request.method=='POST':
        submitted_form = NewEntryForm(request.POST)
        if submitted_form.is_valid():
            en_title=submitted_form.cleaned_data['encyc_title']
            if en_title.lower() in [e.lower() for e in util.list_entries()]:
                msg = "The Encyclopedia with title " + en_title  + " is already exists"
                return render(request, 'encyclopedia/createEntry.html', {'inp_form': submitted_form, 'msg': msg})

            else:
                en_content = submitted_form.cleaned_data['encyc_content']
                util.save_entry(en_title, en_content)
                # return render(request, 'encyclopedia/singleEntry.html', {'entry_title': en_title, 'entry_cont': en_content})
                return redirect('singleEntry', en_title)

        else:
            msg=""
            return render(request, 'encyclopedia/createEntry.html', {'inp_form' : submitted_form,'msg':msg})
    return render(request,'encyclopedia/createEntry.html', {'inp_form' : NewEntryForm(),'msg':''})


def singleEntry(request,title):
    if title in util.list_entries():
        entry_content = markdown2.markdown(util.get_entry(title))
        return render(request, 'encyclopedia/singleEntry.html', {'entry_title': title, 'entry_cont': entry_content})

    else:
        return render(request, 'encyclopedia/errorPage.html',{'title':title})




def randomPage(request):
    ran_tilte=random.choice(util.list_entries())
    #rand_content=markdown2.markdown(util.get_entry(ran_tilte))
    # return render(request,'encyclopedia/singleEntry.html',{'entry_title': ran_tilte, 'entry_cont': rand_content})
    return redirect('singleEntry',ran_tilte)


def editEntry(request, title):
    content=util.get_entry(title)
    editForm=NewEditForm(initial={
        'encyc_title' : title,
        'encyc_content' : content
    })

    if request.method=='POST':
        subm_edit_form=NewEditForm(request.POST)
        if subm_edit_form.is_valid():
            edit_title = subm_edit_form.cleaned_data['encyc_title']
            edit_cont = subm_edit_form.cleaned_data['encyc_content']
            util.save_entry(edit_title,edit_cont)
            return redirect('singleEntry',edit_title)
        else:
            return render(request, 'encyclopedia/editEntry.html', {'entry_title': title, 'edit_form': subm_edit_form})




    return render(request, 'encyclopedia/editEntry.html', {'entry_title': title, 'edit_form': editForm})