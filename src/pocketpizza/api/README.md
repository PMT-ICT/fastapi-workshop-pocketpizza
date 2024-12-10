# Exercise 1

## Exercise 1.1
For this assignment we'll need the Order Repository to retrieve orders from the database. The order repository has been implemented for you in pocketpizza/repositories/order.py We'll need to turn this into a FastAPI Dependency, which we can then receive in the path operation parameters.

HINT: Use `Annotated` from the Python `typing` library and the `Depends` function from the `fastapi` module.

## Exercise 1.2
Implement GET /order. We'll need one optional query parameter: user_id, which must be an integer. If given, we want to return only the orders for that user.

## Exercise 1.3
Implement GET /order/{order_id}. We'll need one path parameter {order_id}, which must be an integer.

We'll need the order repository dependency you made in 1.1 for this assignment.

If no order is found for the given order_id, the endpoint should return a 404 NOT FOUND.

## Exercise 1.4
Implement POST /order. We'll need a request body CreateOrder, which you can find in the pocketpizza.schemas module, and the order repository. Return the created order.

# Exercise 2
Before continuing, uncomment the line in `main.py` that says:

```py
# app.include_router(user.router)
```

This will add the login endpoint to your application. Refresh Swagger UI to see it. You'll see the request body has various fields, but only two are required: `username` and `password`. You can ignore the other fields for this exercise.

## Exercise 2.1

Try to log in using the login endpoint! Your username is `{firstname}@pocketpizza.com`, so for example: `nathaniel@pocketpizza.com`. The password is `swordfish`.

The response body should be a JSON object containing the bearer token you'll need to send along with your API requests.

## Exercise 2.2

Next we'll start implementing authentication for our endpoints. We'll revisit all of the order endpoints we made in Exercise 1 and include user authentication.

To do so, you need to import the `CurrentUser` dependency from `pocketpizza.dependencies.user` and add it to the parameters in your path operations (the functions you created for your endpoints). Try it with the root `/order` endpoint: replace the `user_id` parameter with a `current_user` parameter (use the dependency).

**Note**: since youre removing the `user_id` parameter, you'll have to get the user ID from the current user to make the code work again.

Refresh the Swagger UI once you've made the changes and the application has restarted. You should see an "Authorize" button appear in the top right of the Swagger UI. Click it, and you can authorize for all API calls the same way you logged in with the login endpoint.

## Exercise 2.3

Implement authentication for `GET /order/{order_id}` and `POST /order` as well, replacing user ids in the parameters and request bodies where necessary.

# Bonus Exercise

Create a new module `pizza` in the `pocketpizza.api` module, with a new router for pizza endpoints.

Implement the following endpoints for pizzas:

* `GET /pizza`
* `GET /pizza/{pizza_id}`
* `POST /pizza`
* `PUT /pizza/{pizza_id}`

Any authenticated user can use the `GET` endpoints, but only the superuser is allowed to create, edit and delete pizzas. See if you can implement authorisation for those three endpoints. 

Credentials for the superuser account are: 

* username: `superuser@pocketpizza.com`
* password: `opensesame`

**HINT**: Take a look at the `SuperUser` dependency in `pocketpizza.dependencies.user`.
