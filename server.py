import os
from flask import Flask , render_template, request
app=Flask(__name__)


def evaluate_form(f):
    info_list = []
    count = 0
    for x,y in f.items():
        if x=="usr":
            info_list.append(["Your Name:", y])
        elif x in ["snork", "beach", "food", "nature", "walking"]:
            info_list.append(["Interest:", y])
        elif x=="optradio":
            info_list.append(["Your age:", y])
        elif x=="comment":
            info_list.append(["Your comment:", y])
        elif x=="remember":
            info_list.append(["", "We'll remember you"])
        print("{},{}".format(x,y))
        count +=1
    for x,y in info_list:
        print("{},{}".format(x,y))
    errors = []
    errors.append("Please attend to the following errors before this form can be submitted")
    errors.append("You have not supplied a valid name")
    return True, info_list


@app.route('/')
def main_index():
    return render_template('index.html')


@app.route('/places')
def places():
    return render_template('places.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/contactone', methods=["GET", "POST"])
def contactone():
    if request.method == "POST":
        myform = request.form
        response = evaluate_form(myform)
        if response[0] is True:
            return render_template('success.html', formdata=response[1])
        else:
            return render_template('contact_one.html', errorlist=response[1])
    else:
        return render_template('contact_one.html')


if __name__ == '__main__':
   app.run(debug=True)