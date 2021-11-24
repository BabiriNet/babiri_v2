# Backend Architecture

The backend architecture processes the time-series usage and global ranking snapshots from Pokémon Showdown.

# Tech Stack

-   Go
-   AWS Lambda
-   AWS DynamoDB
-   AWS API Gateway
-   AWS Cloudwatch
-   AWS Virtual Private Cloud
-   AWS Elasticache

# Microservice Architecture

## Handler

The handler layer validates the incoming request. Following validation, the request is transformed into an internal object.

## Service

The service layer handles the business logic.

## DAO

The DAO layer is responsible for interfacing with the database.

# Database Schema

Document tables are separated by formats. For instance, if there are 5 formats supported, there will be 10 tables total.

## Pokémon Team Snapshots

Document for individual team snapshots and ranking metadata.

```javascript
{
    date: datetime,                 // mm/dd/yy
    format: str,
    pokemon_list: [str],
    rating: int,
    replay_upload_date: datetime    // mm/dd/yy
}
```

## Pokémon Usage Snapshots

Document for individual Pokémon usage data out of all ranked teams.

```javascript
{
    date: datetime,
    format: str,
    pokemon_usage: {            // List of Pokémon usage as number of appearances
        [
            str: int
        ]
    },
    pokemon_partners: {
        [
            str: [              // List of Pokémon recorded
                {
                    str: int    // Denotes Pokémon's partners as number of appearances
                }
            ]
        ]
    },
    average_rating: {           // Denotes Pokémon's average rating between all appearances
        [
            str: float
        ]
    },
    core_usage: {               // Denotes cores of three Pokémon as number of appearances
        [
            [str]: int
        ]
    }
}
```

# Endpoints

## `GET api/health`

Get API health status.

### Request

```console
curl /api/health
```

### Response

```console
200 OK
```

## `GET api/formats`

Get supported formats.

### Request

```console
curl /api/formats
```

### Response

```console
{
    formats: ["gen8vgc2021", "gen8ou", "gen8uu", "gen8ru", "gen8nu"]
}
```

## `GET /api/teams/{format}/{date}`

Get most recent recorded teams for specific format.
Defaults to recent VGC format if format not provided (eg. `gen8vgc2021`).
Defaults to most recent if date is not given.

### Request

```console
curl /api/teams/gen8ou/2021-12-15
```

### Response

```console
{
    date: 2021-12-15,
    format: gen8ou,
    teams: {
        {
            pokemon_list: ["Chansey", "Landorus-Therian", "Melmetal", "Kartana", "Dragapult", "Kyurem"],
            rating: 1430,
            replay_upload_date: 2021-10-19
        },
        {
            ...
        }
    }
}
```

Get most recent teams filtered by Pokémon and date.

### Request

```console
curl /api/teams/gen8vgc2021/2021-10-09 \
    -F 'pokemon[]=incineroar' \
    -F 'pokemon[]=rillaboom'
```

### Response

```console
{
    date: 2021-10-09,
    format: gen8vgc2021,
    teams: {
        {
            pokemon_list: ["charizard", "incineroar", "gyarados", "rillaboom", "magnezone", "clefairy"],
            rating: 1430,
            replay_upload_date: 12-10-19
        },
        {
            pokemon_list: ["incineroar", "togekiss", "rillaboom", "indeedee-F", "cinderace", "urshifu"],
            rating: 1430,
            replay_upload_date: 12-10-19
        },
        {
            ...
        }
    }
}
```

## `GET /api/usage/{format}/{date}`

Get most recent recorded individual Pokémon usage for specific format.
Defaults to recent VGC format if format not provided (eg. `gen8vgc2021`).
Defaults to most recent if date is not given.

### Request

```console
curl /api/usage/gen8vgc2021/2021-12-15
```

### Response

```console
{
    date: 2021-12-15,
    format: gen8vgc2021,
    pokemon_usage: {
        {
            "incineroar": 47.0,
            "rillaboom": 37.0,
            "regieleki": 22.0,
            ...
        },
    }
}
```

## `GET /api/rating-usage/{format}/{date}`

Get most recent recorded Pokémon rating to usage ratio for specific format.
Filter by Pokémon using `-F pokemon[]={pokemon}`.
Defaults to recent VGC format if format not provided (eg. `gen8vgc2021`).
Defaults to most recent if date is not given.

### Request

```console
curl /api/rating-usage/gen8vgc2021/2021-12-15
```

### Response

```console
{
    date: 2021-12-15,
    format: gen8vgc2021,
    rating_usage_ratio: {
        {
            "incineroar": 35.4,
            "rillaboom": 21.3,
            ...
        },
    }
}
```

## `GET /api/core-usage/{date}`

Get most recent recorded Pokémon core combinations of 3. Exclusive to current VGC format.
Filter by Pokémon using `-F pokemon[]={pokemon}`.
Defaults to most recent if date is not given.

### Request

```console
curl /api/core-usage/2021-12-15
```

### Response

```console
{
    date: 2021-12-15,
    format: gen8vgc2021,
    core_usage: {
        {
            ["incineroar", "rillaboom", "regieleki"]: 11,
            ["torkoal", "venusaur", "incineroar"]: 8,
            ...
        },
    }
}
```

## `GET /api/partners/{pokemon}/{date}`

Get Pokémon's top 5 partners. Exclusive to current VGC format.
Defaults to most recent if date is not given.

### Request

```console
curl /api/core-usage/2021-12-15
```

### Response

```console
{
    date: 2021-12-15,
    format: gen8vgc2021,
    pokemon: "togekiss",
    partners: {
        {
            incineroar: 27,
            rillaboom: 25,
            whimsicott: 16,
            regieleki: 15,
            amoonguss: 11,
        },
    }
}
```

## `GET /api/timeseries-usage/{format}/{pokemon}`

Get Pokémon's time-series usage to present.

### Request

```console
curl /api/timeseries-usage/gen8vgc2021/incineroar
```

### Response

```console
{
    format: gen8vgc2021,
    pokemon: togekiss,
    time-usage: {
        "2021-12-15": 25,
        "2021-12-14": 21,
        "2021-12-13": 23,
        "2021-12-12": 13,
        ...
    }
}
```
