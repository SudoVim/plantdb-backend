# plantdb-backend

Backend REST API for plantdb.

## API

`/v1/categories/`

Returns `array` of available categories:

```
[
  "<category_1>",
  "<category_2>",
  ...
]
```

`/v1/plants/`

Returns `array` of all plants. Each item looks like:

```
{
  "name": "<plant_name>",
  "latin": "<latin_name>",
  "category": "<category>",
  "description": "<plant_description>",
  "tags": [
    "tag_1",
    "tag_2"
  ]
}
```

Possible keys are:

* **category** - category to filter on
* **tags** - comma-separated list of tags to search for
