from base.models import Product

class Wishlist():
    def __init__(self, request):
        self.session = request.session

        #get request
        self.request = request
        # get the current session key if it exists
        wish = self.session.get('session_key')

        # if the user is new, no session key. If not create one
        if 'session_key' not in request.session:
            wish = self.session['session_key'] = {}
        else:
            wish = self.session['session_key']

        # makes url the wish is available on all pages of the site
        self.wish = wish


    
    def add(self, product, quantity):
        product_id = str(product.id)
        quantity_qty = str(quantity) 


        #logic
        if product_id in self.wish:
            pass
        else:
            # self.wish[product_id] = {'price':  str(product.price)}
            self.wish[product_id] = int(quantity_qty)


        self.session.modified = True


    def __len__(self):
        return(len(self.wish))
    




    def total(self):
        #get product ids
        product_id = self.wish.keys()
        products = Product.objects.filter(id__in= product_id)
        quantities = self.wish
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
        product_ids = self.wish.keys()   
        #look at the db
        products = Product.objects.filter(id__in=product_ids)
    
        return products
    

    

    def get_quantities(self):
        #get ids
        quantities = self.wish  
        return quantities
    

    def update(self, product, quantity):
        product_id = str(product)
        product_qty = int(quantity)

        #update wish/dict
        self.wish[product_id] = product_qty

        self.session.modified = True
        # print("self.wish =", self.wish)
        return self.wish
    

    def delete(self, product):
        product_id = str(product)

        # delete from dict/wish
        if product_id in self.wish:
            del self.wish[product_id]
            # print("wish after deleted =", self.wish)

        self.session.modified = True



        