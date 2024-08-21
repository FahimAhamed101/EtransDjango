from django import forms
from .models import Product
from django import forms
from .models import ReviewRating
#form for product management
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product

        fields= ['product_name','description','price','image1','image2','image3','stock','category','is_available',]



class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']     
        
        