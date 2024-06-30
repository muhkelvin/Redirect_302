import requests

# Read URLs from a text file
with open('urls.txt', 'r') as file:
    urls = file.read().splitlines()

results = []

for url in urls:
    try:
        response = requests.get(url, allow_redirects=True, timeout=10)  # Set a timeout of 10 seconds
        result = f"Checking {url}\nFinal URL: {response.url}\nStatus Code: {response.status_code}\nHeaders: {response.headers}\n"
        print(result)
        results.append(result)
    except requests.exceptions.Timeout:
        error_message = f"Error checking {url}: Timeout occurred\n"
        print(error_message)
        results.append(error_message)
    except requests.exceptions.RequestException as e:
        error_message = f"Error checking {url}: {e}\n"
        print(error_message)
        results.append(error_message)

# Write results to an output file
with open("output.txt", "w") as f:
    for result in results:
        f.write(result + "\n")
