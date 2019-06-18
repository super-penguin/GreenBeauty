from google_images_download import google_images_download
response = google_images_download.googleimagesdownload()   #class instantiation


###############################
# Problematic ingredients:
# https://globalnews.ca/news/3383851/11-skincare-ingredients-to-avoid-during-pregnancy/

Ing_List = ["retinol", "oxybenzone", "avobenzone", "salicylic acid", "hydroquinone"]


############### The product contain Retinol
# HEALTH CONCERNS: Cancer (Possible), Developmental and reproductive toxicity. More
# VULNERABLE POPULATIONS: All
KeyWords = ["DRUNK ELEPHANT A-Passioni™ Retinol Cream", "SUNDAY RILEY Luna Retinol Sleeping Night Oil", "SUNDAY RILEY A+ High-Dose Retinol Serum", "MURAD Retinol Youth Revewal Night Cream", "MURAD Retinol Youth Revewal Serum", "FAB Skin Lab Retinol Eye Cream with Triple Hyaluronic Acid", "DR. DENNIS GROSS SKINCARE Ferulic Acid + Retinol Brightening Solution", "DR. DENNIS GROSS SKINCARE Ferulic + Retinol Anti-Aging Moisturizer", "MURAD Retinol Youth Revewal Eye Serum", "PETER THOMAS ROTH Retinol Fusion PM", "DR. DENNIS GROSS SKINCARE Ferulic + Retinol Wrindle Recovery Overnight Serum", "CLINIQUE Fresh Pressed Clinical Daily+Overnight Boosters with Pure Vitamin C 10% + A (Retinol)", "THE ORDINARY Granactive Retinoid 2% Emulsion", "PETER THOMAS ROTH Professional 3% Retinoid Plus"]

for word in KeyWords:
    keyword = word + " home shelfie"
    arguments = {"keywords": keyword,"limit":50,"print_urls":True}   #creating list of arguments
    paths = response.download(arguments)


############### The product contain Titanium dioxide
# HEALTH CONCERNS: The International Agency for Research on Cancer designates TiO2 as a carcinogen, largely due to studies that have found increased lung cancers due to inhalation exposure in animals.
# VULNERABLE POPULATIONS: Everyone

KeyWords = ["clinique even better makeup broad spectrum spf 15", "smashbox camera ready BB cream SPF 35", "josie maran argan daily moisturizer spf 47", "coola mineral body sunscreen SPF 50", "SHISEIDO Synchro Skin Lasting Liquid Foundation Broad Spectrum SPF 20", "DR. JART+ Premium Beauty Balm SPF 45", "THE ORDINARY Mineral UV Filters SPF 30 with Antioxidants", "TOM FORD Traceless Perfecting Foundation Broad Spectrum SPF 15", "EVE LOM Daily Protection Anti-aging Broad Spectrum SPF 50 Sunscreen"]

for word in KeyWords:
    keyword = word + " home shelfie"
    arguments = {"keywords": keyword,"limit":50,"print_urls":True}   #creating list of arguments
    paths = response.download(arguments)

######################################################################
############### All the sunscreen contain oxybenzone
#

KeyWords = ["Neutrogena Ultra Sheer Sunscreen Lotion", "Neutrogena Ultra Sheer Dry-Touch Sunscreen Lotion", "Banana Boat Clear UltraMist Ultra Defense MAX Skin Protect Continuous Spray Sunscreen", "Coppertone Sport High Performance AccuSpray Sunscreen", "Coppertone Sport High Performance Clear Continuous Spray Sunscreen", "Neutrogena Fresh Cooling Sunscreen Body Mist", "Banana Boat Sport Performance Sunscreen Lotion", "Coppertone Sport High Performance Sunscreen Lotion", "NO-AD Sunscreen Lotion", "Ocean Potion Protect & Nourish Sunscreen Lotion", "KIEHL'S Super Fluid Daily UV Defense Sunscreen Broad Spectrum SPF 50+", "PETER THOMAS ROTH Max Sheer All Day Moisture Defense Lotion SPF 30 Sunscreen Lotion", "SHISEIDO Future Solution LX Total Protective Cream Broad Spectrum SPF 20 Sunscreen", "CLARINS Sunscreen Multi-Protection Broad Spectrum SPF 50"]

for word in KeyWords:
    keyword = word + " home shelfie"
    arguments = {"keywords": keyword,"limit":50,"print_urls":True}   #creating list of arguments
    paths = response.download(arguments)


######################################################################
############### The sunscreen contain avobenzone

KeyWords = ["CLINIQUE Superdefense SPF 20 Daily Defense Moisturizer Very Dry to Dry Combination", "COOLA Classic Body SPF 50- Guava Mango", "PHILOSOPHY Renewed Hope in A Jar SPF 30 Moisturizer", "MARIO BADESCU Oil Free Moisturizer Broad Spectrum SPF 30", "CLINIQUE Superdefense SPF 20 Daily Defense Moisturizer Combination Oily to Oily", "COVER FX SPF 30 Booster Drops Broad Spectrum Sunscreen", "BEAUTYBLENDER Selfie Shield™ Broad Spectrum SPF 38 Dry Oil Primer", "OBAGI CLINICAL Vitamin C Suncare Broad Spectrum SPF 30 Sunscreen"]

for word in KeyWords:
    keyword = word + " home shelfie"
    arguments = {"keywords": keyword,"limit":50,"print_urls":True}   #creating list of arguments
    paths = response.download(arguments)

######################################################################
############### The products contain salicylic acid

KeyWords = ["DRUNK ELEPHANT T.L.C. Framboos™ Glycolic Resurfacing Night Serum", "DRUNK ELEPHANT T.L.C. Sukari Babyfacial™ 25% AHA + 2% BHA Mask", "THE ORDINARY AHA 30% + BHA 2% Peeling Solution", "GLAMGLOW SUPERMUD Activated Charcoal Treatment Mask", "THE ORDINARY Salicylic Acid 2% Solution", "FARMACY HONEYMOON GLOW AHA Resurfacing Night Serum with Hydrating Honey + Gentle Flower Acids", "DERMALOGICA Daily Microfoliant Exfoliator", "OLEHENRIKSEN Balancing Force™ Oil Control Toner", "ORIGINS GinZing™ Energy-Boosting Gel Moisturizer", "SUNDAY RILEY U.F.O. Ultra-Clarifying Face Oil", "KATE SOMERVILLE ExfoliKate Intensive Exfoliating Treatment"]
for word in KeyWords:
    keyword = word + " home shelfie"
    arguments = {"keywords": keyword,"limit":50,"print_urls":True}   #creating list of arguments
    paths = response.download(arguments)


######################################################################
############### The products contain hydroquinone

KeyWords = ["MURAD Rapid Age Spot and Pigment Lightening Serum", "MURAD Post-Acne Spot Lightening Gel"]
for word in KeyWords:
    keyword = word + " home shelfie"
    arguments = {"keywords": keyword,"limit":50,"print_urls":True}   #creating list of arguments
    paths = response.download(arguments)
