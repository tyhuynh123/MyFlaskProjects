from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = '\xf5!\x07!qj\xa4\x08\xc6\xf8\n\x8a\x95m\xe2\x04g\xbb\x98|U\xa2f\x03'


@app.route("/")
def show_index():

    # set up a new game by setting guess count to 0, and
    # setting a random number
    rand_num = random.randint(0, 100)
    session['rand_num'] = rand_num
    print "The answer is: ", rand_num
    session['count'] = 0
    
    return render_template("index.html")

@app.route("/result")
def check_guess():
    
    guess = int(request.args.get("guess"))
    # print "the guess is: ",guess
    # print "the type of the guess is:", type(guess)

    rand_num = session['rand_num']
    # print "random number from check_guess is:", rand_num
    # print "the type of the randome number is:", type(rand_num)

    if session['count'] < 10:

        if guess == rand_num:
            return render_template("result.html", 
                                    response='Hooray! You win.',
                                    count=session['count'])

        else:

            print guess, "!=", rand_num
            session['count'] += 1
            if guess > rand_num:
                return render_template("result.html", 
                                    response='Too high. Try again!',
                                    count=session['count'])
            elif guess < rand_num:
                return render_template("result.html", 
                                    response='Too low. Try again!',
                                    count=session['count'])
        
    else:
        return render_template("result.html",
                            response='You lose.')


if __name__ == '__main__':

    app.run(debug=True)



###### TESTING CODE ########
