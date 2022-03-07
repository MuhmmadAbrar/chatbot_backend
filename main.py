import aiml
import func

kernel = aiml.Kernel()
kernel.learn("std-startup.xml")
kernel.respond("load aiml b")

def response(k):
    response1 = kernel.respond(k)
    return response1

 
while True:
    input_text = input("User   : ")
    k = func.input_processing(input_text.lower())
    print("Hexa:   ",response(k))
