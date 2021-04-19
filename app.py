from flask import Flask, render_template, url_for
import stripe


app = Flask(__name__)

app.config['STRIPE_PUBLIC_KEY'] = STRIPE_PUBLIC_KEY
app.config['STRIPE_SECRET__KEY'] = STRIPE_SECRET_KEY

stripe.api_key = app.config['STRIPE_SECRET__KEY']

@app.route('/')
def index():
    '''
    session = stripe.checkout.Session.create(
        payment_method_types = ['card'],
        line_items = [{
            'price': 'price_1IggsXE0oC5drW2atUduSzC8',
            'quantity': 1,
        }],
        mode = 'payment',
        success_url =url_for('thanks', _external=True) + '?session_id="{CHECKOUT_SESSION_ID}"',
        cancel_url = url_for('index', _external=True),
    )
    '''
    return render_template(
        'checkout.html', 
        #checkout_session_id=session['id'], 
        #checkout_public_key=app.config['STRIPE_PUBLIC_KEY']
    )
    

@app.route('/stripe_pay')
def stripe_pay():
    session = stripe.checkout.Session.create(
        payment_method_types = ['card'],
        line_items = [{
            'price': 'price_1IggsXE0oC5drW2atUduSzC8',
            'quantity': 1,
        }],
        mode = 'payment',
        success_url =url_for('thanks', _external=True) + '?session_id="{CHECKOUT_SESSION_ID}"',
        cancel_url = url_for('index', _external=True),
    )
    return {
        'checkout_session_id': session['id'], 
        'checkout_public_key': app.config['STRIPE_PUBLIC_KEY']
    }


@app.route('/thanks')
def thanks():
    return render_template('thanks.html')


if __name__ == '__main__':
    app.run(debug=True)