import requests
from bs4 import BeautifulSoup
import re
import json

# Target URL
url = "https://www.rightmove.co.uk/house-prices/details/england-152030015-22576921?s=2d6175fdb2c4af2cb418e7f8a6a7d6d8b2a6cb7873661efd78cf90a19a5c8396"

# Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

# Send HTTP request
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the script tag containing PAGE_MODEL
script_tag = soup.find('script', string=re.compile('window.PAGE_MODEL'))

if script_tag:
    print("[+] Found target script")

    # Extract the script content
    script_content = script_tag.string.strip()

    # Remove "window.PAGE_MODEL = " prefix
    prefix = 'window.PAGE_MODEL = '
    if script_content.startswith(prefix):
        json_str = script_content[len(prefix):].rstrip('; \n')

        try:
            # Parse JSON
            data = json.loads(json_str)
            print("[+] Successfully parsed JSON")

            # Optional: print metadata
            # print(data.get('metadata', {}))

            # Save to JSON file
            with open('output.json', 'w', encoding='utf-8') as f:
                property_data = data.get("soldPropertyData")
                
                # Extract images
                images = property_data["property"]["images"]

                # Prepare a list of image URLs
                image_urls = []
                for img in images:
                    image_info = {"url": img.get("url")}
                    image_urls.append(image_info)

                property_details = {
                    "property_name": property_data["address"]["displayAddress"],
                    "date_sold": property_data["transactions"][0]["displayDeedDate"],
                    "price": property_data["transactions"][0]["displayPrice"],
                    "property_type": property_data["propertyType"],
                    "tenure": property_data["transactions"][0]["tenure"],
                    "key_features": property_data["property"]["keyFeatures"],
                    "images": image_urls,
                    "floot_plan": property_data["property"]["floorplans"][0]["url"],
                    "location": {
                        "latitude": property_data["property"]["streetView"]["latitude"],
                        "longitude": property_data["property"]["streetView"]["longitude"]   
                    }
                }
                
                json.dump(property_details, f, indent=4, ensure_ascii=False)
            print("[+] Data saved to output2.json")

        except json.JSONDecodeError as e:
            print("[-] JSON parsing failed:", e)
            print("Partial content:", json_str[:500])  # Debug

    else:
        print("[-] Script content does not start with expected prefix")
else:
    print("[-] Target script not found")
