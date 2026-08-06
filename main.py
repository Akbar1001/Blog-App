from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello FastAPI!"}


@app.get("/health")
def health():
    return "Server running successfully"


@app.get("/about")
def about():
    return {
        "developer": " Dev-1",
        "project":"Expense Tracker",
        "framework": "NodeJs"
    }


@app.get("/contact")
def contact():
    return{
        "email" : "hello@gmail.com",
        "number" : "12123456789"
    }

@app.get("/profile")
def profile():
    return {
        "name": "Akbar Husain",
        "role": "Backend Developer"
    }

@app.get("/skills")
def skills():
    return {
    "programming_languages":[
        "Python",
        "C++",
        "Java",
        "JavaScript"
    ],

    "frameworks":[
        "FastAPI",
        "Django",
        "Node.js",
        "Spring Boot"
    ],

    "databases":[
        "PostgreSQL",
        "MongoDB",
        "MySQL"
    ]
}

# blog with an ID
@app.get("/blogs/{blog_id}")
def get_blog_by_id(blog_id:int):
    return {
        "blog_id" :blog_id  
    }
#user with an id
@app.get("/users/{user_id}")
def get_user_by_id(user_id:int):
    return{
        "user_id":user_id
    }


# #Filtering on the basis of name
# @app.get("/blogs")
# def get_blogs(author :str):
#     return{
#         "author": author
#     }

# #pagination 
# @app.get("/blogs")
# def get_blogs(page:int=1, limit:int=10):
#     return{
#         "page": page,
#         "limit": limit
#     }

#we can have both pagination and filtering at the same time
@app.get("/blogs")
def get_blogs(page: int=1 , limit : int=10, author: str | None=None):
    return{
        "page": page,
        "limit": limit,
        "author": author
    }
