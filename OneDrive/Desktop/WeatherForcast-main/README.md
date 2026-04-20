# Weather Flask App

## Local Run

```
pip install -r requirements.txt
python app.py
```

Open http://127.0.0.1:5000

## Deploy to GitHub Pages? (Static only)

GitHub Pages is for static HTML/CSS/JS. For Flask (dynamic Python), use **Render.com** or **Railway.app** (free tiers).

### Render.com (Recommended, Free)

1. Push to GitHub repo.
2. render.com → New → Web Service → Connect GitHub repo.
3. Settings:
   - Runtime: Python 3
   - Build: `pip install -r requirements.txt`
   - Start: `gunicorn app:app` (install gunicorn: add to requirements.txt)
4. Environment: Add `WEATHERAPI_KEY` (rotate your key).
5. Deploy → Live URL.

**Add to requirements.txt**:

```
gunicorn
```

**Update app.py prod** (add if **name** check):

```python
if __name__ == '__main__':
    app.run(debug=False, port=10000)  # Render uses PORT env
```

Use `gunicorn app:app` for prod.

### Railway.app

Similar: Connect GitHub, auto-deploys, free hobby.

### Heroku (Paid now)

`heroku create`, `git push heroku main`, Procfile `web: gunicorn app:app`.

**Security**: .env → Repo secrets/env vars on platform. Don't commit key.

Repo ready - commit/push!
