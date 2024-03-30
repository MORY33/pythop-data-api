Python data api

## Routes
[.env is not in .gitignore on purpose]
## Get all routes
```http
GET /routes
{
{
    "route_id": "int",
    "from_port": "str",
    "to_port": "str",
    "leg_duration": "int"
  },
  ...
  }
```

## Get a single route by its ID
```http
GET /routes/{route_id}
{
{
  "id": 1,
  "route_id": "int",
  "from_port": "str",
  "to_port": "str",
  "leg_duration": "int",
  "points": [
    {
      "longitude": "float",
      "latitude": "float",
      "timestamp": "int",
      "speed": "float"
    }
  ]
}
  ...
  }
```


## RUN PROJECT

To run this project you need docker and docker-compose.

Go to project directory and run 

```bash```
docker-compose up --build

## AUTHORS
[@MORY33](https://www.github.com/MORY33)