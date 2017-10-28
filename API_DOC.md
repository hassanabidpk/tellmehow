### Eottoke API Guide
----

##### Common Endpoints 

- Get list of all categories: `/api/v1/category/list`
- Get list of all material with specific category `api/v1/category/material/:category_id/`
- Get list of components with specific material `api/v1/category/component/:material_id`
- Get list of main components `api/v1/component/list/`
- Get list of single main component with minor components `api/v1/component/:component_id/`
- Get list of all products `api/v1/product/list`
- Get list of single product `api/v1/product/:product_id`
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

3. List of Main components for a Material

```json
{
    "components": [
        {
            "id": 11,
            "name": "Household - Ceramics",
            "category": "Household",
            "material": "Ceramics",
            "recyclinginfomation": "Recycling info:\r\n\tCeramics are generally not recyclable. However there might be local organisations or industries that accept pottery or ceramic construction materials like used tiles.",
            "minor_components": []
        }
    ]
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