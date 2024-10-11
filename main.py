from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"nombre": "Miguel Lopez Ariza"}

@app.get("/users")
def list_users():
    return [
        {
            'name':'Miguek Lopez Ariza',
            'email':'Lopezarizamiguel@gmail.com'
        },
        {
            'name':'Leo Lopez Ariza',
            'email':'lopezarizamiguel@gmail.com'
        }
    ]
