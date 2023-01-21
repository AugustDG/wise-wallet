for now just going to have one http req:

req body (itemPrice has to be by quantity)
(only supporst some fruits and vegetables rn):


{
    [
        {  
            "itemName": "apple",
            "itemPrice": 5.99
        },
        {  
            "itemName": "banana",
            "itemPrice": 3.99
        }
    ]
}

response body (will only return items it supports
and items that you can find better price for):

{
    [
        {  
            "itemName": "apple",
            "curPrice": 5.99,
            "bestPrice": 0.70,
            "bestUrl": "iga.com/apple1"
        },
        {  
            "itemName": "banana",
            "itemPrice": 3.99,
            "bestPrice": 0.90,
            "bestUrl": "iga.com/banana2"
        }
    ]
}

