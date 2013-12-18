from django.contrib import admin
from polls.models import Poll
from polls.models import Choice

# Register your models here.

class ChoiceInline(admin.TabularInline):  #admin.StackedInline takes up more space
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, 					{'fields': ['question']}),
		('Date information',	{'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question', 'pub_date', 'was_published_recently') # adds descriptions to poll change
	list_filter = ['pub_date'] # adds filter side bar for pub date

admin.site.register(Poll, PollAdmin)