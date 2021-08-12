# flat-webpage-api
give a url, get a json 

## API Request

**Endpoint:**
```
http://127.0.0.1:8000/api
```

**Request format**

```
{
  "url": "any url here"
}
```

**Response format**

```
{
  "title": "...",
  "h1": [
    ...
  ],
  "h2": [
    ...  
  ]
  
  ...
}
```


### Example:

**Request**

```
{
  "url": "https://en.wikipedia.org/wiki/Machine_learning"
}
```


**Response:**
```
HTTP 200 OK
Allow: POST, OPTIONS
Content-Type: application/json
Vary: Accept

{
    "title": "Machine learning - Wikipedia",
    "h1": [
        "Machine learning"
    ],
    "h2": [
        "Contents",
        "Overview[edit]",
        "History and relationships to other fields[edit]",
        ...
    ],
    "h3": [
        "Artificial intelligence[edit]",
        "Data mining[edit]",
        "Optimization[edit]",
        ...
        
    ],
    "h4": [
        "Self learning[edit]",
        "Feature learning[edit]",
        "Sparse dictionary learning[edit]",
        ...
    ],
    "h5": [],
    "p": [
        "Machine learning (ML) is the study of computer algorithms that improve 
        automatically through experience and by the use of data.[1]...
        ...
        ]
     "a": [
        {
            "Jump to navigation": "#mw-head"
        },
        {
            "Jump to search": "#searchInput"
        },
        {
            "Machine Learning (journal)": "/wiki/Machine_Learning_(journal)"
        },
        ...
        ]
}
```


