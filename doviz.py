from flask import Flask,render_template,request
import requests

payload = {}
headers= {
  "apikey": "caCs4oow2BNkByMM51dUl1VnyHyxg9Q6"
}




app = Flask(__name__)
@app.route("/",methods = ["GET","POST"])
def index():
    if request.method == "POST":
        firstCurrency = request.form.get("firstCurrency") # USD
        secondCurrency = request.form.get("secondCurrency") # TRY

        amount = request.form.get("amount") # 15

        url = "https://api.apilayer.com/fixer/convert?to="+secondCurrency+"&from="+firstCurrency+"&amount="+ amount
        response = requests.request("GET", url, headers=headers, data = payload)
        
        app.logger.info(response)

        infos =  response.json()

        
        result = infos["result"]

        currencyInfo = dict()
        currencyInfo["firstCurrency"] = firstCurrency
        currencyInfo["secondCurrency"] = secondCurrency
        currencyInfo["amount"] = amount
        currencyInfo["result"] = result

        return render_template("index.html",info = currencyInfo)
    else:
        return render_template("index.html" )
if __name__ == "__main__":
    app.run(debug=True)