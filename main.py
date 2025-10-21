from fastapi import FastAPI, Query, Body
import uvicorn

app = FastAPI()

hotels = [
    {'id': 1, 'title': 'Sochi', 'name': 'sochi'},
    {'id': 2, 'title': 'Dubai', 'name': 'dubai'},
]


@app.get('/hotels')
def get_hotels(
        id: int | None = Query(None, description='ID отеля'),
        title: str | None = Query(None, description='Название отеля')
):
    hotels_ = []
    for hotel in hotels:
        if id and hotel['id'] != id:
            continue
        if title and hotel['title'] != title:
            continue
        hotels_.append(hotel)
    return hotels_


@app.post('/hotels')
def create_hotel(
        title: str = Body(embed=True)
):
    global hotels
    hotels.append({
        'id': hotels[-1]['id'] + 1,
        'title': title
    })
    return {'status': 'OK'}

@app.delete('/hotels/{hotel_id}')
def del_hotel(hotel_id: int):
    global hotels
    hotels = [hotel for hotel in hotels if hotel['id'] != hotel_id]
    return {'status': 'OK'}

@app.put("/hotels/{hotel_id}")
def change_hotel(
        hotel_id: int,
        title: str = Body(),
        name: str = Body()
):
    global hotels
    hotels[hotel_id-1]['title'] = title
    hotels[hotel_id-1]['name'] = name
    return {'status': 'OK'}

@app.patch("/hotels/{hotel_id}")
def edit_hotel(
        hotel_id: int,
        title: str | None = Body(None),
        name: str | None = Body(None)
):
    global hotels
    if name:
        hotels[hotel_id - 1]['name'] = name
    if title:
        hotels[hotel_id - 1]['title'] = title
    return {'status': 'OK'}


if __name__ == '__main__':
    uvicorn.run('__main__:app', reload=True)
