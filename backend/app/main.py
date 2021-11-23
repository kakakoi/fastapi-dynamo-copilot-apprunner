import uvicorn

from fastapi import FastAPI
from dbcon import Crud
import json
from decimal import Decimal
import pprint

app = FastAPI()

# movie_table = create_movie_table()

# with open("moviedata.json") as json_file:
#     movie_list = json.load(json_file, parse_float=Decimal)
# load_movies(movie_list)

crud = Crud()

movie_resp = crud.put_movie("The Big New Movie", 2015,
                        "Nothing happens at all.", 0)
print("Put movie succeeded:")
pprint.pp(movie_resp, sort_dicts=False)

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)