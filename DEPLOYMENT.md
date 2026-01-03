# 🚀 Deployment Guide - Step by Step

## Step 1: Push to GitHub

### 1.1 Initialize Git Repository (if not already done)

Open terminal in your project folder and run:

```bash
cd C:\Users\adity\OneDrive\Desktop\currency_converter
git init
```

### 1.2 Create .env File (for local development)

Create a `.env` file in the project root:

```
EXCHANGE_RATE_API_KEY=your_api_key_here
```

**Note:** This file is already in `.gitignore`, so it won't be committed to GitHub.

### 1.3 Add Files to Git

```bash
git add .
```

### 1.4 Commit Files

```bash
git commit -m "Initial commit: Currency Converter by Aditya Jaiswal"
```

### 1.5 Create GitHub Repository

1. Go to [GitHub.com](https://github.com) and sign in
2. Click the **"+"** icon in the top right → **"New repository"**
3. Repository name: `currency-converter` (or any name you prefer)
4. Description: `Currency Converter by Aditya Jaiswal - Real-time exchange rate calculator`
5. Choose **Public** (so others can see it)
6. **DO NOT** check "Initialize with README" (we already have one)
7. Click **"Create repository"**

### 1.6 Connect and Push to GitHub

GitHub will show you commands. Run these in your terminal:

```bash
git remote add origin https://github.com/YOUR_USERNAME/currency-converter.git
git branch -M main
git push -u origin main
```

Replace `YOUR_USERNAME` with your actual GitHub username.

**If you get authentication errors:**
- Use GitHub Personal Access Token instead of password
- Or use GitHub Desktop app (easier for beginners)

## Step 2: Deploy to Render (Recommended)

### 2.1 Sign Up

1. Go to [render.com](https://render.com)
2. Click **"Get Started for Free"**
3. Sign up with GitHub (easiest option)

### 2.2 Create Web Service

1. Click **"New +"** → **"Web Service"**
2. Connect your GitHub account (if not already connected)
3. Select your `currency-converter` repository
4. Click **"Connect"**

### 2.3 Configure Service

Fill in the details:

- **Name**: `currency-converter` (or any name)
- **Region**: Choose closest to you
- **Branch**: `main`
- **Root Directory**: (leave empty)
- **Runtime**: `Python 3`
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `gunicorn main:app`

### 2.4 Set Environment Variable

**IMPORTANT:** Before deploying, set your API key:

1. Scroll down to **"Environment Variables"** section
2. Click **"Add Environment Variable"**
3. Key: `EXCHANGE_RATE_API_KEY`
4. Value: `your_api_key_here` (your actual API key)
5. Click **"Save Changes"**

### 2.5 Deploy

1. Scroll to bottom
2. Click **"Create Web Service"**
3. Wait 2-5 minutes for deployment
4. Your site will be live at: `https://currency-converter.onrender.com` (or your chosen name)

### 2.6 Update Structured Data URL

After deployment, update the URL in `index.html`:

1. Go to your GitHub repository
2. Edit `index.html`
3. Find line ~35: `"url": "https://your-site-url.com"`
4. Replace with your actual Render URL: `"url": "https://currency-converter.onrender.com"`
5. Commit and push (Render will auto-deploy)



## Step 5: Submit to Search Engines (Optional)

### Google Search Console

1. Go to [Google Search Console](https://search.google.com/search-console)
2. Add your property (your website URL)
3. Verify ownership
4. Submit sitemap: `https://your-site-url.com/sitemap.xml`

### Bing Webmaster Tools

1. Go to [Bing Webmaster Tools](https://www.bing.com/webmasters)
2. Add your site
3. Verify ownership
4. Submit sitemap

## 🎉 You're Live!

Your currency converter is now:
- ✅ On GitHub (for portfolio/showcase)
- ✅ Live on the internet (accessible to everyone)
- ✅ Secure (API key not exposed)
- ✅ SEO optimized

## 📝 Next Steps

1. **Share on Social Media**
   - LinkedIn post about your project
   - Twitter/X announcement
   - Add to GitHub profile

2. **Add to Portfolio**
   - Link from your personal website
   - Include in resume

3. **Monitor Performance**
   - Check Render/Railway dashboard for usage
   - Monitor API usage from Exchange Rate API

## 🆘 Troubleshooting

**Deployment fails:**
- Check that `requirements.txt` has all dependencies
- Verify environment variable is set correctly
- Check deployment logs in Render/Railway dashboard

**Site shows error:**
- Verify API key is correct in environment variables
- Check that API key has not exceeded rate limits
- Review application logs

**Can't push to GitHub:**
- Make sure you're authenticated (use Personal Access Token)
- Verify repository name is correct
- Try using GitHub Desktop app

## 🔗 Quick Links

- [Render Dashboard](https://dashboard.render.com)
- [Railway Dashboard](https://railway.app/dashboard)
- [GitHub](https://github.com)
- [Exchange Rate API](https://www.exchangerate-api.com/)

---

**Need help?** Check the README.md or open an issue on GitHub!

