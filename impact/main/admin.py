from django.contrib import admin
from .models import FAQ, VisitorsTime, Visitors, ContactQuestions


class VisitorsTimeInline(admin.TabularInline):
    fk_name = 'Visitors'
    model = VisitorsTime
    extra = 0


@admin.register(VisitorsTime)
class Test(admin.ModelAdmin):
    list_display = ('pk', 'time')
    list_display_links = ('pk',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('pk', 'question', 'answer', 'is_on_homepage')
    list_links = ('pk',)


@admin.register(Visitors)
class VisitorsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'ip_address', 'visited_times')
    list_display_links = ('pk',)
    inlines = [VisitorsTimeInline]


@admin.register(ContactQuestions)
class ContactQuestionsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'subject', 'is_answered', 'time')
    list_display_links = ('pk',)
