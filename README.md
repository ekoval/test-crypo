# Cryptocurrencies portfolio sample app.


## How to Use


### Build and run Docker container:

```
docker-compose build
docker-compose up
```

### Authenticate

```
GET http://0.0.0.0:8000/auth/?username=<any_username>
```

This returns you an auth token you have to pass with every further request:

#### Create/update portfolio for current user:
```
POST /portfolio/?jwt=<token> {"btc": 10, "eth": 20}
```

#### Get portfolio for current user:
```
GET /portfolio/?jwt=<token>
```

#### Get your portfolio YTD statistics:
```
GET /ytd-statistics/?jwt=<token>
```

#### Wipe database

```
POST /clear/?jwt=<token>
```

(you must authenticate as `admin` to do this.
