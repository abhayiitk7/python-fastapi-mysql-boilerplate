from fastapi import FastAPI
import uvicorn
import logging
from api.routes.route1 import sample_route


app = FastAPI()

logging.basicConfig(filename='app.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)

app.include_router(sample_route)

# , prefix="/api/v1/routes"


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)