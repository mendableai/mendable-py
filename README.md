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


## Basic Usage

You can use this package to add sources to Mendable and ask questions to it (history is an option parameter):

```python
from mendable import ChatApp

my_chat_bot = ChatApp(api_key="your-api-key")

my_chat_bot.add("url", "https://www.mendable.ai/")

answer = my_chat_bot.ask(question="What is Mendable?", history=[{ "prompt" : "How do I create a new project?", "response" : "You can create a new project by going to the projects page and clicking the new project button." }])

print(answer['answer']['text'])
```

Here is what the ask methods response object looks like:

```json
{
  "answer": {
    "text": "This is how to deploy it..."
  },
  "message_id": 123,
  "sources": [
    {
      "id": 866,
      "content":"",
      "link": "",
      "relevance_score": 0.99
    },
  ]
}
```


## Rate Message

This is how you can rate a message positive (1) or negative (0).

```python
from mendable import ChatApp

my_chat_bot = ChatApp(api_key="your-api-key")

my_chat_bot.add("url", "https://www.mendable.ai/")

answer = my_chat_bot.ask(question="What is Mendable?", history=[{ "prompt" : "How do I create a new project?", "response" : "You can create a new project by going to the projects page and clicking the new project button." }])

message_id = answer["message_id"]

my_chat_bot.rate_message(message_id, 1)
```

## See all sources for project

This method lists all unique sources for a project.

```python
from mendable import ChatApp

my_chat_bot = ChatApp(api_key="your-api-key")

my_chat_bot.add("url", "https://www.mendable.ai/")

my_chat_bot.get_sources()

```

The response object looks like this:
```json
[
  {
    "id": 52,
    "source": "https://mendable.ai"
  },
  ..
]
```

## Add and Delete Indexes

You can also check/delete indexes using `get_sources` and `delete_source` functions:

```python
from mendable import ChatApp

my_chat_bot = ChatApp(api_key="your-api-key")

my_chat_bot.add("url", "https://www.mendable.ai/")

my_chat_bot.get_sources()

my_chat_bot.delete_source("https://www.mendable.ai/")
```

### Supported ingestion formats and type

- Website Crawler URL -> "website-crawler"
- Docusaurus site URL -> "docusaurus"
- GitHub Repo URL -> "github"
- YouTube Video URL -> "youtube"
- Single Website URL -> "url"
- Sitemap URL -> "sitemap"
- OpenAPI YAML URL -> "openapi"

## Start new conversation

This method makes a new conversation for a given project

```python
from mendable import ChatApp

my_chat_bot = ChatApp(api_key="your-api-key")

my_chat_bot.start_new_conversation()

```


## License

This project is licensed under the terms of the MIT license.

---

Please make sure to replace `your_api_key` with your actual API key and modify any part of this README according to your needs before adding it to your package.
