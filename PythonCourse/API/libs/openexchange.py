from cachetools import cached, TTLCache
import requests

"""
{
    disclaimer: "https://openexchangerates.org/terms/",
    license: "https://openexchangerates.org/license/",
    timestamp: 1449877801,
    base: "USD",
    rates: {
        AED: 3.672538,
        AFN: 66.809999,
        ALL: 125.716501,
        AMD: 484.902502,
        ANG: 1.788575,
        AOA: 135.295998,
        ARS: 9.750101,
        AUD: 1.390866,
        /* ... */
    }
}
"""

class OpenExchangeClient:
	BASE_URL = "https://openexchangerates.org/api"

	def __init__(self,app_id):
		self.app_id = app_id

	@property
	@cached(cache=TTLCache(maxsize=2, ttl=900))
	def latest(self):
		return requests.get(f"{self.BASE_URL}/latest.json?app_id={self.app_id}").json()

	def convert(self, from_amount, from_currency, to_currency):
		rates = self.latest["rates"]
		to_rate = rates[to_currency]

		if from_currency == "USD":
			return from_amount * to_rate
		else:
			from_in_usd = from_amount / rates[from_currency]
			return from_in_usd * to_rate