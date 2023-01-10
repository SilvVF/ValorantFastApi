# ValorantFastApi

to run in terminal put 

uvicorn main:app --reload

from local host 
GET localhost:8000/player/{name}/{tagline}
- returns json with the players kd
{ 
   "kd": float,
   "kda": float,
   "defKda": float
}
