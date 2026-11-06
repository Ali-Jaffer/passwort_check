from fastapi import FastAPI
from pydantic import BaseModel
from .passwort_checker import pruefe_passwort

app = FastAPI()


class PasswortAnfrage(BaseModel):
    passwort: str


@app.post("/passwort-check")
def passwort_check(anfrage: PasswortAnfrage):
    ergebnis = pruefe_passwort(anfrage.passwort)
    return {"passwort_laenge": len(anfrage.passwort), "bewertung": ergebnis}
