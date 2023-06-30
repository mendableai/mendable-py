# Mendable Python SDK

This is a Python SDK for Mendable.ai, which provides a Python interface to interact with Mendable.ai's API.

## Installation

To install this package, use pip:

```bash
pip install mendable-py
```

## Prerequisites

To use this package, you'll need to obtain an API key from Mendable.ai and make it available as an environment variable or set it in the constructor.

In your environment (add to .env file):

```bash
MENDABLE_API_KEY=your_api_key
```

OR

```python
my_chat_bot = ChatApp(api_key="your-api-key")
```


## Usage

You can use this package to add sources to Mendable and ask questions to it:

```python
from mendable import ChatApp

my_chat_bot = ChatApp(api_key="your-api-key")

my_chat_bot.add("url", "https://www.mendable.ai/")

answer = my_chat_bot.query("What is Mendable?")
print(answer)
```

## Supported ingestion formats and type

- Website Crawler URL -> "website-crawler"
- Docusaurus site URL -> "docusaurus"
- GitHub Repo URL -> "github"
- YouTube Video URL -> "youtube"
- Single Website URL -> "url"
- Sitemap URL -> "sitemap"
- OpenAPI YAML URL -> "openapi"


## License

This project is licensed under the terms of the MIT license.

---

Please make sure to replace `your_api_key` with your actual API key and modify any part of this README according to your needs before adding it to your package.
