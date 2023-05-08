from pymongo import MongoClient
import pandas as pd





def mongo(database, collection):
    client = MongoClient("localhost:27017")
    db = client[database]
    c = db.get_collection(collection)
    return c




def startups (raised_ammount, year):
    
    tech_startup = MongoClient("localhost:27017")["ironhack"].companies.aggregate([
        {
            "$unwind": "$funding_rounds"
        },
        {
            "$group": {
                "_id": "$_id",
                "name": {
                    "$first": "$name"
                },
                "raised_amount": {
                    "$sum": "$funding_rounds.raised_amount"
                },
                "offices": {
                    "$first": "$offices"
                },
                "category_code": {
                    "$first": "$category_code"
                },
                "founded_year": {
                    "$first": "$founded_year"
                }
            }
        },
        {
            "$match": {
                "raised_amount": {
                    "$gte": raised_ammount
                },
                "category_code": {
                    "$in": [
                        "games_video",
                        "analytics",
                        "biotech",
                        "cleantech",
                        "ecommerce",
                        "games_video",
                        "hardware",
                        "messaging",
                        "mobile",
                        "nanotech",
                        "network_hosting",
                        "search",
                        "semiconductor",
                        "social",
                        "software",
                        "transportation",
                        "travel",
                        "web"
                    ]
                },
                "founded_year": {
                    "$gte": year
                }
            }
        },
        {
            "$project": {
                "_id": 0,
                "name": 1,
                "raised_amount": 1,
                "offices": 1,
                "category_code": 1,
                "founded_year": 1
            }
        }
    ])
    ret = list(tech_startup)
    print(len(ret), " companies.")
    return ret




def design ():
   
    design_companies = MongoClient("localhost:27017")["ironhack"].companies.aggregate([
        {
            "$match": {
                "category_code": {
                    "$in": [
                        "design",
                        "fashion",
                        "photo_video"
                    ]
                }
            }
        },
        {
            "$project": {
                "_id": 0,
                "name": 1,
                "offices": 1
            }
        }
    ])
    ret = list(design_companies)
    print(len(ret), " companies.")
    return ret