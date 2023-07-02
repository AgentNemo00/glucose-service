import uvicorn

from api.handler import *

if __name__ == '__main__':
    uvicorn.run(app=router, host='0.0.0.0', port=int(os.getenv("SERVICE_PORT", default="10001")))
