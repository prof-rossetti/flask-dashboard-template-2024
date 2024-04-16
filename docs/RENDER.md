# Deploying to Render

# Resources

  + https://render.com/docs/deploy-flask

## Repo Setup

Ensure the `gunicorn` package is listed in the "requirements.txt" file and commit and push before moving forward.

## Render Setup

Login to [render](https://dashboard.render.com) and visit the dashboard.

Create a New Web Service. Specify the GitHub repo URL via "Public Git repository" option at the bottom.

Specify start command:

```
gunicorn "web_app:create_app()"
```

Choose instance type of "free".

Set environment variables (see README, omit quotes for the values):
  + `ALPHAVANTAGE_API_KEY`


Click "Create web service" and wait a few moments as your code is deployed.
