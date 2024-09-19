from django.contrib import admin
from .models import (
    Agentname,
    AnnouncedLgaResults,
    AnnouncedPuResults,
    AnnouncedStateResults,
    AnnouncedWardResults,
    Lga,
    Party,
    PollingUnit,
    States,
    Ward
)

# Custom Admin for Agentname
class AgentnameAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'email', 'phone', 'pollingunit_uniqueid')
    search_fields = ('firstname', 'lastname', 'email', 'phone')
    list_filter = ('pollingunit_uniqueid',)

# Custom Admin for AnnouncedLgaResults
class AnnouncedLgaResultsAdmin(admin.ModelAdmin):
    list_display = ('lga_name', 'party_abbreviation', 'party_score', 'entered_by_user', 'date_entered', 'user_ip_address')
    search_fields = ('lga_name', 'party_abbreviation', 'entered_by_user')
    list_filter = ('lga_name', 'party_abbreviation')

# Custom Admin for AnnouncedPuResults
class AnnouncedPuResultsAdmin(admin.ModelAdmin):
    list_display = ('polling_unit_uniqueid', 'party_abbreviation', 'party_score', 'entered_by_user', 'date_entered', 'user_ip_address')
    search_fields = ('polling_unit_uniqueid', 'party_abbreviation', 'entered_by_user')
    list_filter = ('polling_unit_uniqueid', 'party_abbreviation')

# Custom Admin for AnnouncedStateResults
class AnnouncedStateResultsAdmin(admin.ModelAdmin):
    list_display = ('state_name', 'party_abbreviation', 'party_score', 'entered_by_user', 'date_entered', 'user_ip_address')
    search_fields = ('state_name', 'party_abbreviation', 'entered_by_user')
    list_filter = ('state_name', 'party_abbreviation')

# Custom Admin for AnnouncedWardResults
class AnnouncedWardResultsAdmin(admin.ModelAdmin):
    list_display = ('ward_name', 'party_abbreviation', 'party_score', 'entered_by_user', 'date_entered', 'user_ip_address')
    search_fields = ('ward_name', 'party_abbreviation', 'entered_by_user')
    list_filter = ('ward_name', 'party_abbreviation')

# Custom Admin for Lga
class LgaAdmin(admin.ModelAdmin):
    list_display = ('lga_name', 'state_id', 'entered_by_user', 'date_entered', 'user_ip_address')
    search_fields = ('lga_name', 'entered_by_user')
    list_filter = ('state_id',)

# Custom Admin for Party
class PartyAdmin(admin.ModelAdmin):
    list_display = ('partyid', 'partyname')
    search_fields = ('partyid', 'partyname')

# Custom Admin for PollingUnit
class PollingUnitAdmin(admin.ModelAdmin):
    list_display = ('polling_unit_number', 'polling_unit_name', 'ward_id', 'lga_id', 'entered_by_user', 'date_entered', 'user_ip_address')
    search_fields = ('polling_unit_number', 'polling_unit_name', 'entered_by_user')
    list_filter = ('ward_id', 'lga_id')

# Custom Admin for States
class StatesAdmin(admin.ModelAdmin):
    list_display = ('state_id', 'state_name')
    search_fields = ('state_name',)

# Custom Admin for Ward
class WardAdmin(admin.ModelAdmin):
    list_display = ('ward_name', 'lga_id', 'entered_by_user', 'date_entered', 'user_ip_address')
    search_fields = ('ward_name', 'entered_by_user')
    list_filter = ('lga_id',)

# Registering models with their custom admin classes
admin.site.register(Agentname, AgentnameAdmin)
admin.site.register(AnnouncedLgaResults, AnnouncedLgaResultsAdmin)
admin.site.register(AnnouncedPuResults, AnnouncedPuResultsAdmin)
admin.site.register(AnnouncedStateResults, AnnouncedStateResultsAdmin)
admin.site.register(AnnouncedWardResults, AnnouncedWardResultsAdmin)
admin.site.register(Lga, LgaAdmin)
admin.site.register(Party, PartyAdmin)
admin.site.register(PollingUnit, PollingUnitAdmin)
admin.site.register(States, StatesAdmin)
admin.site.register(Ward, WardAdmin)
