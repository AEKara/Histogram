from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from django.template.loader import get_template


import os.path
BASE = os.path.dirname(os.path.abspath(__file__))


import string

def histogram(request,offset): #Parameter offset is from url coming ofter histogram/....

    file = open(os.path.join(BASE, "../templates/"+offset)) #offset is file name. My offsets under templates
    filedata = file.read()
    words=string.split(filedata)
    histogram = {}
    for word in words:
            histogram[word] = histogram.get(word, 0) + 1
    #for word in histogram.keys():
    #histogram_result = 'Word: %s - count %s' % (word, str(histogram[word]))

    t = get_template('file_to_display.html')
    html = t.render(Context({'frequency': histogram,'name':offset}))
    return HttpResponse(html)




