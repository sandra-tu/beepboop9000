# from django.views.generic.base import TemplateView
# from .models import Organisation
from django.shortcuts import render
from django.http import Http404
from register.models import Organisation
from django.views.generic import ListView
from django.db.models import Q
#
# class ViewPageView(TemplateView):
#     model = Organisation
#     template_name = "view/view.html"

def view_view(request):
    # orgs = Organisation.objects.all()
    search_organisation = request.GET.get('search')

    if search_organisation:
        organisations = Organisation.objects.filter(Q(name__icontains=search_organisation))
    else:
        # If not searched, return default posts
        organisations = Organisation.objects.all().order_by("name")
    return render(request, 'view/view.html', {'orgs': organisations})
    

# class SearchView(ListView):
#     model = Organisation
#     template_name = 'view.html'
#     # context_object_name = 'all_search_results'

#     # def get_queryset(self):
#     #    result = super(SearchView, self).get_queryset()
#     #    query = self.request.GET.get('search')
#     #    if query:
#     #       postresult = Organisation.objects.filter(name__contains=query)
#     #       result = postresult
#     #    else:
#     #        result = None
#     #    return result

#     def get_queryset(self): # new
#         query = self.request.GET.get('q')
#         if query == None:
#             object_list = Organisation.objects.all()
#         else:
#             object_list = Organisation.objects.filter(
#                 Q(name__icontains=query)
#             )
#         return object_list