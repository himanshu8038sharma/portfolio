# Himanshu Sharma - Portfolio
 portfolio built with Python and Streamlit.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Customize

- Edit the CONFIG block at the top of `app.py` (email, LinkedIn, repo links, certificate links).
- Add project screenshots to `assets/projects/<project-slug>/` (png, jpg, webp). The first image is the cover; the rest go in "More screenshots".
- Add your resume as `assets/resume.pdf` to show a download button.

## Deploy

Push to GitHub, then create an app on Streamlit Community Cloud pointing at `app.py`.
