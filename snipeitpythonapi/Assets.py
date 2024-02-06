import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context
import requests
try:
    requests.packages.urllib3.disable_warnings()
except AttributeError:
    pass
else:
    requests.packages.urllib3.disable_warnings()
try:
    from .packages.urllib3.exceptions import ResponseError
except:
    pass

import json


class Assets(object):
    def __init__(self):
        pass

    def createBaseGetRequest(self, server, base_uri, token, limit=None, offset=None):
        uri = base_uri
        if limit is not None:
            uri = base_uri + '&limit={0}'.format(str(limit))
        if offset is not None:
            uri = base_uri + '&offset={0}'.format(str(offset))

        self.server = server + uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def get(self, server: str, token: str, limit: str = None, order: str ='asc', offset: str = None):
        """Get list of assets

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            offset {string} -- Starting offset to get the data

        Keyword Arguments:
            limit {string} -- Limit the number of data returned by the server (default: {50})
            order {string} -- Display order of data (asc / desc default:{asc})

        Returns:
            [string] -- List of assets from the server, in JSON format
        """
        uri = '/api/v1/hardware?order={0}'.format(order)
        return self.createBaseGetRequest(server, uri, token, limit, offset)

    def search(self, server: str, token: str, limit: str = None, order: str = 'asc', keyword: str = None, offset: str = None):
        if keyword is None:
            keyword = ''

        uri = '/api/v1/hardware?order={0}'.format(order)
        uri = uri + '&search=' + str(keyword)

        return self.createBaseGetRequest(server, uri, token, limit, offset)

    def getAssetsByModel(self, server: str, token: str, modelID: str, limit: str = None, order: str ='asc', offset: str = None):
        uri = '/api/v1/hardware?order={0}'.format(order)
        uri = uri + '&model_id=' + str(modelID)
        return self.createBaseGetRequest(server, uri, token, limit, offset)

    def getAssetsByCategory(self, server: str, token: str, categoryID: str, limit: str = None, order: str = 'asc', offset: str = None):
        uri = '/api/v1/hardware?order={0}'.format(order)
        uri = uri + '&category_id=' + str(categoryID)
        return self.createBaseGetRequest(server, uri, token, limit, offset)

    def getAssetsByManufacturer(self, server: str, token: str, manufacturerID: str, limit: str = None, order: str = 'asc', offset: str = None):
        uri = '/api/v1/hardware?order={0}'.format(order)
        uri = uri + '&manufacturer_id={0}'.format(manufacturerID)
        return self.createBaseGetRequest(server, uri, token, limit, offset)

    def getAssetsByCompany(self, server: str, token: str, companyID: str, limit: str = None, order: str = 'asc', offset: str = None):
        uri = '/api/v1/hardware?order={0}'.format(order)
        uri = uri + '&company_id={0}'.format(companyID)
        return self.createBaseGetRequest(server, uri, token, limit, offset)

    def getAssetsByLocation(self, server: str, token: str, locationID: str, limit: str = None, order: str = 'asc', offset: str = None):
        uri = '/api/v1/hardware?order={0}'.format(order)
        uri = uri + '&location_id={0}'.format(locationID)
        return self.createBaseGetRequest(server, uri, token, limit, offset)

    def getAssetsByStatus(self, server: str, token: str, status: str, limit: str = None, order: str = 'asc', offset: str = None):
        """Get list of assets with the given status

        Arguments:
            status {string} -- Status types (RTD, Deployed, Undeployable, Deleted, Archived, Requestable)
        """
        uri = '/api/v1/hardware?order={0}'.format(order)
        uri = uri + '&status={0}'.format(status)
        return self.createBaseGetRequest(server, uri, token, limit, offset)

    def getAssetsByStatusLabel(self, server: str, token: str, statusLabelID: str, limit: str = None, order: str = 'asc', offset: str = None):
        uri = '/api/v1/hardware?order={0}'.format(order)
        uri = uri + '&status_id={0}'.format(statusLabelID)
        return self.createBaseGetRequest(server, uri, token, limit, offset)

    def getDetailsByID(self, server, token, AssetID):
        """Get asset details by ID

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            AssetID {string} -- Asset ID

        Returns:
            [string] -- Asset details from the server, in JSON formatted
        """
        self.uri = '/api/v1/hardware/{0}'.format(str(AssetID))
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getDetailsByTag(self, server, token, AssetTag):
        """Get asset details by ID

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            AssetTAG {string} -- Asset TAG

        Returns:
            [string] -- Asset details from the server, in JSON formatted
        """
        self.uri = '/api/v1/hardware/bytag/{0}'.format(str(AssetTag))
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getDetailsBySerial(self, server, token, AssetSerial):
        """Get asset details by Serial Number

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            AssetSerial {string} -- Asset Serial Number

        Returns:
            [string] -- List of assets from the server, in JSON formatted
        """
        self.uri = '/api/v1/hardware/byserial/{0}'.format(str(AssetSerial))
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def create(self, server, token, payload):
        """Create new asset data

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            payload {string} -- Asset data

        Returns:
            [string] -- Server response in JSON formatted
        """
        self.uri = '/api/v1/hardware'
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(), indent=4, separators=(',', ':'))

    def getID(self, server, token, asset_name):
        """search asset ID by its name

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            asset_name {string} -- Asset name

        Returns:
            [string] -- Server response in JSON formatted
        """
        self.uri = '/api/v1/hardware?search={0}'.format(asset_name)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        jsonData = json.loads(
            (results.content).decode('utf-8').replace("'", '"'))
        # print(jsonData)
        if len(jsonData['rows']) < 2 and jsonData['rows'][0]['id'] is not None:
            AssetID = jsonData['rows'][0]['id']
        return AssetID

    def delete(self, server, token, DeviceID):
        """Delete asset data

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            DeviceID {string} -- Asset ID to be deleted

        Returns:
            [string] -- Server response in JSON formatted
        """
        self.uri = '/api/v1/hardware/{0}'.format(DeviceID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(token)}
        results = requests.delete(self.server, headers=headers)
        jsonData = json.loads(results.content)
        return jsonData['status']

    def updateDevice(self, server, token, DeviceID, payload):
        """Update asset data

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            DeviceID {string} -- Asset ID
            payload {string} -- Asset data

        Returns:
            [string] -- Server response in JSON formatted
        """
        self.uri = '/api/v1/hardware/{0}'.format(DeviceID)
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(token)}
        results = requests.patch(self.server, headers=headers, data=payload)
        jsonData = json.loads(results.content)
        return jsonData['status']

    def checkInAsset(self, server, token, assetID, note=None, locationID=None):
        """Check in an asset

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            assetID {string} -- ID of the asset

        Keyword Arguments:
            note {string} -- Note of the checkin (default: {None})
            locationID {string} -- Location id where the asset checked in (default: {None})
        """
        self.uri = ('/api/v1/hardware/{0}/checkin'.format(assetID))
        payload = {'note': note, 'location_id': locationID}
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(), indent=4, separators=(',', ':'))

    def checkOutAsset(self, server, token, assetID, note=None, locationID=None):
        """Check out an asset

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
            assetID {string} -- ID of the asset

        Keyword Arguments:
            note {string} -- Note of the checkin (default: {None})
            locationID {string} -- Location id where the asset checked out (default: {None})
        """
        self.uri = ('/api/v1/hardware/{0}/checkout'.format(assetID))
        payload = {'note': note, 'location_id': locationID}
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(), indent=4, separators=(',', ':'))

    def auditAsset(self, server, token, assetTag=None, locationID=None):
        """Audit an asset

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API

        Keyword Arguments:
            assetTag {string} -- asset tag to be audited (default: {None})
            locationID {[type]} -- location ID to be audited (default: {None})
        """
        self.uri = '/api/v1/hardware/audit'
        payload = {'asset_tag': assetTag, 'location_id': locationID}
        self.server = server + self.uri
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'Bearer {0}'.format(token)}
        results = requests.post(self.server, headers=headers, data=payload)
        return json.dumps(results.json(), indent=4, separators=(',', ':'))

    def getAuditDue(self, server, token):
        """Gets list of audit dues

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        """
        self.uri = '/api/v1/hardware/audit/due'
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content

    def getAuditOverdue(self, server, token):
        """Gets list of audit overdues

        Arguments:
            server {string} -- Server URI
            token {string} -- Token value to be used for accessing the API
        """
        self.uri = '/api/v1/hardware/audit/overdue'
        self.server = server + self.uri
        headers = {'Authorization': 'Bearer {0}'.format(token)}
        results = requests.get(self.server, headers=headers)
        return results.content
