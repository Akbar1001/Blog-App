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
