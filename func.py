def input_processing(text):
    
    res = " "
    if "place" and "order" in text:
        res = "CAN I STILL PLACE A NEW ORDER WITH AFLIN"
    elif (("return" and "product") or ("return" and "item")) in text:
        res = "CAN I RETURN OR EXCHANGE MY PRODUCT AT MY LOCAL AFLIN STORE"
    elif "support" in text:
        res = "CAN I GET GENIUS SUPPORT AT AN AFLIN STORE"
    elif "repair" in text:
        res = "WHAT’S THE STATUS OF MY REPAIR"
    elif "experience" in text:
        res = "CAN I HAVE EXPERIENCE AN AFLIN PRODUCT BEFORE BUYING IT"
    elif "covid measures" in text:
        res = "WHAT ARE THE COVID MEASURES TAKEN IN AFLIN STORES"
    elif "pickup" in text:
        res = "CAN I COME BY AND PICK UP A PRODUCT WITHOUT GOING INSIDE THE STORE"
    elif  "aflin stores" and "status" in text:
        res = "HOW DO I KNOW THE STATUS OF OFFLINE AFLIN STORES"
    elif "wait" and "line" in text:
        res = "WILL I HAVE TO WAIT IN LINE"
    elif "distancing" in text:
        res = "HOW IS PHYSICAL DISTANCING PRACTISED AT AFLIN STORE LOCATIONS"
    elif "wear" and "mask" in text:
        res = "WEAR A MASK"
    elif "covid vaccination" in text:
        res = "PROOF OF COVID 19 VACCINE"
    elif ("hi" or "hello" or "hey" )in text:
        res = "GREETINGS"
    else:
        res = "I am sorry to be not able to help you right at this moment." 
    return res




