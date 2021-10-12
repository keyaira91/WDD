from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review
class BookAdmin(admin.ModelAdmin):
    date_hierarchy = 'publication_date'
    list_display = ('title', 'isbn13')
    list_filter = ('publisher', 'publication_date',)
    search_fields = ('title', 'isbn', 'publisher__name__startswith')
    def isbn13(self, obj):
        return "{}-{}-{}-{}-{}".format(obj.isbn[0:3], obj.isbn[3:4], \
            obj.isbn[4:6], obj.isbn[6:12], obj.isbn[12:13])

class ReviewAdmin(admin.ModelAdmin):
    exclude = ('date_edited',)
    fieldsets = ((None, {'fields': ('creator', 'book')}), \
        ('Review content', {'fields': ('content', 'rating')}))


# Register your models here.

admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review, ReviewAdmin)

