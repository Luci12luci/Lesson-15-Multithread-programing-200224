import urllib.request
import time
from concurrent.futures import ThreadPoolExecutor


def download_site(url):
    print("Stahujem..." + url)
    with urllib.request.urlopen(url) as response:
        return f"Stiahnutie {url}: {len(response.read())} bytov"


sites = [
    "https://www.example.com",
    "https://www.example.org",
    "https://www.example.net",
]

threads = []
start_time = time.time()

with ThreadPoolExecutor(max_workers=3) as executor:
    futures = []
    for site in sites:
        futures.append(executor.submit(download_site, site))

    for future in futures:
        result = future.result()
        print(result)

duration = time.time() - start_time
print(f"Stiahnute {len(sites)} stranok za {duration} sekund")
