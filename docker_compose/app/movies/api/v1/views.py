from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q, F
from django.http import JsonResponse
from django.views.generic.list import BaseListView
from django.views.generic.detail import DetailView
from django.db.models.functions import Coalesce
from django.shortcuts import render
from movies.models import FilmWork


class MoviesApiMixin:
    model = FilmWork
    http_method_names = ['get']
    paginate_by = 50

    def get_queryset(self):
        queryset = self.__class__.model.objects.prefetch_related('genres', 'persons').all().values('id', 'title',
                                                                                                   'description',
                                                                                                   'creation_date',
                                                                                                   'type').annotate(
            rating=Coalesce(F('rating'), 0.0),
            genres=ArrayAgg('genres__name', distinct=True),
            actors=ArrayAgg('persons__full_name', distinct=True, filter=Q(personfilmwork__role='actor')),
            writers=ArrayAgg('persons__full_name', distinct=True, filter=Q(personfilmwork__role='writer')),
            directors=ArrayAgg('persons__full_name', distinct=True, filter=Q(personfilmwork__role='director'))
        )

        return queryset

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(
            queryset,
            self.paginate_by
        )
        context = {"count": paginator.count,
                   "total_pages": paginator.num_pages,
                   "prev": page.previous_page_number() if page.has_previous() else None,
                   "next": page.next_page_number() if page.has_next() else None,
                   "results": list(queryset),
                   "is_paginated": is_paginated
                   }
        return context


class MoviesDetailApi(MoviesApiMixin, DetailView):

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)['object']
        return context


def home(request):
    return render(request, 'static.html')
