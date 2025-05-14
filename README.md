
# FastAPI 2FA Authentication Demo 🚀

A no-nonsense, production-ready boilerplate for secure two-factor authentication in FastAPI. Built with bcrypt hashing, PyOTP TOTP, and JWT, this demo equips your endpoints with rock-solid protection.


## 🔍 Overview
- **Hashing**: `passlib` + **bcrypt**
- **2FA**: `pyotp` (TOTP) & provisioning URIs for Google Authenticator
- **Tokens**: JWT (`pyjwt`)
- **Database**: SQLAlchemy ORM
- **Framework**: FastAPI

Built for engineers who demand clarity, security, and speed.

---

## ⚙️ Features
- **Register**: Securely hash passwords & generate a secret for 2FA.
- **Login**: Verify credentials before prompting for OTP.
- **Verify OTP**: Validate TOTP codes & issue JWT access tokens.
- **Modular**: Easy to extend for refresh tokens, roles, scopes.

---

## 🛠 Prerequisites
- Python 3.9+
- FastAPI
- Uvicorn
- SQLAlchemy
- Passlib
- PyOTP
- PyJWT

Install with:
```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] pyotp pyjwt
````

---

## 🚀 Quickstart

1. **Clone**

   ```bash
   git clone [https://github.com/your-repo/fastapi-2fa-auth.git](https://github.com/your-repo/fastapi-2fa-auth.git)
   cd fastapi-2fa-auth
   ```



````

2. **Configure**
   - Create a `.env`:
     ```ini
     JWT_SECRET=your-very-secret-key
     DATABASE_URL=sqlite:///./test.db
     ```

3. **Run**
   ```bash
uvicorn app.main:app --reload
````

4. **Test Endpoints**

   * **Register**: `POST /auth/register` ➡️ returns `otp_uri` for provisioning
   * **Login**: `POST /auth/login` ➡️ returns `msg: "enter OTP"`
   * **Verify OTP**: `POST /auth/verify-otp` ➡️ returns `{ access_token: <JWT> }`

---

## 📫 Usage Example

```bash
# Register a new user\ ncurl -X POST http://localhost:8000/auth/register -d 'username=john&password=1234'
# Login (password)
curl -X POST http://localhost:8000/auth/login -d 'username=john&password=1234'
# Verify (OTP code)
curl -X POST http://localhost:8000/auth/verify-otp -d 'username=john&code=123456'
```

---

## 🧩 Extending

* Add refresh tokens
* Integrate roles & permissions
* Switch DB for PostgreSQL/MySQL
* Plug-in SMS/email 2FA channels

---

## 📝 License

MIT © 2025
