from fastapi import FastAPI, File, Request, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

origins = ["*"]

image_results = {}

with open('./data/classification_results.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        image_results[row[0]] = row[1]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/getAnswer", tags=["Root"])
async def read_root(image:UploadFile = File(...)):
    result = image_results[image.filename.split(".")[0]]
    return {image.filename: result}