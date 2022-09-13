from fastapi import FastAPI
from fastapi.exceptions import HTTPException

from . import models
from .database import SessionLocal, engine
from .interactors import calculate_ytd_statistics
from .models import Portfolio
from .schemas import DataSchema, PortfolioSchema
from .session import authenticate, get_session, has_admin_permission

models.Base.metadata.create_all(bind=engine)

app = FastAPI()
db = SessionLocal()


@app.post('/auth/')
def auth(username: str):
    return authenticate(username)


@app.get('/portfolio/')
def portfolio(jwt: str):
    username = get_session(jwt)['username']
    return db.query(Portfolio).filter(Portfolio.username==username).first()


@app.get('/ytd-stats/')
def ytd_statistics(jwt: str):
    username = get_session(jwt)['username']
    return calculate_ytd_statistics(username)


@app.post('/clear/')
def clear(jwt: str):
    username = get_session(jwt)['username']
    if not has_admin_permission(username):
        raise HTTPException(403)

    db.query(Portfolio).delete()
    db.commit()
    return {'status': 'ok'}


@app.post("/portfolio/")
def set_portfolio(pf: DataSchema, jwt: str):
    username = get_session(jwt)['username']
    portfolio = db.query(Portfolio).filter(Portfolio.username==username).first()
    if not portfolio:
        portfolio = Portfolio(username=username, data=pf.data)
        db.add(portfolio)
    else:
        portfolio.data = pf.data

    db.commit()
    db.refresh(portfolio)
    return PortfolioSchema.from_orm(portfolio)
