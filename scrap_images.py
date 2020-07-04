#scraping images urls using selenium

def scrap_image_url(driver):
    images=driver.find_elements_by_xpath("//img[@class='_3togXc']")
    brands=driver.find_elements_by_xpath("//div[@class='_2B_pmu']")
    product_description =driver.find_elements_by_xpath("//div[@class='_2mylT6']/a[1]")
    prices=driver.find_elements_by_xpath("//a[@class='_1uv9Cb']//div[@class='_1vC4OE']")

    product_data={}
    product_data['image_urls']=[]
    product_data['product_description']=[]
    product_data['brands']=[]
    product_data['prices']=[]

    for image in images:
        source=image.get_attribute('src')
        product_data['image_urls'].append(source)

    for brand in brands:
        product_data['brands'].append(brand.text)

    for  prod_desr in product_description:
        product_data['product_description'].append(brand.text)

    for  prices in prices:
        product_data['prices'].append(price.text)

    print('Returning Scraped Data')

    return product_data
        

        
        
    
    
    
