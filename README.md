# 🕷️ Spider — Web Crawler Tool

> A lightweight Python tool that recursively crawls websites, extracts URLs, and filters them by keyword.
---
![Spider Demo](https://github.com/user-attachments/assets/943154e0-7ee5-4696-9cb4-b70142f7fb89)


## 🚀 Features

- 🔍 **Recursive crawling** — follows links automatically across pages
- 🏷️ **Keyword-based URL filtering** — surface only the URLs you care about
- 📏 **Depth control** — define how deep the crawler should go
- ⚡ **Lightweight & fast** — minimal dependencies, quick setup
- 🛡️ **Error handling** — gracefully handles broken links and timeouts

---

## 📦 Installation

```bash
git clone https://github.com/your-username/spider.git
cd spider
pip install requests beautifulsoup4
```

---

## ▶️ Usage

```bash
python spider.py
```

You'll be prompted to enter:
- **Target URL** — the site to crawl
- **Keywords** — filter URLs containing specific terms
- **Depth** — how many levels deep to crawl

---

## 🧠 How It Works

```
Start URL
   │
   ▼
Fetch HTML ──► Extract all <a href="..."> links
   │
   ▼
Filter by keyword
   │
   ▼
Recurse into matching URLs (up to max depth)
   │
   ▼
Output filtered URL list
```

---

## 📁 Project Structure

```
spider/
├── spider.py        # Main crawler script
├── README.md        # Documentation
```

---

## 🧪 Example Output

```
[*] Crawling: https://example.com
[+] Found: https://example.com/admin/login
[+] Found: https://example.com/admin/dashboard
[-] Skipped: https://example.com/about (no keyword match)

Total URLs found: 2
```

---

## ⚠️ Disclaimer

This tool is intended **for educational and authorized testing purposes only.**
Do **not** use it on websites without explicit permission from the owner.
Unauthorized crawling may violate terms of service and applicable laws.

---

## 👨‍💻 Author

**Dharun R** — Cybersecurity Student

[![GitHub](https://img.shields.io/badge/GitHub-your--username-181717?style=flat&logo=github)](https://github.com/Dharun1319)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
