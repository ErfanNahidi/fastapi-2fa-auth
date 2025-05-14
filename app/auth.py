from fastapi import APIRouter , Depends , HTTPException , status
from sqlalchemy.orm import Session
from passlib.context import CryptContext # type: ignore
import pyotp , jwt , os # type: ignore
from . import models , database


pwd_ctx = CryptContext(schemes=["bcrypt"] , deprecated="auto")
router = APIRouter(prefix="/auth")
JWT_SECRET = os.getenv("JWT_SECRET" , "secret")

@router.post("/register")
def register(username: str , password: str , db:Session = Depends(database.SessionLocal)):
    hashed = pwd_ctx.hash(password)
    secret = pyotp.random_base32(32)
    user = models.User(username=username , password_hash=hashed , opt_secret=secret)
    db.add(user) ; db.commit()
    return {"opt_uri": pyotp.totp(secret).provisioning_uri(username , issuer_name="FastAPI-2FA-Auth")}

@router.post("/login")
def login(username:str , password:str , db:Session = Depends(database.SessionLocal)):
    user = db.query(models.User).filter_by(username=username).first() or _raise()
    if not pwd_ctx.verify(password, user.password_hash): _raise()
    return {"msg": "enter OTP"}

@router.post("/verify-otp")
def verify_otp(username: str, code: str, db: Session = Depends(database.SessionLocal)):
    user = db.query(models.User).filter_by(username=username).first() or _raise()
    totp = pyotp.TOTP(user.otp_secret)
    if not totp.verify(code, valid_window=1):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    token = jwt.encode({"sub": str(user.id)}, JWT_SECRET, algorithm="HS256")
    return {"access_token": token}

def _raise():
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)