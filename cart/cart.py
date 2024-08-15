from base.models import Product

class Cart():
    def __init__(self, request):
        self.session = request.session

        #get request
        self.request = request
        # get the current session key if it exists
        cart = self.session.get('session_key')

        # if thr user is new, no session key. If not create one
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        # makes url the cart is available on all pages of the site
        self.cart = cart


    
    def add(self, product, quantity):
        product_id = str(product.id)
        quantity_qty = str(quantity) 


        #logic
        if product_id in self.cart:
            pass
        else:
            # self.cart[product_id] = {'price':  str(product.price)}
            self.cart[product_id] = int(quantity_qty)


        self.session.modified = True


    def __len__(self):
        return(len(self.cart))
    




    def total(self):
        #get product ids
        product_id = self.cart.keys()
        products = Product.objects.filter(id__in= product_id)
        quantities = self.cart
        #start with 0
        t = 0
        for key, val in quantities.items():
            key = int(key)
            for prod in products:
                if prod.id == key:
                    t =  t + (prod.price * val)
                    

        return t


    def get_products(self):
        #get ids
        product_ids = self.cart.keys()   
        #look at the db
        products = Product.objects.filter(id__in=product_ids)
    
        return products
    

    

    def get_quantities(self):
        #get ids
        quantities = self.cart  
        return quantities
    

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        #update cart/dict
        self.cart[product_id] = product_qty

        self.session.modified = True
        # print("self.cart =", self.cart)
        return self.cart
    

    def delete(self, product):
        product_id = str(product)

        # delete from dict/cart
        if product_id in self.cart:
            del self.cart[product_id]
            # print("cart after deleted =", self.cart)

        self.session.modified = True