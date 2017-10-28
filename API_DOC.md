### Eottoke API Guide
----

##### Common Endpoints 

- Get list of all categories: `/api/v1/category/list`
- Get list of all material with specific category `api/v1/category/material/:category_id/`
- Get component with specific material `api/v1/category/component/:material_id?category=category_id`
- Get list of main components `api/v1/component/list/`
- Get single main component with minor components `api/v1/component/:component_id/`
- Get list of all products `api/v1/product/list`
- Get single product `api/v1/product/:product_id`
- Get a product with specific bar code `api/v1/product/code/:code`
- Sample Request:  `http://128.199.69.81:8000/api/v1/category/list`

##### Response Values

1. Category List 

```json
[
    {
        "id": 1,
        "name": "Bottles"
    },
    {
        "id": 2,
        "name": "Household"
    },
    {
        "id": 3,
        "name": "Cans"
    }
]

```

2. Material with specific Category (let's say id=1)

```json
{
    "materials": [
        {
            "id": 8,
            "name": "Plastic"
        }
    ]
}

```

3. Main components for a Material with specific id

```json
{
    "component": {
        "id": 1,
        "name": "Bottles - Glass",
        "category": "Bottles",
        "material": "Glass",
        "recyclinginfomation": "Recycling info:.",
        "minor_components": [
            {
                "id": 1,
                "name": "Paper Container Label Of Bottle",
                "material": "Paper",
                "recyclinginfomation": "As"
            },
            {
                "id": 2,
                "name": "Plastic Container Cap Of Bottle",
                "material": "Plastic",
                "recyclinginfomation": "Most"
            },
            {
                "id": 3,
                "name": "Metal Container Cap Of Bottle",
                "material": "Metal",
                "recyclinginfomation": "you "
            }
        ]
    }
}

```

4. List of Main components


```json
[
    {
        "id": 1,
        "name": "Cans_Paper",
        "category": "Cans",
        "material": "Paper",
        "recyclinginfomation": null,
        "minor_components": []
    },
    {
        "id": 2,
        "name": "Household_Plastic",
        "category": "Household",
        "material": "Plastic",
        "recyclinginfomation": null,
        "minor_components": []
    },
    {
        "id": 3,
        "name": "Bottle_plastic",
        "category": "Bottles",
        "material": "Plastic",
        "recyclinginfomation": null,
        "minor_components": [
            {
                "id": 1,
                "name": "Cap",
                "material": "Plastic",
                "recyclinginfomation": null
            },
            {
                "id": 2,
                "name": "Body",
                "material": "Paper",
                "recyclinginfomation": null
            }
        ]
    }
]

```

5. Main component detail with minor components

```json
{
    "id": 3,
    "name": "Bottle_plastic",
    "category": "Bottles",
    "material": "Plastic",
    "recyclinginfomation": null,
    "minor_components": [
        {
            "id": 1,
            "name": "Cap",
            "material": "Plastic",
            "recyclinginfomation": null
        },
        {
            "id": 2,
            "name": "Body",
            "material": "Paper",
            "recyclinginfomation": null
        }
    ]
}

```


6. List of all the products

```json

[
    {
        "id": 1,
        "name": "Evian",
        "code": "1111vagag",
        "photo": "/media/product_images/evian_8h1mL9m.jpg",
        "main_component": {
            "id": 1,
            "name": "plastic bottle",
            "type": "Main",
            "category": "hello",
            "material": "Glass"
        },
        "slug": "evian",
        "updated_at": "2017-10-28T04:35:50.608357+09:00",
        "created_at": "2017-10-28T04:35:50.608280+09:00"
    }
]
```

7. Product Detail 

```json
{
    "id": 1,
    "name": "Evian 500ml",
    "code": "3089080",
    "photo": "/media/product_images/evian.jpg",
    "main_component": {
        "id": 3,
        "name": "Bottle_plastic",
        "category": "Bottles",
        "material": "Plastic",
        "recyclinginfomation": null,
        "minor_components": [
            {
                "id": 1,
                "name": "Cap",
                "material": "Plastic",
                "recyclinginfomation": null
            },
            {
                "id": 2,
                "name": "Body",
                "material": "Paper",
                "recyclinginfomation": null
            }
        ]
    },
    "slug": "evian-500ml",
    "updated_at": "2017-10-28T15:51:48.968091+09:00",
    "created_at": "2017-10-28T15:51:48.968003+09:00"
}

```

8. Get Product with code 

```json
{
    "id": 1,
    "name": "evian 500ml",
    "code": "3068320024400",
    "photo": "/media/product_images/evian_vibX4vF.jpg",
    "main_component": {
        "id": 4,
        "name": "Bottles - Plastic",
        "category": "Bottles",
        "material": "Plastic",
        "recyclinginfomation": "Recycling info:\r\nPlease rinse the containers before disposal and place them in a clear plastic bag. Just like general waste, the recyclable waste should be placed outside the building or in designated areas/bins.\r\n\r\nNOTE:\r\nContainers that are plastic-coated are not fit for recycling and should be disposed of together with general waste.\r\n\r\nExtra buttons:\r\n“What if my container has a paper label?” >> As long as the label is easily removable and made only of paper, you can remove it and put it together with paper recycling waste. However paper and glue is easily removed during normal recycling process, so you can skip this altogether.",
        "minor_components": [
            {
                "id": 7,
                "name": "Paper Label",
                "material": "Paper",
                "recyclinginfomation": "As long as the label is easily removable and made only of paper, you can remove it and put it together with paper recycling waste. However paper and glue is easily removed during normal recycling process, so you can skip this altogether."
            }
        ]
    },
    "slug": "evian-500ml",
    "updated_at": "2017-10-28T20:56:28.975000+09:00",
    "created_at": "2017-10-28T20:56:28.975000+09:00"
}

```