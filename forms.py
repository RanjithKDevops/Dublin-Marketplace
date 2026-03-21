from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FloatField, SubmitField
from wtforms.validators import DataRequired, Length, Email, NumberRange

class ListingForm(FlaskForm):
    title = StringField('Title', validators=[
        DataRequired(message="Please enter a title"),
        Length(min=3, max=100, message="Title must be between 3 and 100 characters")
    ])
    
    price = FloatField('Price (€)', validators=[
        DataRequired(message="Please enter a price"),
        NumberRange(min=0, message="Price must be 0 or greater")
    ])
    
    description = TextAreaField('Description', validators=[
        DataRequired(message="Please enter a description"),
        Length(min=10, max=500, message="Description must be between 10 and 500 characters")
    ])
    
    category = StringField('Category', validators=[
        DataRequired(message="Please enter a category"),
        Length(max=50, message="Category too long")
    ])
    
    contact_email = StringField('Contact Email', validators=[
        DataRequired(message="Please enter an email"),
        Email(message="Please enter a valid email address")
    ])
    
    location = StringField('Location', validators=[
        Length(max=100, message="Location too long")
    ])
    
    submit = SubmitField('Post Listing')
