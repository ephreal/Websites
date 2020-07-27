# /bin/python
# Auto updater for the website. 
# Simply place the pictures in
# their folders, update the json
# file, and run this script.
#
# Conglaggerations. You have 
# updated the website.

import product_formatter

html = "".join(product_formatter.product_html())
prod_list = "".join(product_formatter.product_menu())

# Open the products.html
with open("../../products.html", 'r') as f:
	prod_html = f.read()

# We'll update the list first

# Figure out where the list nav is
start = prod_html.index('id="prod_list"')
# This is a terrible way to search
# for the end.... but... oh well.
# It's good enough for now.
end = prod_html.index('</nav>\n\n<!--')

# We want to replace all li elements inside the nav>ul
to_replace = prod_html[start+45:end-12]

prod_html = prod_html.replace(to_replace, prod_list)


# Figure out where the article tag starts and closes
start = prod_html.index("<article class=\"products\">")
end = prod_html.index('</article>')

# we want to replace everything from start of
# article tag, to the end of the article tag.
to_replace = prod_html[start:end+10]

prod_html = prod_html.replace(to_replace, html)

# Update the html file
with open("../../products.html", 'w') as f:
	f.write(prod_html)

