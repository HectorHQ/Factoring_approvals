import pandas as pd
import requests
import json
import streamlit as st
from openpyxl import load_workbook


st.set_page_config("Factoring Order Requests",page_icon=':heavy_dollar_sign:',layout="wide",initial_sidebar_state='expanded')
st.title(':blue[Factoring] Orders :heavy_dollar_sign:')




bearer_token = str(st.text_input("Insert Bearer Token"))


headers = {
    'authority': 'api.getnabis.com',
    'accept': '*/*',
    'accept-language': 'es-ES,es;q=0.9',
    'authorization': bearer_token,
    # 'content-type': 'application/json',
    'origin': 'https://app.getnabis.com',
    'referer': 'https://app.getnabis.com/',
    'sec-ch-ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36',
}



# Requested
def Factored_Requested(headers,order_number):
    json_data = {
        'operationName': 'GetAdminFactoredInvoices',
        'variables': {
            'pageInfo': {
                'numItemsPerPage': 50,
                'orderBy': [
                    {
                        'attribute': 'date',
                        'order': 'DESC',
                    },
                    {
                        'attribute': 'createdAt',
                        'order': 'DESC',
                    },
                ],
                'page': 1,
            },
            'organizationId': None,
            'factorStatus': 'REQUESTED',
            'search': order_number,
            'start': None,
            'end': None,
        },
        'query': 'query GetAdminFactoredInvoices($organizationId: ID, $orderBy: String, $direction: String, $factorStatus: OrderFactorStatusEnum, $isAdvancePaid: Boolean, $isReservePaid: Boolean, $paymentStatus: [OrderPaymentStatusEnum], $search: String, $start: DateTime, $end: DateTime, $pageInfo: PageInfoInput) {\n  getAdminFactoredInvoices(organizationId: $organizationId, orderBy: $orderBy, direction: $direction, factorStatus: $factorStatus, isAdvancePaid: $isAdvancePaid, isReservePaid: $isReservePaid, paymentStatus: $paymentStatus, search: $search, start: $start, end: $end, pageInfo: $pageInfo) {\n    results {\n      ...factorFragment\n      creator {\n        ...userFragment\n        __typename\n      }\n      licensedLocation {\n        ...licensedLocationFragment\n        __typename\n      }\n      organization {\n        ...organizationFragment\n        __typename\n      }\n      site {\n        ...siteFragment\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      ...pageInfoFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment factorFragment on FactorInvoice {\n  id\n  advanceAmount\n  createdAt\n  creditMemo\n  date\n  daysTillPaymentDue\n  discount\n  distroFees\n  dueToBrand\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  factorStartDate\n  factorStatus\n  gmv\n  gmvCollected\n  invoicesS3FileLink\n  irn\n  isAdvancePaid\n  isReservePaid\n  manifestGDriveFileId\n  mustPayPreviousBalance\n  nabisDiscount\n  nabisDistroFees\n  name\n  netGmv\n  number\n  paidAt\n  paymentMethod\n  paymentStatus\n  paymentDueDate\n  pricingFee\n  pricingPercentage\n  remittedAt\n  reserveAmount\n  status\n  surcharge\n  totalFactorFee\n  totalFees\n  accountingNotes\n  __typename\n}\n\nfragment userFragment on User {\n  id\n  email\n  firstName\n  lastName\n  address1\n  address2\n  city\n  state\n  zip\n  phone\n  profilePicture\n  isAdmin\n  isDriver\n  driversLicense\n  __typename\n}\n\nfragment licensedLocationFragment on LicensedLocation {\n  id\n  name\n  address1\n  address2\n  city\n  state\n  zip\n  siteCategory\n  lat\n  lng\n  billingAddress1\n  billingAddress2\n  billingAddressCity\n  billingAddressState\n  billingAddressZip\n  warehouseId\n  isArchived\n  doingBusinessAs\n  noExciseTax\n  phoneNumber\n  printCoas\n  hoursBusiness\n  hoursDelivery\n  deliveryByApptOnly\n  specialProtocol\n  schedulingSoftwareRequired\n  schedulingSoftwareLink\n  centralizedPurchasingNotes\n  payByCheck\n  collectionNotes\n  deliveryNotes\n  collect1PocFirstName\n  collect1PocLastName\n  collect1PocTitle\n  collect1PocNumber\n  collect1PocEmail\n  collect1PocAllowsText\n  collect1PreferredContactMethod\n  collect2PocFirstName\n  collect2PocLastName\n  collect2PocTitle\n  collect2PocNumber\n  collect2PocEmail\n  collect2PocAllowsText\n  collect2PreferredContactMethod\n  delivery1PocFirstName\n  delivery1PocLastName\n  delivery1PocTitle\n  delivery1PocNumber\n  delivery1PocEmail\n  delivery1PocAllowsText\n  delivery1PreferredContactMethod\n  delivery2PocFirstName\n  delivery2PocLastName\n  delivery2PocTitle\n  delivery2PocNumber\n  delivery2PocEmail\n  delivery2PocAllowsText\n  delivery2PreferredContactMethod\n  unmaskedId\n  qualitativeRating\n  creditRating\n  trustLevelNabis\n  trustLevelInEffect\n  isOnNabisTracker\n  locationNotes\n  infoplus\n  w9Link\n  taxIdentificationNumber\n  sellerPermitLink\n  nabisMaxTerms\n  __typename\n}\n\nfragment organizationFragment on Organization {\n  id\n  address1\n  address2\n  alias\n  city\n  doingBusinessAs\n  factoredStatus\n  hasAnalyticsDashboard\n  hasPlatformV2ApiAccess\n  hasMustPayExternalBalance\n  infoplus\n  isBrand\n  isManufacturer\n  isRetailer\n  isSalesOrg\n  isMarketplace\n  licensedLocationId\n  logoS3Link\n  manifestGDriveFolderId\n  marketplaceContactEmail\n  marketplaceContactName\n  marketplaceContactNumber\n  name\n  phone\n  receiveReports\n  singleHubWarehouseId\n  singleHubWarehouse {\n    ...allWarehousesFragment\n    __typename\n  }\n  state\n  type\n  zip\n  __typename\n}\n\nfragment allWarehousesFragment on Warehouse {\n  ...warehouseFragment\n  site {\n    ...siteFragment\n    licenses {\n      ...licenseFragment\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment warehouseFragment on Warehouse {\n  id\n  isArchived\n  infoplus\n  region\n  isInUseByOps\n  isSingleHub\n  __typename\n}\n\nfragment siteFragment on Site {\n  id\n  name\n  address1\n  address2\n  city\n  state\n  zip\n  pocName\n  pocPhoneNumber\n  pocEmail\n  siteCategory\n  createdAt\n  licensedLocationId\n  __typename\n}\n\nfragment licenseFragment on License {\n  id\n  nickname\n  category\n  type\n  licenseNumber\n  legalEntityName\n  issuanceDate\n  expirationDate\n  contactName\n  contactPhone\n  contactEmail\n  address1\n  address2\n  city\n  state\n  zip\n  archivedAt\n  onboardedAt\n  __typename\n}\n\nfragment pageInfoFragment on PageInfo {\n  totalNumItems\n  totalNumPages\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    return response


# Requested Approved
def Update_factored_Invoices_Approved(headers,invoice_data):
    json_data = {
        'operationName': 'UpdateFactoredInvoices',
        'variables': {
            'input': {
                'changedInvoices': [
                    {
                        'isReservePaid': False,
                        'isAdvancePaid': False,
                        'factorStatus': 'APPROVED',
                        'invoiceId': invoice_data['data']['getAdminFactoredInvoices']['results'][0]['id'],
                        'organizationId': invoice_data['data']['getAdminFactoredInvoices']['results'][0]['organization']['id'],
                    },
                ],
            },
        },
        'query': 'mutation UpdateFactoredInvoices($input: BulkUpdateFactorInvoiceInput!) {\n  bulkUpdateFactoredInvoices(input: $input)\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    return response

# Requested Rejected
def Update_factored_Invoices_Rejected(headers,invoice_data):
    json_data = {
        'operationName': 'UpdateFactoredInvoices',
        'variables': {
            'input': {
                'changedInvoices': [
                    {
                        'isReservePaid': False,
                        'isAdvancePaid': False,
                        'factorStatus': 'REJECTED',
                        'invoiceId': invoice_data['data']['getAdminFactoredInvoices']['results'][0]['id'],
                        'organizationId': invoice_data['data']['getAdminFactoredInvoices']['results'][0]['organization']['id'],
                    },
                ],
            },
        },
        'query': 'mutation UpdateFactoredInvoices($input: BulkUpdateFactorInvoiceInput!) {\n  bulkUpdateFactoredInvoices(input: $input)\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    return response

# Factored Invoices Approved tab to be flipped to Yes Search function
def factored_Approved_tab(headers,order_number):
    json_data = {
        'operationName': 'GetAdminFactoredInvoices',
        'variables': {
            'pageInfo': {
                'numItemsPerPage': 50,
                'orderBy': [
                    {
                        'attribute': 'date',
                        'order': 'DESC',
                    },
                    {
                        'attribute': 'createdAt',
                        'order': 'DESC',
                    },
                ],
                'page': 1,
            },
            'organizationId': None,
            'factorStatus': 'APPROVED',
            'isAdvancePaid': False,
            'search': order_number,
            'start': None,
            'end': None,
        },
        'query': 'query GetAdminFactoredInvoices($organizationId: ID, $orderBy: String, $direction: String, $factorStatus: OrderFactorStatusEnum, $isAdvancePaid: Boolean, $isReservePaid: Boolean, $paymentStatus: [OrderPaymentStatusEnum], $search: String, $start: DateTime, $end: DateTime, $pageInfo: PageInfoInput) {\n  getAdminFactoredInvoices(organizationId: $organizationId, orderBy: $orderBy, direction: $direction, factorStatus: $factorStatus, isAdvancePaid: $isAdvancePaid, isReservePaid: $isReservePaid, paymentStatus: $paymentStatus, search: $search, start: $start, end: $end, pageInfo: $pageInfo) {\n    results {\n      ...factorFragment\n      creator {\n        ...userFragment\n        __typename\n      }\n      licensedLocation {\n        ...licensedLocationFragment\n        __typename\n      }\n      organization {\n        ...organizationFragment\n        __typename\n      }\n      site {\n        ...siteFragment\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      ...pageInfoFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment factorFragment on FactorInvoice {\n  id\n  advanceAmount\n  createdAt\n  creditMemo\n  date\n  daysTillPaymentDue\n  discount\n  distroFees\n  dueToBrand\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  factorStartDate\n  factorStatus\n  gmv\n  gmvCollected\n  invoicesS3FileLink\n  irn\n  isAdvancePaid\n  isReservePaid\n  manifestGDriveFileId\n  mustPayPreviousBalance\n  nabisDiscount\n  nabisDistroFees\n  name\n  netGmv\n  number\n  paidAt\n  paymentMethod\n  paymentStatus\n  paymentDueDate\n  pricingFee\n  pricingPercentage\n  remittedAt\n  reserveAmount\n  status\n  surcharge\n  totalFactorFee\n  totalFees\n  accountingNotes\n  __typename\n}\n\nfragment userFragment on User {\n  id\n  email\n  firstName\n  lastName\n  address1\n  address2\n  city\n  state\n  zip\n  phone\n  profilePicture\n  isAdmin\n  isDriver\n  driversLicense\n  __typename\n}\n\nfragment licensedLocationFragment on LicensedLocation {\n  id\n  name\n  address1\n  address2\n  city\n  state\n  zip\n  siteCategory\n  lat\n  lng\n  billingAddress1\n  billingAddress2\n  billingAddressCity\n  billingAddressState\n  billingAddressZip\n  warehouseId\n  isArchived\n  doingBusinessAs\n  noExciseTax\n  phoneNumber\n  printCoas\n  hoursBusiness\n  hoursDelivery\n  deliveryByApptOnly\n  specialProtocol\n  schedulingSoftwareRequired\n  schedulingSoftwareLink\n  centralizedPurchasingNotes\n  payByCheck\n  collectionNotes\n  deliveryNotes\n  collect1PocFirstName\n  collect1PocLastName\n  collect1PocTitle\n  collect1PocNumber\n  collect1PocEmail\n  collect1PocAllowsText\n  collect1PreferredContactMethod\n  collect2PocFirstName\n  collect2PocLastName\n  collect2PocTitle\n  collect2PocNumber\n  collect2PocEmail\n  collect2PocAllowsText\n  collect2PreferredContactMethod\n  delivery1PocFirstName\n  delivery1PocLastName\n  delivery1PocTitle\n  delivery1PocNumber\n  delivery1PocEmail\n  delivery1PocAllowsText\n  delivery1PreferredContactMethod\n  delivery2PocFirstName\n  delivery2PocLastName\n  delivery2PocTitle\n  delivery2PocNumber\n  delivery2PocEmail\n  delivery2PocAllowsText\n  delivery2PreferredContactMethod\n  unmaskedId\n  qualitativeRating\n  creditRating\n  trustLevelNabis\n  trustLevelInEffect\n  isOnNabisTracker\n  locationNotes\n  infoplus\n  w9Link\n  taxIdentificationNumber\n  sellerPermitLink\n  nabisMaxTerms\n  __typename\n}\n\nfragment organizationFragment on Organization {\n  id\n  address1\n  address2\n  alias\n  city\n  doingBusinessAs\n  factoredStatus\n  hasAnalyticsDashboard\n  hasPlatformV2ApiAccess\n  infoplus\n  isBrand\n  isManufacturer\n  isRetailer\n  isSalesOrg\n  isMarketplace\n  licensedLocationId\n  logoS3Link\n  manifestGDriveFolderId\n  marketplaceContactEmail\n  marketplaceContactName\n  marketplaceContactNumber\n  name\n  phone\n  receiveReports\n  singleHubWarehouseId\n  singleHubWarehouse {\n    ...allWarehousesFragment\n    __typename\n  }\n  state\n  type\n  zip\n  __typename\n}\n\nfragment allWarehousesFragment on Warehouse {\n  ...warehouseFragment\n  site {\n    ...siteFragment\n    licenses {\n      ...licenseFragment\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment warehouseFragment on Warehouse {\n  id\n  isArchived\n  infoplus\n  region\n  isInUseByOps\n  isSingleHub\n  __typename\n}\n\nfragment siteFragment on Site {\n  id\n  name\n  address1\n  address2\n  city\n  state\n  zip\n  pocName\n  pocPhoneNumber\n  pocEmail\n  siteCategory\n  createdAt\n  licensedLocationId\n  __typename\n}\n\nfragment licenseFragment on License {\n  id\n  nickname\n  category\n  type\n  licenseNumber\n  legalEntityName\n  issuanceDate\n  expirationDate\n  contactName\n  contactPhone\n  contactEmail\n  address1\n  address2\n  city\n  state\n  zip\n  archivedAt\n  onboardedAt\n  __typename\n}\n\nfragment pageInfoFragment on PageInfo {\n  totalNumItems\n  totalNumPages\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    return response

# Flipping invoices to Yes on the Approved tab
def Factored_Approved_Tab_Yes(headers,invoice_data):
    json_data = {
        'operationName': 'UpdateFactoredInvoices',
        'variables': {
            'input': {
                'changedInvoices': [
                    {
                        'isReservePaid': False,
                        'isAdvancePaid': True,
                        'factorStatus': 'APPROVED',
                        'invoiceId': invoice_data['data']['getAdminFactoredInvoices']['results'][0]['id'],
                        'organizationId': invoice_data['data']['getAdminFactoredInvoices']['results'][0]['organization']['id'],
                    },
                ],
            },
        },
        'query': 'mutation UpdateFactoredInvoices($input: BulkUpdateFactorInvoiceInput!) {\n  bulkUpdateFactoredInvoices(input: $input)\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    return response


# Ready for reserve release tab

def Factored_Ready_for_release(headers,order_number):
    json_data = {
        'operationName': 'GetAdminFactoredInvoices',
        'variables': {
            'pageInfo': {
                'numItemsPerPage': 50,
                'orderBy': [
                    {
                        'attribute': 'date',
                        'order': 'DESC',
                    },
                    {
                        'attribute': 'createdAt',
                        'order': 'DESC',
                    },
                ],
                'page': 1,
            },
            'organizationId': None,
            'factorStatus': 'APPROVED',
            'isReservePaid': False,
            'isAdvancePaid': True,
            'paymentStatus': [
                'NET_TERMS_PAID',
                'SELF_COLLECTED',
                'REMITTED',
            ],
            'search': order_number,
            'start': None,
            'end': None,
        },
        'query': 'query GetAdminFactoredInvoices($organizationId: ID, $orderBy: String, $direction: String, $factorStatus: OrderFactorStatusEnum, $isAdvancePaid: Boolean, $isReservePaid: Boolean, $paymentStatus: [OrderPaymentStatusEnum], $search: String, $start: DateTime, $end: DateTime, $pageInfo: PageInfoInput) {\n  getAdminFactoredInvoices(organizationId: $organizationId, orderBy: $orderBy, direction: $direction, factorStatus: $factorStatus, isAdvancePaid: $isAdvancePaid, isReservePaid: $isReservePaid, paymentStatus: $paymentStatus, search: $search, start: $start, end: $end, pageInfo: $pageInfo) {\n    results {\n      ...factorFragment\n      creator {\n        ...userFragment\n        __typename\n      }\n      licensedLocation {\n        ...licensedLocationFragment\n        __typename\n      }\n      organization {\n        ...organizationFragment\n        __typename\n      }\n      site {\n        ...siteFragment\n        __typename\n      }\n      __typename\n    }\n    pageInfo {\n      ...pageInfoFragment\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment factorFragment on FactorInvoice {\n  id\n  advanceAmount\n  createdAt\n  creditMemo\n  date\n  daysTillPaymentDue\n  discount\n  distroFees\n  dueToBrand\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  factorStartDate\n  factorStatus\n  gmv\n  gmvCollected\n  invoicesS3FileLink\n  irn\n  isAdvancePaid\n  isReservePaid\n  manifestGDriveFileId\n  mustPayPreviousBalance\n  nabisDiscount\n  nabisDistroFees\n  name\n  netGmv\n  number\n  paidAt\n  paymentMethod\n  paymentStatus\n  paymentDueDate\n  pricingFee\n  pricingPercentage\n  remittedAt\n  reserveAmount\n  status\n  surcharge\n  totalFactorFee\n  totalFees\n  accountingNotes\n  __typename\n}\n\nfragment userFragment on User {\n  id\n  email\n  firstName\n  lastName\n  address1\n  address2\n  city\n  state\n  zip\n  phone\n  profilePicture\n  isAdmin\n  isDriver\n  driversLicense\n  __typename\n}\n\nfragment licensedLocationFragment on LicensedLocation {\n  id\n  name\n  address1\n  address2\n  city\n  state\n  zip\n  siteCategory\n  lat\n  lng\n  billingAddress1\n  billingAddress2\n  billingAddressCity\n  billingAddressState\n  billingAddressZip\n  warehouseId\n  isArchived\n  doingBusinessAs\n  noExciseTax\n  phoneNumber\n  printCoas\n  hoursBusiness\n  hoursDelivery\n  deliveryByApptOnly\n  specialProtocol\n  schedulingSoftwareRequired\n  schedulingSoftwareLink\n  centralizedPurchasingNotes\n  payByCheck\n  collectionNotes\n  deliveryNotes\n  collect1PocFirstName\n  collect1PocLastName\n  collect1PocTitle\n  collect1PocNumber\n  collect1PocEmail\n  collect1PocAllowsText\n  collect1PreferredContactMethod\n  collect2PocFirstName\n  collect2PocLastName\n  collect2PocTitle\n  collect2PocNumber\n  collect2PocEmail\n  collect2PocAllowsText\n  collect2PreferredContactMethod\n  delivery1PocFirstName\n  delivery1PocLastName\n  delivery1PocTitle\n  delivery1PocNumber\n  delivery1PocEmail\n  delivery1PocAllowsText\n  delivery1PreferredContactMethod\n  delivery2PocFirstName\n  delivery2PocLastName\n  delivery2PocTitle\n  delivery2PocNumber\n  delivery2PocEmail\n  delivery2PocAllowsText\n  delivery2PreferredContactMethod\n  unmaskedId\n  qualitativeRating\n  creditRating\n  trustLevelNabis\n  trustLevelInEffect\n  isOnNabisTracker\n  locationNotes\n  infoplus\n  w9Link\n  taxIdentificationNumber\n  sellerPermitLink\n  nabisMaxTerms\n  __typename\n}\n\nfragment organizationFragment on Organization {\n  id\n  address1\n  address2\n  alias\n  city\n  doingBusinessAs\n  factoredStatus\n  hasAnalyticsDashboard\n  hasPlatformV2ApiAccess\n  infoplus\n  isBrand\n  isManufacturer\n  isRetailer\n  isSalesOrg\n  isMarketplace\n  licensedLocationId\n  logoS3Link\n  manifestGDriveFolderId\n  marketplaceContactEmail\n  marketplaceContactName\n  marketplaceContactNumber\n  name\n  phone\n  receiveReports\n  singleHubWarehouseId\n  singleHubWarehouse {\n    ...allWarehousesFragment\n    __typename\n  }\n  state\n  type\n  zip\n  __typename\n}\n\nfragment allWarehousesFragment on Warehouse {\n  ...warehouseFragment\n  site {\n    ...siteFragment\n    licenses {\n      ...licenseFragment\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment warehouseFragment on Warehouse {\n  id\n  isArchived\n  infoplus\n  region\n  isInUseByOps\n  isSingleHub\n  __typename\n}\n\nfragment siteFragment on Site {\n  id\n  name\n  address1\n  address2\n  city\n  state\n  zip\n  pocName\n  pocPhoneNumber\n  pocEmail\n  siteCategory\n  createdAt\n  licensedLocationId\n  __typename\n}\n\nfragment licenseFragment on License {\n  id\n  nickname\n  category\n  type\n  licenseNumber\n  legalEntityName\n  issuanceDate\n  expirationDate\n  contactName\n  contactPhone\n  contactEmail\n  address1\n  address2\n  city\n  state\n  zip\n  archivedAt\n  onboardedAt\n  __typename\n}\n\nfragment pageInfoFragment on PageInfo {\n  totalNumItems\n  totalNumPages\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    return response

# Flipping to Yes invoices ready for release
def Factored_Ready_to_Release_Approved(headers,invoice_data):
    json_data = {
        'operationName': 'UpdateFactoredInvoices',
        'variables': {
            'input': {
                'changedInvoices': [
                    {
                        'isReservePaid': True,
                        'isAdvancePaid': True,
                        'factorStatus': 'APPROVED',
                        'invoiceId': invoice_data['data']['getAdminFactoredInvoices']['results'][0]['id'],
                        'organizationId': invoice_data['data']['getAdminFactoredInvoices']['results'][0]['organization']['id'],
                    },
                ],
            },
        },
        'query': 'mutation UpdateFactoredInvoices($input: BulkUpdateFactorInvoiceInput!) {\n  bulkUpdateFactoredInvoices(input: $input)\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    return response


def load_excel(file_path):
    book = load_workbook(file_path, data_only=True)
    writer = pd.ExcelWriter("temp.xlsx", engine="openpyxl")
    writer.book = book
    writer.save()
    writer.close()
    df = pd.read_excel("temp.xlsx")
    return df


def load_dataframe(file):
    """
    Loads the uploaded file into a Pandas DataFrame.
    """

    file_extension = file.name.split(".")[-1]
    
    if file_extension == "csv":
        df = pd.read_csv(file)

    elif file_extension == "xlsx":
        df = pd.read_excel(file)

    return df


def main_approved(invoices):
    for order in invoices:
        try:
            invoice_data = Factored_Requested(headers,order)
            response_approved = Update_factored_Invoices_Approved(headers,invoice_data)
            
            st.write(f'{order} Processed')
        except:
            
            st.write(f'{order} Failed, try again')
            st.write(invoice_data.text)
            st.write(response_approved.text)
            continue

def main_rejected(invoices):
    for order in invoices:
        try:    
            invoice_data = Factored_Requested(headers,order)
            response_rejected = Update_factored_Invoices_Rejected(headers,invoice_data)
            st.write(f'{order} Processed')
        except:
            st.write(f'{order} Failed, try again')
            st.write(invoice_data.text)
            st.write(response_rejected.text)
            continue

def main_flip_to_yes_approved_tab(invoices):
    for order in invoices:
        try:
            invoice_data = factored_Approved_tab(headers,order)
            response_yes = Factored_Approved_Tab_Yes(headers,invoice_data)
            st.write(f'{order} Processed')
        except:
            st.write(f'{order} Failed, try again')
            st.write(invoice_data.text)
            st.write(response_yes.text)
            continue

def main_flip_ready_for_release(invoices):
    for order in invoices:
        try:
            invoice_data = Factored_Ready_for_release(headers,order)
            response_released_approved = Factored_Ready_to_Release_Approved(headers,invoice_data)
            st.write(f'{order} Processed')
        except:
            st.write(f'{order} Failed, try again')
            st.write(invoice_data.text)
            st.write(response_released_approved.text)
            continue


col1,col2 = st.columns([2,1])
with col1:
    list_orders = st.file_uploader('Upload List of invoices.',accept_multiple_files=False)
    

if list_orders is not None:
        #df = load_excel(list_orders)
        df = load_dataframe(list_orders)
        df['Invoice'] = df['Order'].astype('str')
        count_invoices = df.shape
        st.write(f'{count_invoices[0]} Invoices to Update')
        
        with col2:
            select_tab = st.selectbox('Select Tab',options=['Requested','Approved','Ready For Reserve Release'])

            if select_tab == 'Requested':
                selection = st.radio('Approve or Reject Order',options=['Approve','Reject'])
                if selection == 'Approve':
                        st.caption('Click Button below to process')
                        submit_to_approve = st.button('Approve Order')
                        if submit_to_approve:
                            main_approved(df["Invoice"])

                elif selection == 'Reject':            
                        st.caption('Click Button below to process')
                        submit_to_reject = st.button('Reject Order')
                        if submit_to_reject:
                            main_rejected(df["Invoice"])

            elif select_tab == 'Approved':
                st.caption('Click Button below to process')
                submit_to_yes = st.button('Flip to Yes')
                if submit_to_yes:
                    main_flip_to_yes_approved_tab(df["Invoice"])

            elif select_tab == 'Ready For Reserve Release':
                st.caption('Click Button below to process')
                submit_to_ready_for_release = st.button('Flip ready for release')
                if submit_to_ready_for_release:
                    main_flip_ready_for_release(df["Invoice"])



st.markdown('---')
left_col,center_col,right_col = st.columns(3)

with center_col:
    st.title('**Powered by HQ**')
    st.image('https://www.dropbox.com/s/twrl9exjs8piv7t/Headquarters%20transparent%20light%20logo.png?dl=1')

