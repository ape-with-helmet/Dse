import requests, json
from collections import Counter
endpoint = "https://api.github.com/users/ape-with-helmet/repos"
repos = json.loads(requests.get(endpoint).text)

from dateutil.parser import parse
dates = [parse(repo["created_at"]) for repo in repos]
month_counts=Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)
print(month_counts)
print(weekday_counts)
