import uvicorn
from fastapi import FastAPI
from Routers import books as BookRouter
from Routers import authors as AuthorRouter
from Routers import  categories as CategoryRouter

app = FastAPI()
app.include_router(BookRouter.router, prefix="/book")
app.include_router(AuthorRouter.router, prefix="/author")
app.include_router(CategoryRouter.router, prefix="/category")

if __name__ == "__main__":
    uvicorn.run("main:app", host='localhost', port=3000, reload=True,workers=3)

