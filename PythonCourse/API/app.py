import time
from libs.openexchange import OpenExchangeClient

APP_ID = "6fdb88c9dda14a21bd02bcb5d156ad23"

client = OpenExchangeClient(APP_ID)

start = time.time()
usd_amount = 1
gbp_amount = client.convert(usd_amount,"USD","GBP")
end = time.time()
print("Elapsed time: %s" %(end-start))

# print("USD: %f GBP: %f " % (usd_amount,gbp_amount))


