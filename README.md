Migrations from scratch
`flask db init -d ./src/migrations`
`flask db migrate -d ./src/migrations`

Upgrading migrations
`flask db upgrade -d ./src/migrations`