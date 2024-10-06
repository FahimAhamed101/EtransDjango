from django.shortcuts import render
from store.models import Product
from category.models import banner,Category
from cart.models import CartItem


from category.models import banner,banneractive,bannertwo
from blog.models import Post

def home(request):
    products = Product.objects.order_by('-created_date').filter(is_available=True,Is_featured=True)
    products_new = Product.objects.order_by('-created_date').filter(is_available=True)
    
    category = Category.objects.all()
    
 
    posts = Post.objects.filter(status='published') 
    bannerstwo = bannertwo.objects.filter(is_selected =True).order_by('id') 
    banners = banner.objects.filter(is_selected =True).order_by('id')
    banneractives = banneractive.objects.filter(is_selected =True).order_by('id')
    
    """ user = request.user
    if user.is_active == True:
        cart_count = CartItem.objects.filter(user=request.user,is_active=True).count()
    else:
        cart_count = 0
'cart_count':cart_count,
    print(cart_count)
    print(banners)"""
    
    


    context = {
        'bannertwo':bannerstwo,
'products_new':products_new,
        'category':category,
      
        'products': products,
        'banners':banners,
        'banneractive':banneractives,
        'posts':posts,

    }
    
    return render(request,'home.html',context)


