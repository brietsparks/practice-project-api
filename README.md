Install
`docker-compose -f docker/dev/docker-compose.yml build`

Run
`docker-compose -f docker/dev/docker-compose.yml up`

Migrations from scratch
`flask db init`
`flask db migrate`

Upgrading migrations
`flask db upgrade`