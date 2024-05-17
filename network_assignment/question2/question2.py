import requests
import time
from datetime import datetime
import pytz

def read_subdomains_from_file(filename):
    with open(filename, "r") as file:
        subdomains = file.read().splitlines()
    return subdomains

def check_subdomains(subdomains):
    current_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    while True:
        print("-" * 70)
        print("{:<20} {:<10} {:<5}".format("Subdomain", "Status", "Current Time (IST)"),current_time)
        print("-" * 70)
        for subdomain in subdomains:
            try:
                response = requests.get("http://" + subdomain)
                if response.status_code == 200:
                    status = "UP"
                else:
                    status = "DOWN"
                print("{:<20} {:<10}".format(subdomain, status))
            except requests.ConnectionError:
                print("{:<20} {:<10}".format(subdomain, "DOWN"))
        print("-" * 50)
        time.sleep(60)  # Wait for 60 seconds before checking again

if __name__ == "__main__":
    filename = "subdomains.txt"  # Change this to your file name
    subdomains = read_subdomains_from_file(filename)
    check_subdomains(subdomains)

