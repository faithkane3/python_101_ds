#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:14:43 2019

@author: faith
"""

shopping_cart = {
    "tax": .08,
    "items": [
        {
            "title": "orange juice",
            "price": 3.99,
            "quantity": 1
        },
        {
            "title": "rice",
            "price": 1.99,
            "quantity": 3
        },
        {
            "title": "beans",
            "price": 0.99,
            "quantity": 3
        },
        {
            "title": "chili sauce",
            "price": 2.99,
            "quantity": 1
        },
        {
            "title": "chocolate",
            "price": 0.75,
            "quantity": 9
        }
    ]
}

def total_number_of_items(shopping_cart):
    return sum([item["quantity"] for item in shopping_cart["items"]])
# =============================================================================
#     lst = my_dict.get("items")
#     x = [item.pop("quantity") for item in lst]
#     return sum(x)
# =============================================================================
