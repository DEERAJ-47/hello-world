#CHATBOT FOR AUTOMOBILE BY DEERAJ_ABHIMANYU


import pyttsx3
import speech_recognition as sr



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices') 
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

print('\t HELLO THERE THANKS FOR CONTACTING YCM MECHANIC \n')
speak('HELLO THERE.., THANKS FOR CONTACTING YCM MECHANIC WE ARE ALWAYS THERE TO HELP YOU ')


speak('PLEASE ENTER YOUR NAME HERE..')
name = input('PLEASE ENTER YOUR NAME HERE.. \n')
print('WELCOME',name + "\n",)


speak(" thanks for contacting us please select the category of your vehicle \n ")
print('ok',name + " thanks for contacting us please select the category of your vehicle \n ")

print(' 1.bike \n 2.auto \n 3.car \n 4.lorry \n')
speak(' NUMBER 1.bike \n NUMBER 2.auto \n NUMBER 3.car \n NUMBER 4.lorry \n')
a = int(input('please enter the category \n'))


    
if a == 1:
           
        print('thanks for selecting your categoey \n please select the problem you are facing from given below list \n')
        speak('thanks for selecting your categoey \n please select the problem you are facing from given below list')

        
        print(' 1.engine problem \n 2.breaking problem \n 3.electrical problem \n 4.high fuel consumption problem \n')
        speak(' 1.engine problem \n 2.breaking problem \n 3.electrical problem \n 4.high fuel consumption problem \n')
        p1 = int(input('please enter the number of the problem you are facing in given list \n'))

        if p1 == 1:
            print("so you are having engine problem \n please contact the engineer 2 days after in our mechanics \n contact number is 9999999999 \n")
            speak("so you are having engine problem \n please contact the engineer 2 days after in our mechanics \n contact number is 9999999999 \n")

        if p1 == 2:
            print("so you are having breaking problem \n please contact the engineer 3 days after in our mechanics \n contact number is 8888888888 \n")
            speak("so you are having breaking problem \n please contact the engineer 3 days after in our mechanics \n contact number is 8888888888 \n")
        if p1 == 3:
            print("so you are having electrical problem \n please contact the engineer 4 days after in our mechanics \n contact number is 7777777777 \n")
            speak("so you are having electrical problem \n please contact the engineer 4 days after in our mechanics \n contact number is 7777777777 \n")
        if p1 == 4:
            print("so you are having high fule consumption \n please contact the engineer 1 days after in our mechanics \n contact number is 6666666666 \n")
            speak("so you are having high fule consumption \n please contact the engineer 1 days after in our mechanics \n contact number is 6666666666 \n")
    
if a == 2:
            
            print('thanks for selecting your categoey \n please select the problem you are facing from given below list \n')
            speak('thanks for selecting your categoey \n please select the problem you are facing from given below list')
            
            print(' 1.gas problem \n 2.gear clutch problem \n 3.engine problem \n 4.breaking problem \n')
            speak(' 1.gas problem \n 2.gear clutch problem\n 3.engine problem \n 4.breaking problem \n')
            p2 = int(input('please enter the number of the problem you are facing in given list \n'))

            if p2 == 1:
                print("so you are having gas problem \n please contact the engineer 3 days after in our mechanics \n contact number is 5555555555  \n")
                speak("so you are having gas problem \n please contact the engineer 3 days after in our mechanics \n contact number is 5555555555  \n")
            if p2 == 2:
                print("so you are having gearclutch problem \n please contact the engineer 2 days after in our mechanics \n contact number is 4444444444 \n")
                speak("so you are having gearclutch problem \n please contact the engineer 2 days after in our mechanics \n contact number is 4444444444 \n")
            if p2 == 3:
                print("so you are having engine problem \n please contact the engineer 1 days after in our mechanics \n contact number is 3333333333 \n")
                speak("so you are having engine problem \n please contact the engineer 1 days after in our mechanics \n contact number is 3333333333 \n")
            if p2 == 4:
                print("so you are having breaking problem \n please contact the engineer 4 days after in our mechanics \n contact number is 2222222222 \n")
                speak("so you are having breaking problem \n please contact the engineer 4 days after in our mechanics \n contact number is 2222222222 \n")
    
if a == 3:
              print('thanks for selecting your categoey \n please select the problem you are facing from given below list \n')
              speak('thanks for selecting your categoey \n please select the problem you are facing from given below list')
              
              print(' 1.gearbox problem \n 2.clutch problem\n 3.turbo problem\n 4.brakes problem\n')
              speak(' 1.gearbox problem\n 2.clutch problem\n 3.turbo problem\n 4.brakes problem\n')
              
              p3 = int(input('please enter the number of the problem you are facing in given list \n'))

              if p3 == 1:
                 print("so you are having gearbox problem \n please contact the engineer 5 days after in our mechanics \n contact number is 1111111111 \n")
                 speak("so you are having gearbox problem \n please contact the engineer 5 days after in our mechanics \n contact number is 1111111111 \n")
              if p3 == 2:
                print("so you are having clutch problem \n please contact the engineer 4 days after in our mechanics \n contact number is 0000000000 \n")
                speak("so you are having clutch problem \n please contact the engineer 4 days after in our mechanics \n contact number is 0000000000 \n")
              if p3 == 3:
                print("so you are having turbo problem \n please contact the engineer 2 days after in our mechanics \n contact number is 9999999999 \n")
                speak("so you are having turbo problem \n please contact the engineer 2 days after in our mechanics \n contact number is 9999999999 \n")
              if p3 == 4:
                print("so you are having breakes problem \n please contact the engineer 1 days after in our mechanics \n contact number is 8888888888 \n")
                speak("so you are having breakes problem \n please contact the engineer 1 days after in our mechanics \n contact number is 8888888888 \n")
    
if a == 4:
              print('thanks for selecting your categoey \n please select the problem you are facing from given below list \n')
              speak('thanks for selecting your categoey \n please select the problem you are facing from given below list')
              
              print(' 1.engine over heating problem \n 2.starter failure problem \n 3.issues with wheels \n 4.break fluid problem \n')
              speak(' 1.engine over heating problem \n 2.starter failure \n 3.issues with wheels \n 4.break fluid problem \n')
              
              p4 = int(input('please enter the number of the problem you are facing in given list \n'))

              if p4 == 1:
                 print("so you are having engine over heat problem \n please contact the engineer 7 days after in our mechanics \n contact number is 7777777777 \n")
                 speak("so you are having engine over heat problem \n please contact the engineer 7 days after in our mechanics \n contact number is 7777777777 \n")
              if p4 == 2:
                 print("so you are having starter failure problem \n please contact the engineer 2 days after in our mechanics \n contact number is 6666666666 \n")
                 speak("so you are having starter failure problem \n please contact the engineer 2 days after in our mechanics \n contact number is 6666666666 \n")
              if p4 == 3:
                 print("so you are having issue with the wheels \n please contact the engineer 1 days after in our mechanics \n contact number is 5555555555 \n")
                 speak("so you are having issue with the wheels \n please contact the engineer 1 days after in our mechanics \n contact number is 5555555555 \n")
              if p4 == 4:
                 print("so you are having break fluid problem \n please contact the engineer 4 days after in our mechanics \n contact number is 4444444444 \n")
                 speak("so you are having break fluid problem \n please contact the engineer 4 days after in our mechanics \n contact number is 4444444444 \n")
    

print('THANKS FOR CONTACTING YCM MECHANICS \n HAVE A NICE DAY \n')
speak('THANKS FOR CONTACTING YCM MECHANICS \n HAVE A NICE DAY \n')




