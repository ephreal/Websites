# Could this be PHP? Yes.
# Do I want to write PHP? No.
import json
import os

# Note to future self (2-4 days from 5/21/18):
# What confuses you here? Comment it.
# I'm not sure what is confusing at 
# the moment because I just wrote this
# and it makes perfect sense to me.
def product_html():
	prod_file = "../../json/product_list.json"
	prod_folder = "../../img/products"

	with open (prod_file, 'r') as f:
		all_products = json.loads(f.read())

	product_names = list(all_products.keys())
	product_names.sort()

	product_list = []
	products = []
	products.append('\n<article class="products">')

	for product in product_names:

		prod_id        = all_products[product]["id"]
		prod_desc      = all_products[product]["desc"]
		prod_packaging = all_products[product]["pack"]
		prod_weight    = all_products[product]["weight"]
		prod_area      = all_products[product]["imp_area"]
		prod_qty       = all_products[product]["quantities"]
		prod_price     = all_products[product]["prices"]
		prod_options   = all_products[product]["options"]
		prod_setup     = all_products[product]["setup_fee"]
		prod_items	   = os.listdir(f"{prod_folder}/{prod_id}")

		# Create a product ID that doesn't use '-'.
		# Using '-' screws up the ability to create a 
		# javascript variable out of it.
		img_id	 	   = f"img_{prod_id}".replace('-', '_')

		# Setup the initial product image
		html_block = f"""
		<input type="checkbox" id="{prod_id}">
		<section class="product" id="nav-{prod_id}">
			<label for="{prod_id}" class="controller">
				<div class="product-image">
					<figcaption class="product-name">
						{product}
					</figcaption>
					<figure>
						<img id="{img_id}" src="img/products/{prod_id}/{prod_items[0]}" alt="{product}">
					</figure>
				</div>
			</label>
			<aside class="product-info">"""

		# Add in some buttons and javascript if there
		# is more than one picture for the product
		if len(prod_items) > 1:
			# Create the filepaths for javascript
			prod_items = [f"img/products/{prod_id}/{item}" for item in prod_items]
			# Add buttons/javascript
			html_block += f"""
				<p class="alt_img_txt">Available Colors:</p>
	        	<div class="img_options">
	         		<button class="img_button" onclick="{img_id}_index = prev_img('{img_id}', {img_id}_array, {img_id}_index)">Prev</button>
	        		<button class="img_button" onclick="{img_id}_index = next_img('{img_id}', {img_id}_array, {img_id}_index)">Next</button>
	        	</div>
				<script>
					var {img_id}_index = 0;
					var {img_id}_array = {prod_items};
				</script>
				"""

		# Add in anything to do with product description
		html_block += f"""
				<p>
					{prod_desc}
				</p>
				<p>
					<strong>Packaging: </strong>{prod_packaging}</br>
					<strong>Weight: </strong>{prod_weight}</br>
					<strong>Imprint Area: </strong>{prod_area}</br>
					<strong>Product Code: </strong>{prod_id}
				</p>
				<section class=prod-pricing>
					<div class="prod-quantity-cell" align="center">QTY</div>
					<div class="prod-price-cell" align="center">PRICE</div>
			"""

		# Create the product amounts and prices chart
		for i in range(0, len(prod_qty)-1):
			qty = prod_qty[i]
			price = prod_price[i]
			html_block += f'\n\t\t\t\t<div class="prod-quantity-cell" align="center">{qty}</div>'
			html_block += f'\n\t\t\t\t<div class="prod-price-cell" align="center">${price}</div>'

		# Close out the section, put in any
		# additional options, close out the
		# product html block.
		html_block += f"""
				</section>
				<p class="prod_options">
					{prod_options}
				</p>
				<p>
					Setup Fee ${prod_setup} (V)
				</p>
			</aside>
		</section>"""
		# Add the html to the product list
		products.append(html_block)

	# Close out article tag
	products.append("\n</article>")

	return products

def product_menu():

	prod_file = "../../json/product_list.json"
	prod_folder = "../../img/products"

	with open (prod_file, 'r') as f:
		all_products = json.loads(f.read())

	product_names = list(all_products.keys())
	product_names.sort()

	product_list = []

	for product in product_names:
		prod_id = all_products[product]["id"]

		# Create menu options
		product_list.append(f'\t\t\t<li class="prod-list-entry"><a href="#nav-{prod_id}">{product}</a></li>\n')

	return product_list


print("".join(product_html()))
print("".join(product_menu()))