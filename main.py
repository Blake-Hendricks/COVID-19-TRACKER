#this program will track covid-19 total case numbers/deaths/recovery
#website: https://www.worldometers.info/coronavirus/
import requests
import bs4

import tkinter as tk

#function that will get covid-19 data from website when passed with a url, example demonstrated in the next function.
def get_html_data(url):
    #variable to retrieve get the html data out the url
    data = requests.get(url)
    #brings back the url at the end of the function
    return data

#function that will get the covid data from website when passed with the url
def get_covid_data():
    url = "https://www.worldometers.info/coronavirus/"
    #boom defined a variable to store the url

    #now define a variable that can call the function created above in order to retrieve the html datat from the url
    html_data = get_html_data(url)
    #get_covid_data(): will print and also make sure the html from the url was retreived with no error

    #create a variable that uses beautiful soup to parse(analyze) the html data |
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    #variable defined to find the specific class that the element/data belongs in (its knocking on each door)
    info_div = bs.find("div", {"class" : "content-inner"}).findAll("div", {"id" : "maincounter-wrap"})
    #print(info_div) so you can see what elements you need to grab text from to display cases
    #define empty string so you can later on define the active and recovered cases in it
    all_data = " "
    #search each block of info_div html and find number of active and recovered covid-19 cases
    for block in info_div:
        #grabbing the header "Coronavirus Cases" in h1
        text = block.find("h1",{"class": ""}).get_text()
        # grabbing the span "Case Count" number in span
        count = block.find("span",{"class" : ""}).get_text()
        all_data = all_data + text + " " + count + "\n"
    #print(all_data) to test
    return(all_data)

#function to get country data for each individual country (search function)
def get_country_data():
    name = textfield.get()
    #define new url. go to website and find the url that views specific country... /country/
    url = "https://www.worldometers.info/coronavirus/country/" + name #adding the inputted country name from the window at the end of the url
    #copy get_covid_data script into this script
    html_data = get_html_data(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
    info_div = bs.find("div", {"class" : "content-inner"}).findAll("div", {"id" : "maincounter-wrap"})
    all_data = " "
    for block in info_div:

        text = block.find("h1",{"class": ""}).get_text()

        count = block.find("span",{"class" : ""}).get_text()

        all_data = all_data + text + " " + count + "\n"
    #to show data inside of main label replaced this code with the return(all_data) functino
    mainlabel['text'] = all_data



#reload function to reload data from website
def reload():
    #define variable to re run get_covid_data
    new_data = get_covid_data()
    #save it to main label to show it in main label window
    mainlabel['text']=new_data


#run get covid function
get_covid_data()


#definition to open a window with tkinter.. building GUI
root= tk.Tk()
#set size of window
root.geometry("900x700")
#set title of window
root.title("Covid Tracker")
#font details
f = ("poppins", 25, "bold")
#add banner. copy and past it into your covid19tracker project
banner = tk.PhotoImage(file = "covid.png")
#set the banner
bannerlabel = tk.Label(root, image = banner)
#pack banner. get it ready
bannerlabel.pack()

#define a text field. Where user can enter a country name in the text field
textfield = tk.Entry(root, width = 50)
textfield.pack()

#need to show data inside of main window | text is going to display the covid data
mainlabel = tk.Label(root, text = get_covid_data(), font = f)
mainlabel.pack()

#make a get data button for when someone is searching for specific country details.. | copy and paste from reload button | change command definition to get_country_data
get_data_button = tk.Button(root, text = "Get Data", font=f, relief = 'solid', command=get_country_data)
get_data_button.pack()

#make reload button
reload_button = tk.Button(root, text = "Reload", font=f, relief = 'solid', command=reload)
reload_button.pack()

root.mainloop()
