# 🕸️ Web-Scraping

This repository demonstrates two different approaches to web scraping in Python:

1. **Static Scraping** – Using standard libraries like `requests` and `BeautifulSoup` to parse HTML and extract data embedded in JavaScript variables.
2. **Spider-Based Scraping** – Using Scrapy spiders to crawl pages and extract structured data embedded inside `<script>` tags.

---

## 📁 Project Structure

```
Web-Scraping/
├── static_scraping/     # Static HTML scraping with JS data extraction
├── spider_scraping/     # Scrapy spider for JS-embedded JSON extraction
├── requirements.txt     # List of dependencies
├── LICENSE              # MIT License
└── README.md            # Project overview
```

---

## 🧰 Technologies Used

- `requests` – for sending HTTP requests (in static scraping)
- `beautifulsoup4` – for HTML parsing
- `re` – for regex matching `<script>` tags
- `json` – to parse JavaScript-embedded JSON
- `scrapy` – for spider-based web scraping

---

## 🔎 Scraping Methods

### 1. 📦 Static Scraping (`static_scraping/`)

**Technique:**  
`HTML Parsing + Embedded JavaScript Data Extraction`

- Loads the page with `requests`
- Parses the HTML using `BeautifulSoup`
- Locates a `<script>` tag with `window.PAGE_MODEL = {...}` JavaScript object
- Extracts and converts the embedded JSON into structured Python data

👉 Best for websites where JSON data is embedded directly in the HTML source.

---

### 2. 🕷️ Spider-Based Scraping (`spider_scraping/`)

**Technique:**  
`Spider-Based HTML Parsing with Embedded JavaScript Data Extraction`

- Uses Scrapy to crawl pages
- Extracts JavaScript-embedded data in `<script>` tags
- Processes and stores it using Scrapy's item pipeline or file output

👉 Ideal for scraping multiple pages or when you want scalable crawling logic.

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/SAKTHIVINASH2/Web-Scraping.git
   cd Web-Scraping
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage

### Static Scraping
Navigate to the `static_scraping` directory and run the script:

```bash
cd static_scraping
python scrape_static.py
```

### Spider-Based Scraping (using Scrapy)
Navigate to the `spider_scraping` directory and run:

```bash
cd spider_scraping
scrapy crawl property_spider
```

---

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE) file for details.

---

## 🙌 Author

- [Sakthivinash](https://github.com/SAKTHIVINASH2)

---

## ⭐️ Give a Star!

If you found this repository useful, consider giving it a ⭐ to support the project!
