
# Genetec SecurityCenter Python wrapper

**Still in developpement !**
## Getting Started

I have a problem with ``requests.Session()`` who doesn't use correctly the cookies.

Before use, please logon on the web server and retrieve cookies (``webclient`` and ``XSRF-TOKEN``) from your browsers and set the variables ``xsrfCookie`` and ``webclientCookie``

If needed, set ``partitions`` variable (can be found in your browser network requests)

For now, only basic functions for managing access control are available.

## Example

Create a card holder
```python
addCardHolder("John","DOE")
```

Assign unused card to card holder
```python
user = searchCardHolder(FullName="John DOE")
unassignedCard = getCardUnassigned()[0]
setCard(user,unassignedCard)
```
Create users from CSV and assign cards
```python
    # CSV format : firstname;lastname;groupName;cardNumber
    with open(file, "r",encoding='utf-8') as csvfile:
        csvreader = csv.reader(csvfile,delimiter=';')

        # This skips the first row of the CSV file.
        next(csvreader)

        for row in csvreader:
            firstname = row[0]
            lastname = row[1]
            groupName = row[2]
            cardNumber = row[3]
            createUser(firstname,lastname,groupName,cardNumber)
```

## Todo

 - [ ] Automatically use cookies with a ``login()`` function
 - [ ] Create function ``getPartitions()``
