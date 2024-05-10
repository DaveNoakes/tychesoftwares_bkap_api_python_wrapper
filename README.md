# Tychesoftwares WooCommerce Bookings & Appointments API - Python Wrapper

A python module to work with the Tychesoftwares Bookings & Appointments REST API.
API documentation here
https://www.tychesoftwares.com/docs/woocommerce-booking-appointment-plugin/booking-appointment-rest-api/

This module is an adaptation of the WooCommerce API python SDK by Claudio Sanches @ Automattic.

## Create an API instance

```
bkapapi = BkapAPI(
    url=URL,
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    timeout=None
    )
```

## Get Bookings

```
bkapapi.get('bookings')
```

Optional paramaters can be added:

```
params = {
    "start_date": "2024-01-01",
    "product_id": 68,
}

bkapapi.get('bookings', params=params)
```

## List Booking Information for a Booking ID

```
bkapapi.get('bookings/68')
```

## Count Bookings

```
bkapapi.get('bookings/count')
```

## Create Booking

```
data = {
    "product_id": 273,
    "quantity": 1,
    "start_date": "2021-09-24",
    "end_date": "2021-09-24",
    "price": 150,
    "customer_id": 1,
    "resource_id":10
}

bkapapi.post('bookings', data=data)
```

**_Visit the official documentation for more examples of parameters for different product types_**

## Update Booking

```
{
    "quantity":2,
    "status":"paid",
    "price":400,
    "start_date": "2021-09-29",
    "start_time": "10:00",
    "end_time": "11:00"
}

bkapapi.put('bookings/68', data=data)
```

## Delete Booking

```
bkapapi.delete('bookings/68')
```

## Booking Availablitity

```
bkapapi.get('bookings/availablity')
```

### Booking Resources

```
bkapapi.get('resources')
```

### List Resources for a Resource ID

```
bkapapi.get('resources/68')
```

### Resources Count

```
bkapapi.get('resources/count')
```

### Delete Booking Resource

```
bkapapi.delete('resources/68')
```

### Booking Products

```
bkapapi.get('products')
```

### List Booking Product for a Product ID

```
bkapapi.get('products/68')
```

### Count Booking Products

```
bkapapi.get('products/count')
```

### Update Booking Product

```
data = {
    "booking": {
        "enable_booking": "on",
        "booking_type": "only_day",
        "enable_inline_calendar": "on",
        "booking_can_be_cancelled": "off"
    }
}

bkapapi.put('products/68', data=data)
```

### Delete Booking Product

```
bkapapi.delete('products/68')
```
