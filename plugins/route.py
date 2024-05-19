#Coded by KA18 the @legend580 💛❤️

from aiohttp import web

routes = web.RouteTableDef()

text = """
      _ _   _  __     ___     _              ____        _ _ _   _              ____        _   
     | | \ | | \ \   / (_) __| | ___  ___   / ___| _ __ | (_) |_| |_ ___ _ __  | __ )  ___ | |_ 
  _  | |  \| |  \ \ / /| |/ _` |/ _ \/ _ \  \___ \| '_ \| | | __| __/ _ \ '__| |  _ \ / _ \| __|
 | |_| | |\  |   \ V / | | (_| |  __/ (_) |  ___) | |_) | | | |_| ||  __/ |    | |_) | (_) | |_ 
  \___/|_| \_|    \_/  |_|\__,_|\___|\___/  |____/| .__/|_|_|\__|\__\___|_|    |____/ \___/ \__|
                                                  |_|                                           
"""
@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response(text)
