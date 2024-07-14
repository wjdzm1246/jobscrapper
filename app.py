
from flask import Flask, render_template, request, redirect, send_file
import extractor.wanted_scrapper
from file import save_to_file

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("home.html", name="sunah")

@app.route("/search")
def search():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword in db:
        jobs = db[keyword]
    else:    
        jobscrapper=extractor.wanted_scrapper.job_scrapper()
        jobs = jobscrapper.scrapping(keyword)
        db[keyword] = jobs
    return render_template("search.html", keyword=keyword, jobs=jobs)

@app.route("/export")
def export():
    keyword = request.args.get("keyword")
    if keyword == None:
        return redirect("/")
    if keyword not in db:
        return redirect(f"/search?keyword={keyword}")
    save_to_file(keyword, db[keyword])
    return send_file(f"{keyword}.csv", as_attachment=True)

app.run("0.0.0.0")
'''
from extractor.wanted_scrapper import job_scrapper
from file import save_to_File

keyword = input("What do you want to search for?")

scrapper = job_scrapper()
jobs = scrapper.scrapping(keyword)
save_to_file(keyword, jobs)
'''
