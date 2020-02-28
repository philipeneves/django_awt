from rest_framework import viewsets
from .serializers import BookSerializer, BookUserSerializer
from .models import Book, BookUser

class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookUserViewset(viewsets.ModelViewSet):
    queryset = BookUser.objects.all()
    serializer_class = BookUserSerializer

#def book_create(request):
#	form = BookForm(request.POST or None, request.FILES or None)
#	if form.is_valid():
#		instance = form.save(commit=False)
#		instance.user = request.user
#		instance.save()
#		# message success
#		messages.success(request, "Successfully Created")
#		return HttpResponseRedirect(instance.get_absolute_url())
#	context = {
#		"form": form,
#	}
#	return render(request, "book_form.html", context)
#
#def book_detail(request, slug=None): 
#    # dictionary for initial data with  
#    # field names as keys 
#    context ={} 
#  
#    # add the dictionary during initialization 
#    context["data"] = Book.objects.get(slug = slug) 
#          
#    return render(request, "book-detail.html", context) 
#
#def book_list(request):
#	queryset_list = Book.objects.all()
#
#	context = {
#		"object_list": queryset_list, 
#		"title": "List",
#	}
#	return render(request, "book_list.html", context)
#