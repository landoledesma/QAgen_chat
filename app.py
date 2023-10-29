from fastapi import FastAPI, Form, Request, Response, File, Depends, HTTPException, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder

import os 
import json
import time
import uvicorn


import csv

from dotenv import load_dotenv
import os

load_dotenv("token.env")
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

app = FastAPI()
app.mount("/static",StaticFiles(directory="static",name="static"))
template = Jinja2Templates(directory="templates")

