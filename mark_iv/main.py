import aiml


kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

def response(k):
    response1 = kernel.respond(k)
    return response1

 
while True:
    input_text = input("User   : ")
    try:
        print("Hexa:   ",response(input_text.upper()))
    except NoMatchFound:
        print("Hexa:   Sorry.. couldnt process that!", )
