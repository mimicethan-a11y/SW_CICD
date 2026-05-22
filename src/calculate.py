from fastapi import FastAPI

app = FastAPI()

def add_f(a, b):
    return a + b


def sub_f(a, b):
    return a - b


def mut_f(a: float, b: float) -> float:
    return a * b


@app.get("/")
def home():
    return {"status": "Online", "message": "這是簡易計算機 API"}


@app.get("/add")
def calculate_add(a: float, b: float):
    # add_func
    result = add_f(a, b)
    return {"operation": "addition", "x": a, "b": b, "result": result}