from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/user_profile")
async def user_profile(user_id: int):
    user_profiles = {
        1: {
            'user_id': 1,
            'username': 'Jane Doe',
            'favorite_color': 'Green'
        },
        2: {
            'user_id': 2,
            'username': 'John Doe',
            'favorite_color': 'Blue'
        },
    }
    if user_id in user_profiles:
        return {"profile": user_profiles[user_id]}
    else:
        return {"error": "User not found"}


@app.get("/personal_greeting")
async def personal_greeting(username: str):
    return {"message": f"Hello, {username}!"}


@app.get("/greeting")
async def greeting():
    return {"message": "Hello, World!"}


@app.get("/")
async def root():
    return {"message": "Welcome to Fast API Proof of Concept"}


def main():
    uvicorn.run(app, host="127.0.0.1", port=8000)


if __name__ == "__main__":
    main()
