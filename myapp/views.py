import io
import sys
from http.client import responses

#from django.db.models.fields import return_None
from django.http import HttpResponse, JsonResponse, FileResponse
from django.shortcuts import render
from myapp.models import Student
import io
from reportlab.pdfgen import canvas


# Create your views here.
def home(request):
    response = HttpResponse('Welcome back!')
    return response

def info(request):
    r = HttpResponse(sys.version)
    return r

def data(request):
    d = {
        '67000000':{
            'first_name': 'Luffy',
            'last_name': 'D'

        },
        '7000000':{
            'first_name': 'ACE',
            'last_name': 'D'
        }
    }
    return JsonResponse(d)

def pdf(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")

def students(request):
    context = {}
    context['object_list'] = Student.objects.all()[:11]
    context['object_list'] = Student.objects.filter(name__icontains = 'พ')
    context['object_list'] = Student.objects.filter(name__endswith = 'm')
    context['object_list'] = Student.objects.filter(name__startswith = 'm')
    return render(request,'myapp/students.html',context)


