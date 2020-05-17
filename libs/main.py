from api import Genius

api = Genius("bEqP-2oD05hhOkoeYFMVkc_AuXRgTDxh547rguq9ngdXkmUi0hTgm90zUULdiAXO")

result = api.get_url_from_search("Dreams of you", "Brennan Savage")
print(result)
