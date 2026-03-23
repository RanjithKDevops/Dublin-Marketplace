from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, Listing
from forms import ListingForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///marketplace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    listings = Listing.query.order_by(Listing.created_at.desc()).all()
    return render_template('index.html', listings=listings)

@app.route('/listing/new', methods=['GET', 'POST'])
def new_listing():
    form = ListingForm()
    
    if form.validate_on_submit():
        listing = Listing(
            title=form.title.data,
            price=form.price.data,
            description=form.description.data,
            category=form.category.data,
            contact_email=form.contact_email.data,
            location=form.location.data or "Dublin"
        )
        
        db.session.add(listing)
        db.session.commit()
        flash('Your listing has been posted successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_listing.html', form=form)

@app.route('/listing/<int:id>')
def view_listing(id):
    listing = Listing.query.get_or_404(id)
    return render_template('listing_detail.html', listing=listing)

@app.route('/listing/<int:id>/edit', methods=['GET', 'POST'])
def edit_listing(id):
    listing = Listing.query.get_or_404(id)
    form = ListingForm()
    
    if form.validate_on_submit():
        listing.title = form.title.data
        listing.price = form.price.data
        listing.description = form.description.data
        listing.category = form.category.data
        listing.contact_email = form.contact_email.data
        listing.location = form.location.data
        
        db.session.commit()
        flash('Listing updated successfully!', 'success')
        return redirect(url_for('view_listing', id=listing.id))
    
    form.title.data = listing.title
    form.price.data = listing.price
    form.description.data = listing.description
    form.category.data = listing.category
    form.contact_email.data = listing.contact_email
    form.location.data = listing.location
    
    return render_template('edit_listing.html', form=form, listing=listing)

@app.route('/listing/<int:id>/delete', methods=['POST'])
def delete_listing(id):
    listing = Listing.query.get_or_404(id)
    db.session.delete(listing)
    db.session.commit()
    flash('Listing has been removed', 'info')
    return redirect(url_for('index'))

@app.route('/category/<category>')
def category(category):
    listings = Listing.query.filter_by(category=category).order_by(Listing.created_at.desc()).all()
    return render_template('index.html', listings=listings, current_category=category)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
