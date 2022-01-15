from datetime import datetime
import requests
from urllib.parse import unquote


class GenectecSecurityCenter():

    def __init__(self, hostname: str, cookies: dict, verifySsl=True):
        """[summary]

        Args:
            hostname (str): Hostname of the web server
            cookies (dict): Cookies
            verifySsl (bool, optional): [description]. Defaults to True.
        """
        self.hostname = hostname
        self.cookies = cookies
        self.baseUrl = "https://{}/securitycenter".format(hostname)
        self.verifySsl = verifySsl

        headers = {
            'Host': self.hostname,
            'Accept': 'application/json, text/plain, */*',
            'Content-Type': 'application/json;charset=utf-8',
            'X-XSRF-TOKEN': unquote(self.cookies['XSRF-TOKEN']),
            'Cookie': 'webclient={};XSRF-TOKEN={}'.format(self.cookies['webclient'], self.cookies['XSRF-TOKEN'])
        }

        # Create session for API calls with default
        # headers and SSL verification
        self.session = requests.Session()
        self.session.headers.update(headers)
        self.session.verify = self.verifySsl

    # Card management
    def getCardUnassigned(self, Assigned=False, FederatedState=2, Name='', Page=1, PageSize=25):
        """Return all unassigned cards

        Args:
            Assigned (bool, optional): [description]. Defaults to False.
            FederatedState (int, optional): [description]. Defaults to 2.
            Name (str, optional): [description]. Defaults to ''.
            Page (int, optional): [description]. Defaults to 1.
            PageSize (int, optional): [description]. Defaults to 25.

        Returns:
            [type]: [description]
        """
        url = self.baseUrl + '/Credentials/Entities'
        query = {
            "Assigned": Assigned,
            "FederatedState": FederatedState,
            "Name": Name,
            "Page": Page,
            "PageSize": PageSize
        }

        response = self.session.get(url=url, params=query)

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def getCards(self, Name='', NameOrder=0, Page=1, Pagesize=25):
        """ Search for cards

        Args:
            Name (str, optional): [description]. Defaults to ''.
            NameOrder (int, optional): [description]. Defaults to 0.
            Page (int, optional): [description]. Defaults to 1.
            Pagesize (int, optional): [description]. Defaults to 25.

        Returns:
            [type]: [description]
        """

        url = self.baseUrl + '/Credentials'
        query = {
            "Name": Name,
            "NameOrder": NameOrder,
            "Page": Page,
            "Pagesize": Pagesize
        }

        response = self.session.get(url, params=query)

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    # Card holder management
    def getCardHolder(self, guid: str):
        """[summary]

        Args:
            guid (str): guid of the card holder

        Returns:
            [type]: [description]
        """

        url = self.baseUrl + '/Cardholders/{}'.format(guid)
        response = self.session.get(url)

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def deleteCardHolder(self, guid: str):
        """Delete a card holder

        Args:
            guid (str): guid of the card holder

        Returns:
            [type]: [description]
        """

        url = "{}/Cardholders/{}".format(self.baseUrl, guid)
        response = self.session.delete(url)

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def searchCardHolder(
            self,
            FullName='',
            IncludeAccessRules=False,
            IncludeCardholderGroups=True,
            IncludeCredentials=True,
            IncludePartitions=False,
            LastNameOrder=0,
            MobilePhoneNumber='',
            NameOrder=0,
            Page=1,
            Pagesize=25,
            FirstNameOrder=0
            ):
        """Search for card holder

        Args:
            FullName (str, optional): [description]. Defaults to ''.
            IncludeAccessRules (bool, optional): [description]. Defaults to False.
            IncludeCardholderGroups (bool, optional): [description]. Defaults to True.
            IncludeCredentials (bool, optional): [description]. Defaults to True.
            IncludePartitions (bool, optional): [description]. Defaults to False.
            LastNameOrder (int, optional): [description]. Defaults to 0.
            MobilePhoneNumber (str, optional): [description]. Defaults to ''.
            NameOrder (int, optional): [description]. Defaults to 0.
            Page (int, optional): [description]. Defaults to 1.
            Pagesize (int, optional): [description]. Defaults to 25.
            FirstNameOrder (int, optional): [description]. Defaults to 0.

        Returns:
            [type]: [description]
        """

        url = self.baseUrl + '/Cardholders'
        query = {
            'FullName': FullName,
            'IncludeAccessRules': IncludeAccessRules,
            'IncludeCardholderGroups': IncludeCardholderGroups,
            'IncludeCredentials': IncludeCredentials,
            'IncludePartitions': IncludePartitions,
            'LastNameOrder': LastNameOrder,
            'MobilePhoneNumber': MobilePhoneNumber,
            'NameOrder': NameOrder,
            'Page': Page,
            'Pagesize': Pagesize,
            'FirstNameOrder': FirstNameOrder
        }
        response = self.session.get(url, params=query)

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def setCardHolderCard(self, cardHolder: dict, card: dict):
        """Assign card to a card holder

        Args:
            cardHolder (dict): [description]
            card (dict): [description]

        Returns:
            [type]: [description]
        """

        url = '{}/Cardholders/{}'.format(self.baseUrl, cardHolder['id'])
        cardHolder['credentials'] = {card['id']: card['name']}
        response = self.session.put(url, json=cardHolder)

        if response.status_code == 200:
            return response.json
        else:
            return response.status_code

    # Card holder group management
    def searchGroups(self, Name='', FederatedState=2, Page=1, PageSize=25):
        """Search card holder groups

        Args:
            Name (str, optional): [description]. Defaults to ''.
            FederatedState (int, optional): [description]. Defaults to 2.
            Page (int, optional): [description]. Defaults to 1.
            PageSize (int, optional): [description]. Defaults to 25.

        Returns:
            [type]: [description]
        """

        url = '{}/CardholderGroups/Entities'.format(self.baseUrl)
        query = {
            Name: Name,
            FederatedState: FederatedState,
            Page: Page,
            PageSize: PageSize
        }
        response = self.session.get(url, params=query)

        if response.status_code == 200:
            return response.json()
        else:
            return response.status_code

    def addCardHolder(
        self,
        firstName: str,
        lastName: str,
        partitions: dict,
        photo='',
        emailAddress='',
        cardholderGroups={},
        useExtendedGrantTime=False,
        canEscort=False,
        antipassbackExemption=False,
        credentials={},
        customFields=[],
        accessRules={},
        accessPermissionLevel=7,
        description='',
        name='',
        inheritAccessPermissionLevelFromGroup=True,
        antipassbackExemptionIsInherited=True,
        privileges=[],
        expirationDate=None,
        expirationDuration=1,
        activationDate=datetime.utcnow().isoformat()[:-3] + 'Z',
        entityType=7,
        accessStatus=1,
        activationMode=0,
        expirationMode=1
    ):
        """Create a card holder

        Args:
            firstName (str): [description]
            lastName (str): [description]
            photo (str, optional): [description]. Defaults to ''.
            emailAddress (str, optional): [description]. Defaults to ''.
            cardholderGroups (dict, optional): [description]. Defaults to {}.
            useExtendedGrantTime (bool, optional): [description]. Defaults to False.
            canEscort (bool, optional): [description]. Defaults to False.
            antipassbackExemption (bool, optional): [description]. Defaults to False.
            credentials (dict, optional): [description]. Defaults to {}.
            customFields (list, optional): [description]. Defaults to [].
            accessRules (dict, optional): [description]. Defaults to {}.
            accessPermissionLevel (int, optional): [description]. Defaults to 7.
            partitions (dict, optional): [description]. Defaults to {}.
            description (str, optional): [description]. Defaults to ''.
            name (str, optional): [description]. Defaults to ''.
            inheritAccessPermissionLevelFromGroup (bool, optional): [description]. Defaults to True.
            antipassbackExemptionIsInherited (bool, optional): [description]. Defaults to True.
            privileges (list, optional): [description]. Defaults to [].
            expirationDate ([type], optional): [description]. Defaults to None.
            expirationDuration (int, optional): [description]. Defaults to 1.
            activationDate ([type], optional): [description]. Defaults to datetime.utcnow().isoformat()[:-3]+'Z'.
            entityType (int, optional): [description]. Defaults to 7.
            accessStatus (int, optional): [description]. Defaults to 1.
            activationMode (int, optional): [description]. Defaults to 0.
            expirationMode (int, optional): [description]. Defaults to 1.

        Returns:
            [type]: [description]
        """
        url = '{}/Cardholders'.format(self.baseUrl)
        payload = {
            "firstName": firstName,
            "lastName": lastName,
            "photo": photo,
            "emailAddress": emailAddress,
            "cardholderGroups": cardholderGroups,
            "useExtendedGrantTime": useExtendedGrantTime,
            "canEscort": canEscort,
            "antipassbackExemption": antipassbackExemption,
            "credentials": credentials,
            "customFields": customFields,
            "accessRules": accessRules,
            "accessPermissionLevel": accessPermissionLevel,
            "partitions": partitions,
            "description": description,
            "name": name,
            "inheritAccessPermissionLevelFromGroup": inheritAccessPermissionLevelFromGroup,
            "antipassbackExemptionIsInherited": antipassbackExemptionIsInherited,
            "privileges": privileges,
            "expirationDate": expirationDate,
            "expirationDuration": expirationDuration,
            "activationDate": activationDate,
            "entityType": entityType,
            "accessStatus": accessStatus,
            "activationMode": activationMode,
            "expirationMode": expirationMode
        }

        response = self.session.post(url, json=payload)

        if response.status_code == 200:
            return response.json()
        else:
            return response.text
