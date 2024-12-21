from robots_explorer.robots_explorer import fetch_robots_txt


def main():
    website_url = "https://info.issauga.lt/"  # Replace with your target website
    robots_content = fetch_robots_txt(website_url)
    if robots_content:
        print("\nExplanation:")
        print("This file provides rules for bots accessing the website.")

if __name__ == "__main__":
    main()