"""
https://petstore.swagger.io/#/store/placeOrder

{
  "id": 0,
  "petId": 0,
  "quantity": 0,
  "shipDate": "2023-08-31T15:14:36.206Z",
  "status": "placed",
  "complete": true
}

"""
request = {}
request["id"] = 1
request["petId"] = 1
request["quantity"] = 1
request["shipDate"] = "2023-08-31T18:15:36.206Z"
request["status"] = "not placed"
request["complete"] = False
