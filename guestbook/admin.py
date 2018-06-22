from django.contrib import admin

from .models import Team,Portfolio,Services,About,Clients,Privacy,TermsOfUse,FooterLinks

admin.site.register(Team)
admin.site.register(Portfolio)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Clients)

admin.site.register(Privacy)
admin.site.register(TermsOfUse)
admin.site.register(FooterLinks)

