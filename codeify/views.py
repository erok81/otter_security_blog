from django.shortcuts import render
from django.http import HttpResponse
from codeify.forms import EncodeForm

# Create your views here.
def codeify(request):

    if request.method == 'GET':
        form = EncodeForm()
        context = {'form': form}


    else:
        form = EncodeForm(request.POST)
        context = {'form': form}

        if form.is_valid():
            #what = form.cleaned_data['what']
            input_type = form.cleaned_data['input_type']
            output_type = form.cleaned_data['output_type']
            input_text = form.cleaned_data['input_text']
            direction = form.cleaned_data['option']
            something = request.POST.get('option1')

            resulted = results()

            context.update({'form':form, 'resulted':resulted
            })

            print(input_type, output_type, input_text, direction, something)







    return render(request, 'coder.html', context)


def results():
    some_value = 'this will be returned data section'
    return some_value