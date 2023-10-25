from typing import Union

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/dday")
def get_dday():
    """
    # D-DAY
    ![LGTM](https://i.lgtm.fun/2lwa.gif)
    """
    from dday.dday import calculate_dday
    r = calculate_dday()
    return {"dday": r}
