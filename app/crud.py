from app import external_api, schemas


def get_all_posts() -> list[dict]:
    data = external_api.fetch_all()
    return [schemas.Post(**it) for it in data]


def get_post_by_id(post_id: int):
    data = external_api.fetch_by_id(post_id)
    if data is None:
        return None
    return schemas.Post(**data)


def create_post(payload: schemas.PostCreate):
    created = external_api.create(payload.dict())
    if created is None:
        return None
    return schemas.Post(**created)
