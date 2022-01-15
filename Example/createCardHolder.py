from GenectecSecurityCenter import GenectecSecurityCenter

# This is an example, edit with your own cookies
cookies = {
    'webclient': '%7b%22Id%22%3a%224855ced0-rec4-4e93-b2b9-97ebada3bdff%22%2c%22Token%22%3a%22eyJhbGciOiJLosdzXoereJndfeTY0MjNBREMzQ0I2NjUiLCJ4NXQiOiJtYjg1d1dMU1NsTmZBdzFqbnhaQ090dzh0bVUiLCJ0eXAiOiJKV1QifQ.eyJodHRwOi8vZ2VuZXRlYy5jb20vQ2xhaW1zL05hbWUiOiJjb3VydG9pcyIsImh0dHA6Ly9nZW5ldGVjLmNvbS9DbGFpbXMvVXNlcklkIjoiMWI5MjA3YTFjNWJkNDc3MTlmZTNkNTJmOGVhOTgxZDIiLCJodHRwOi8vZ2VuZXRlYy5jb20vQ2xhaW1zL0lzQWRtaW4iOjEsImh0dHA6Ly9nZW5ldGVjLmNvbS9DbGFpbXMvUHJpdiI6WyIwOGQ5ZmNiYS1lY2FkLTRiNzUtYjdlMy05YWNiOGIyN2JhNGIiLCIxYjAzYzg5ZS0wYjAyLTRkNjgtYjI4MS1lZjVhNGY3NjE0NmMiLCI0OGQ5ZTIyNy1iZjZiLTQzZGMtOWQ4Ny1hOTc5ZWZmNTg0ZDMiLCI0YzFkOTExZi1iMTIzLTQ0ZmItOGEzNy00ODdiODUzMmZjMTQiLCI1ODVhNDY4Mi02YzVhLTRlZWQtYjFjOC1lZWM0ZGNlNGJiN2IiLCI2ZmIyMGQ3Yy00MTUzLTRkOTYtODBkYi01M2I2MzIyY2NmYzkiLCI3NzA2NGY2Mi01ZWNjLTQ5MTYtYjZhMS1iNjc4NDljZjM0MjEiLCI3ZjNiOTM1Zi0zZTUwLTQ3MjItYjc4Yi0wNmUxNzQ2NDA2Y2MiLCI4MzU1YzQ4OC1mYTdkLTQzZDMtOGY0ZS0zNDRjY2VmNjQ5OGQiLCI4NTA3YmMyYy1lZWU5LTQ1ZjEtYTRjNi1hZDU3Y2U5NmFhMjgiLCI5YmYwMjlmNC01NDAyLTQ1YmUtYjI4My05ZmM1Y2Q1ZGE3Y2IiLCJhMjFhNWMyMy1kMjE0LTQyMGQtYTNkOS1iMTQ2ZjJiNGU1ODkiLCJhNzFlOGNiNS1hZjZiLTQ4MWYtYjI4NS03MmFmYTE4NjVmOTMiLCJiMDQ2YzFhOC0yYmVhLTRiYjEtODUwMi1iMjRiMzI0ODE1YjIiLCJjMTUxNGE4ZS1hODIwLTRkNGItYTUxZi1lNWM1ODAyY2E1OGIiLCJjNWQzZjYzNy1lOWYwLTRiZTYtYTEwMi03OTQ1ZmRhZTQ4NzIiLCJjODZiYzQ5Yy0xYWI4LTRiZjUtYmIxNy01NTZhMTkyNTMyMzIiLCJkNzJmNjk5NS01NDhjLTRjMzgtYTRmYS0wZmRkZDJhNzY3NGQiLCJkYjYwYTk0YS0xNTdlLTRlMTYtYjc2Ni1mMGY2NjE3YjYxMDYiLCJkYzBjMDk4My1jNzM3LTRhYTctYmExZS03OThjNDAxMGM0ZTUiLCJlMDZlY2Y1OC1iZmNlLTQyYzYtODkwYS1jNDc2MTE1OGJkMjAiLCJlNjIwNmI2MC0yM2U4LTQ0NjYtODQ5My0xNDE4ZjA4OGU3YTkiXSwibmJmIjoxNjQyMjA0Mzg5LCJleHAiOjE2NDIyNDc1ODksImlhdCI6MTY0MjIwNDM4OSwiaXNzIjoiR2VuZXRlY1N0czovLzJkMDQ5NzNjMzFiMjQ4OTY4NTcwOGI3YzNjMTFjNzYwIiwiYXVkIjoiZ2VuZXRlYzovL1dlYlRva2VuIn0.XlEeQvwr4lGbP8EySBFzJ0RGBtUODWkWvWKJPNFB1ZjlM3bZy7KUadpaWb_UpTj3rwMnwmPEqD-yw-9S3H6h08tUYwhFbY2JCWnRr7RLCiSEp0Ro_7Tnoe-re0l6jUuXbhueTqpLWTIISgMnzew-XAv2Sjkhi5Z_zCfKND1FsM0IKwh1n4PszbaBsfABImrrscWQ9OT3AvQMVuqH4n5EZaiSSmKljm46buUSWjjb280iIwa9zm73Ll3S8Ht_SuXfKyBdK7xJVBAZ1C3ctjF3IkiIyizl7akMJunKZMcmXePeFF2m_wROmoiDw5r5SSEcOL8CJ1WuRVmtSkeYDh-6Iw%22%2c%22ApplicationId%22%3a%2200000000-0000-0000-0000-000000000000%22%2c%22ValidUntil%22%3a%222022-01-15T11%3a53%3a09.4826082Z%22%2c%22MillisecondsValid%22%3a43200000%7d',
    'XSRF-TOKEN': 'mGugukcg0gT4iaMgGJBDC5uJirfJuV8eqOr4kYM8tC4%3dyRip7yygrdBpWwf%2fiLf5WhVG%2bRo6TjRfGZfOqqcumeE%3d'
}

Gsc = GenectecSecurityCenter("192.168.1.100", cookies=cookies, verifySsl=False)
firstName = "John"
lastName = "DOE"
fullName = "{} {}".format(firstName, lastName)
# Set  this with your own value (can be found in network)
partition = {'00000000-0000-0000-0000-00000000000b': 'SRV-GENETEC'}
search = Gsc.searchCardHolder(FullName=fullName)

if not search:
    # Card holder don't exist
    # Search for an unassigned card
    card = Gsc.getCardUnassigned()[0]

    # Create user
    create = Gsc.addCardHolder(
        firstName=firstName,
        lastName=lastName,
        name=fullName,
        credentials={card['id']: card['name']},
        partitions=partition
    )

    print(create)

else:
    print("{} already exist".format(fullName))
