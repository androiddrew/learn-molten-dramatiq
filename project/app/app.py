from molten import App, Route


def ping():
    return {"message": "Pong!"}


app = App(routes=[Route("/ping", ping, method="GET")])
