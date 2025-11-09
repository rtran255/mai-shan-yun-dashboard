# Mai Shan Yun — Inventory Intelligence Dashboard

## Description
A modern interactive dashboard using Plotly Dash to analyze and visualize restaurant inventory data.
Styled in black, white, and Aggie maroon for a Texas A&M and Mai Shan Yun fusion aesthetic.

---

## Deployment (Render)

1. Push this repo to GitHub.
2. Create a new **Web Service** on [Render](https://render.com/).
3. Connect your repo.
4. Use the following settings:
   - Environment: Python 3
   - Start Command: `gunicorn app:server`
   - Port: 8080
5. Deploy!

Your dashboard will be live after build.

---

## Local Development

```bash
python -m venv venv
source venv/bin/activate  # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt
python app.py
