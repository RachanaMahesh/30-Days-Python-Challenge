# requests[HTTP for Humans] library allows us to easily make http requests to get information from website. pip install requests
# requests library is good o fetch the info from the website but for parsing we need to use beautifulsoup.

import requests
#--------------------------------- 1. to fetch the source code from the browser -------------------------
# r = requests.get("https://xkcd.com/353/")
# print(r)
# print(dir(r))
# print(help(r)) # to get detailed explaination 
# print(r.status_code)
# print(r.text)

#---------------------- 2. to download an image from the browser -----------------------
# r = requests.get("https://imgs.xkcd.com/comics/python.png")
# with open("RequestsDowloadImage", 'wb') as wf:
#     wf.write(r.content)

## Status Code : 200 - are success, 300- redirects, 400 - client errors(when tries to aceess we might not have permission ), 500- Server Error
# print(r.ok) # retuens Truew for 200 & 300 but return False if the status code is other than 200 & 300

#------ 3. httpbin-Get route Eg:lets say we want to do get requests on a route that has some URL parameters, we r going to use httpbin get-route to test this, the way he had set the site up is that - httpbin is going to respond with the json information of what we have sent in the requests.
# httpbin.org : will show the different routes available to us & we can test http methods like get,post,puy,delete, we can test redirects & we can test authentication
# r = requests.get("https://httpbin.org/get?page=2&count=20") # adding parameters(?page=2&count=20) directly into URL can be prone to mistakes.
# print(r.headers)
# print(r.text)

# paylod = {'page':2, 'count':20}
# r = requests.get("https://httpbin.org/get", params=paylod) 
# print(r.text)
# print(r.url) # to check if the library created the correct URL  

# -----------------4.  To post form - data to the route -------------------------
# paylod = {'username':'Rachu','password':'testing'}
# r = requests.post("https://httpbin.org/post", data=paylod) 
# # print(r.text) # Output: No args but we have data in form data,  "json": null,
# #since we r getting data in json format we can use json instead of r.text
# r_dict = r.json() # it created python dictionary from the json response
# # if we r usibg json() in python then it's equal to importing json module & using json.load(s) on response text
# print(r_dict['form'])

# ------------- 5. Put requests form - data to the route -----------------------------------
# if we r performing login then not all of them were done through form based authentication some of them are done through basic authentication. 
# if we need to pass crendentials through basic authentication then requests can do that as well by specifying the crendentials in the URL that u want to test against
# eg: https://httpbin.org/basic-auth/Rachu/testing - if we provide the correct credentials in the popup then it redirects to the page where {"authenticated": true, "user": "Rachu"}

r = requests.get("https://httpbin.org/basic-auth/Rachu/testing", auth=("Rachu","testing"))
# print(r.text)
print(r)
r = requests.get("https://httpbin.org/basic-auth/Rachu/testing", auth=("RachanaMahesh","testing"))
# print(r.text) # No response as the credentials we passed are wrong
print(r)


#---------------------- 6. set a timeout if the website won't respond within an acceptable amount of time----------
r = requests.get("https://httpbin.org/delay/1", timeout=3)
print(r)
r = requests.get("https://httpbin.org/delay/6", timeout=3)
print(r) # ReadTimeout Exception
# It's always good to add timeout for all the requests unless we r getting the requests from API that is doing lot of computation & expected to take a long time