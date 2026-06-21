# SAPI

Simple API tester, made with love by sadonat. All you need to do is create a collection file once, and run the command

## Features

- Testing single endpoint
- Testing multiple endpoints

## How to Install

## How to Use

Before anything else, you need to create a collection file. don't worry, i use yaml format so its readable and easy to master.

```yaml
base_url: https://jsonplaceholder.typicode.com
endpoints:
  example_get:
    path: /posts/1
    method: GET
  example_post:
    path: /posts
    method: POST
    headers:
      Content-Type: application/json
    json:
      id: 1
      title: Example title
      body: Example body
      userId: 1
```

You just need to define your base_url and create endpoints. To create an endpoint you can fill up this key inside the endpoints key. Remember! indentation is important in yaml.

- path: the path of destination url
- method: the method of the request
- params: query params in url
- headers: header for the request. fill anything you need in your header. in the example i just use Content-Type
- json: the request data in json format that needed to do request

SAPI is a cli tool, you need to enter the command to run it. theres the command:

### 1. sapi test [endpoint name] -f [collection file]

this command will test one endpoint. [endpoint name] is just a key you define in `endpoints` inside your collection file. based on my example, we can use _example_get_ and _example_post_. `-f [collection file]` is optional, you can use this if you want to use custom coection file name. if not it will just use sapilection.yaml in your current directory if exist.

### 2. sapi multitest
this will test all endpoints inside your collection file and then generate the report as `sapireport.md`. same as `sapi test` theres an optional `-f [collection file]`.
