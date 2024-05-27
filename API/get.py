import requests

try:
    print("Sending GET request...")
    response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
    
    print(f"HTTP Status Code: {response.status_code}")  # Print the HTTP status code
    
    # Check if the request was successful
    if response.status_code == 200:
        print("Response JSON Data:")
        print(response.json())  # Print the JSON response body
    else:
        print("Failed to retrieve data.")
        print("Response Content:", response.text)  # Print response content for debugging

except requests.exceptions.HTTPError as errh:
    print("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
    print("Connection Error:", errc)
except requests.exceptions.Timeout as errt:
    print("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
    print("Error:", err)
