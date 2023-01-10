import json
import undetected_chromedriver as uc
from player_keys import PlayerDataKeys
from typing import Union
from fastapi import FastAPI

app = FastAPI()
options = uc.ChromeOptions()
options.headless = True
driver = uc.Chrome(use_subprocess=True, options=options)

recent_fetch_cache = {}


def log_cache():
    for k, v in recent_fetch_cache:
        print(k + "     " + v)


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/cache")
def read_cache():
    return recent_fetch_cache


# uvicorn main:app --reload
@app.get("/player/{name}/{tagline}")
def read_item(name: str, tagline: str, q: Union[str, None] = None):
    if recent_fetch_cache.get(name + tagline, False):
        return recent_fetch_cache[name + tagline]
    driver.get('https://tracker.gg/valorant/profile/riot/' + name + '%23' + tagline + '/overview')
    html = driver.page_source
    target = "window.__INITIAL_STATE__ ="
    start = html.find(target) + len(target)
    current = html[start:]
    json_site_data = current[:current.find("</script>")]
    data = PlayerDataKeys(json.loads(json_site_data)['stats']['standardProfiles'][0]['segments'][0]["stats"])
    response = {
        "kd": data.kDRatio,
        "kda": data.kDARatio,
        "defKda": data.defenseKDRatio
    }
    recent_fetch_cache[name + tagline] = response
    return response
