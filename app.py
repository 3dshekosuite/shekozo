from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def home():
    if request.method == 'POST':
        airport_price = float(request.form.get('airport_price', 0))
        how_many_airports = float(request.form.get('how_many_airports', 0))
        sightseeing = float(request.form.get('sightseeing', 0))
        sightseeing_value = float(request.form.get('sightseeing_value', 0))
        other_transfers = float(request.form.get('other_transfers', 0))
        pax = float(request.form.get('pax', 0))
        guide = float(request.form.get('guide', 0))
        leader = float(request.form.get('leader', 0))
        cairo_accommodation = float(request.form.get('cairo_accommodation', 0))
        cairo_nights = float(request.form.get('cairo_nights', 0))
        luxor_accommodation = float(request.form.get('luxor_accommodation', 0))
        luxor_nights = float(request.form.get('luxor_nights', 0))
        aswan_accommodation = float(request.form.get('aswan_accommodation', 0))
        aswan_nights = float(request.form.get('aswan_nights', 0))
        hurghada_accommodation = float(request.form.get('hurghada_accommodation', 0))
        hurghada_nights = float(request.form.get('hurghada_nights', 0))
        cruise_accommodation = float(request.form.get('cruise_accommodation', 0))
        cruise_nights = float(request.form.get('cruise_nights', 0))
        lunch = float(request.form.get('lunch', 0))
        tickets = float(request.form.get('tickets', 0))
        flights = float(request.form.get('flights', 0))
        other_options = float(request.form.get('other_options', 0))

        total_price = calculate_price(
            airport_price, how_many_airports, sightseeing, sightseeing_value,
            other_transfers, pax, guide, leader, cairo_accommodation, cairo_nights,
            luxor_accommodation, luxor_nights, aswan_accommodation, aswan_nights,
            hurghada_accommodation, hurghada_nights, cruise_accommodation, cruise_nights,
            lunch, tickets, flights, other_options
        )
        return f'Price Per Pax: {total_price}'
    return render_template('index.html')

def calculate_price(
        airport_price, how_many_airports, sightseeing, sightseeing_value,
        other_transfers, pax, guide, leader, cairo_accommodation, cairo_nights,
        luxor_accommodation, luxor_nights, aswan_accommodation, aswan_nights,
        hurghada_accommodation, hurghada_nights, cruise_accommodation, cruise_nights,
        lunch, tickets, flights, other_options
    ):
    transfers = ((airport_price * how_many_airports) + (sightseeing * sightseeing_value) + other_transfers) / 20 / pax
    gratuities = ((guide * sightseeing) + leader) / 20 / pax
    accommodation = (cairo_accommodation * cairo_nights) + (luxor_accommodation * luxor_nights) + (aswan_accommodation * aswan_nights) + (hurghada_accommodation * hurghada_nights) + (cruise_accommodation * cruise_nights)
    expenses = (lunch + tickets) / 20
    total_price = flights + expenses + accommodation + gratuities + transfers
    total_price = total_price + (total_price * 0.35) + other_options
    return total_price


if __name__ == '__main__':
    app.run(debug=True)
