from django.contrib import admin
from .models import Genre, FilmWork, GenreFilmWork, Person, PersonFilmWork
from django.utils.translation import gettext_lazy as _

admin.site.empty_value_display = '???'


class RatingListFilter(admin.SimpleListFilter):
    title = _('Ratings')

    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return (
            ('bad_films', '0-4'),
            ('normal_films', '4-7'),
            ('good_films', '7-8.5'),
            ('excellent_films', '8.5-10')
        )

    def queryset(self, request, queryset):
        if self.value() == 'bad_films':
            print()
            return queryset.filter(rating__gte=0,
                                   rating__lt=4)
        if self.value() == 'normal_films':
            return queryset.filter(rating__gte=4,
                                   rating__lte=7)
        if self.value() == 'good_films':
            return queryset.filter(rating__gte=7,
                                   rating__lt=8.5)
        if self.value() == 'excellent_films':
            return queryset.filter(rating__gte=8.5,
                                   rating__lte=10)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    search_fields = ('name', 'description', 'id')


class PersonFilmWorkInline(admin.TabularInline):
    model = PersonFilmWork
    autocomplete_fields = ("person",)


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name',)
    search_fields = ('full_name', 'id')
    date_hierarchy = 'created'


class GenreFilmWorkInline(admin.TabularInline):
    model = GenreFilmWork


@admin.register(FilmWork)
class FilmWorkAdmin(admin.ModelAdmin):
    inlines = (GenreFilmWorkInline, PersonFilmWorkInline)
    list_display = ('title', 'type', 'creation_date', 'rating')
    list_filter = ('type', RatingListFilter, 'genres')
    date_hierarchy = 'creation_date'
    search_fields = ('title', 'description', 'id')
