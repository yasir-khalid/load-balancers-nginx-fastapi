from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socket
from datetime import datetime
from faker import Faker

app = FastAPI()
"""FastAPI runs through the code top to bottom and prioritses API logic based
on the function that appears first
"""
# Add CORS middleware to allow all origins, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

fake = Faker()
@app.get("/synthetic")
async def system_information():
    return {
        "version": "1.0.0",
        "Request received": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"),
        "server_id": str(socket.gethostname()),
        "data": {
                'person_id':fake.uuid4(),
                'first_name':fake.first_name(),
                'last_name':fake.last_name(),
                'address':fake.address(),
                'dob':fake.date_of_birth(minimum_age = 18, maximum_age = 75),
                'ssn':fake.ssn()
            }
    }
