from flask import Flask, render_template, redirect, request, url_for
from Models.item_report import ItemReport,LostReport, FoundReport
from database import add_report, get_all_reports



# b = LostReport(
#     last_seen_date = "12-Oct-2026",
#     report_id = 123,
#     title = "Lost Bag", 
#     description ="lost leather bag in mall near a shop", 
#     category ="Bags", 
#     location = "near Dr.Fixit", 
#     date = "12-Oct-2026",
# )


# c = FoundReport(
#     found_date = "18-Oct-2026",
#     condition = "As was when lost",
#     report_id = 123,
#     title = "Lost Bag", 
#     description ="lost leather bag in mall near a shop", 
#     category ="Bags", 
#     location = "near Dr.Fixit", 
#     date = "12-Oct-2026"
# )


# print(b.get_details())
# print("\n Hello \n")
# print(c.get_details())




app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report/lost", methods = ["GET", "POST"])
def lost_item_report():
    if request.method == "POST":
        item_title = request.form.get("item_title")
        item_description = request.form.get("item_description")
        item_category = request.form.get("item_category")
        lost_location = request.form.get("lost_location")
        last_seen_location = request.form.get("last_seen_location")
        print(item_title)
        print(item_description)
        print(item_category)
        print(lost_location)
        print(last_seen_location)

        return render_template("lost_report.html")

    if request.method == "GET":
        return render_template("lost_report.html")

@app.route("/report/found")
def found_item_report():
    return render_template("found_report.html")


if __name__ == "__main__":
    app.run(debug = True)