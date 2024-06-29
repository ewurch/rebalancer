import json
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Form

templates = Jinja2Templates(directory="templates")

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


class CryptoPortfolio(BaseModel):
    assets: dict


class FinancialObjectives(BaseModel):
    objectives: dict


CRYPTO_PORTFOLIO = {
    "btc": "Bitcoin (BTC)",
    "eth": "Ethereum (ETH)",
    "ada": "Cardano (ADA)",
    "sol": "Solana (SOL)",
    "dot": "Polkadot (DOT)",
    "usdt": "Tether (USDT)",
    "usdc": "USD Coin (USDC)",
}

@app.get("/", response_class=HTMLResponse)
async def read_form():
    return templates.TemplateResponse("index.html", {"request": {}})


@app.post("/rebalance")
async def rebalance(portfolio: str = Form(...), objectives: str = Form(...)):
    portfolio = json.loads(portfolio)
    objectives = json.loads(objectives)
    rebalance_strategy = await get_rebalance_strategy(portfolio, objectives)
    return {"strategy": rebalance_strategy}


@app.get("/no-portfolio-form")
def no_portfolio_form(request: Request):
    return templates.TemplateResponse(
        "partials/no_portfolio_form.html", 
        {"request": request, "crypto_portfolio": CRYPTO_PORTFOLIO}
    )

@app.post("/no-portfolio-form")
async def calculate_no_portfolio_form(
        request: Request,
        amount: float = Form(...),
    ):
    form_data = await request.form()
    print(form_data)
    print(amount)
    return templates.TemplateResponse(
        "partials/no_portfolio_form.html",
        {"request": request, "crypto_portfolio": CRYPTO_PORTFOLIO}
    )

async def get_rebalance_strategy(portfolio, objectives):
    # Logic to interact with ChatGPT
    # Placeholder logic
    return "Generated rebalance strategy based on portfolio and objectives"


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
