# Requirements

Create a new `.env` file in the directory and add the required env variables like `SECRET_KEY` and `DEBUG`

# How to run

use
```
docker-compose up
```
and navigate to `localhost:8000` to access the application

# Endpoints

| Endpoint | Request Type | Args | Return |
| -------- | -------------| ---- | ------ |
| auth/users | POST | -email -username -password | HTTPS 200 |
| auth/jwt/ceate | POST | - username - password | - Access Token - Refresh Token |
| app/book | GET | | List of books available |
| app/book/ | POST | -title -amazon_url -genre -author | Book detail |
| app/reader/ | GET | | List of user's fav books |
| app/reader/ | POST | List of user's fav books | List of user's fav books |
| app/reader/ | PUT | List of user's new fav books | List of user's new fav books |
| app/reader/<pk> | PATCH | Book to be added to user's list of fav books | The book added to user's list of fav books |
| app/reader/<pk> | DELETE | Book to be delted from user's list of fav books | List of user's fav books |

For more endpoints realted to user or authentication refer to [djoser doc](https://djoser.readthedocs.io/en/latest/base_endpoints.html) <br>

Remember to pass the JWT toke in format `Authorization: JWT [TOKEN]` where Authorization is the header key

[![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/c62fe54950d842134d28)