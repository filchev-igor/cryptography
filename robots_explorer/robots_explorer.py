import requests

def fetch_robots_txt(url):
    """Fetch and explain the robots.txt file from a website."""
    robots_url = url + "/robots.txt"
    try:
        response = requests.get(robots_url)
        if response.status_code == 200:
            print(f"robots.txt from {url}:")
            print(response.text)
            return response.text
        else:
            print(f"No robots.txt file found at {robots_url} (HTTP {response.status_code})")
            return None
    except Exception as e:
        print(f"Error fetching robots.txt: {e}")
        return None

if __name__ == "__main__":
    website_url = "https://example.com"  # Replace with your target website
    robots_content = fetch_robots_txt(website_url)
    if robots_content:
        print("\nExplanation:")
        print("This file provides rules for bots accessing the website.")
