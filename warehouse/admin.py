from django.contrib import admin

# Register your models here.

from .models import AWS, AWS_files, AWS_Budget, Domain, IsAlive, High_Level_Budget, Budget_Detail, GL

admin.site.register(AWS)
admin.site.register(AWS_files)
admin.site.register(AWS_Budget)
admin.site.register(Domain)
admin.site.register(IsAlive)
admin.site.register(High_Level_Budget)
admin.site.register(Budget_Detail)
admin.site.register(GL)
