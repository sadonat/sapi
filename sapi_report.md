# TESTING REPORT FOR https://jsonplaceholder.typicode.com

## [GET] /posts/3
time:  1221.65ms
Request body:
```json
None
```
Response:
```json
{'userId': 1, 'id': 3, 'title': 'ea molestias quasi exercitationem repellat qui ipsa sit aut', 'body': 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut'}
```

## [POST] /posts
time:  1178.62ms
Request body:
```json
b'{"id": 1, "title": "Uang itu tidak berguna", "body": "Tapi booonh yahahaha", "userId": 1}'
```
Response:
```json
{'id': 101, 'title': 'Uang itu tidak berguna', 'body': 'Tapi booonh yahahaha', 'userId': 1}
```
