from fastapi import FastAPI
from whenconnect import when_connect, when_disconnect


class DeviceManager(object):
    DEVICE_SET = set()

    @classmethod
    def add(cls, device):
        cls.DEVICE_SET.add(device)

    @classmethod
    def remove(cls, device):
        cls.DEVICE_SET.remove(device)


when_connect(device='any', do=DeviceManager.add)
when_disconnect(device='any', do=DeviceManager.remove)

app = FastAPI()


@app.get("/")
def hello():
    return {"Hello": "World"}


@app.get("/devices")
def all_devices():
    return {"devices": list(DeviceManager.DEVICE_SET)}


# start server with:
#   uvicorn server:app --reload
