print("Title of program: Encouragement bot")
print()
while True:
  description = input("how are you feeling?")

  list_of_words = description.split()

  feelings_list = []
  encouragement_list = []
  counter = 0
  
  for each_word in list_of_words:
    
    if each_word == "sad":
      feelings_list.append("sad")
      encouragement_list.append("that things will get better!!")
      counter += 1
    if each_word == "happy":
      feelings_list.append("happy")
      encouragement_list.append("to keep smiling")
      counter += 1
    if each_word == "tired":
      feelings_list.append("tired")
      encouragement_list.append("that you will make it through !")
      counter += 1
    if each_word == "angry":
      feelings_list.append("angry")
      encouragement_list.append("things will get easier!")
      counter += 1
      
  if counter == 0:
    
      output = "sorry, I don't really understand. try using different words instead!"

  elif counter == 1:
    
      output = "ahh it seems that you are feeling quite " + feelings_list[0] + ". still, do remember "+ encouragement_list[0] + "! i hope you feel better ^^"  

  else:

    feelings = ""    
    for i in range(len(feelings_list)-1):
      feelings += feelings_list[i] + ", "
    feelings += "and " + feelings_list[-1]
    
    encouragement = ""    
    for j in range(len(encouragement_list)-1):
      encouragement += encouragement_list[i] + ", "
    encouragement += "and " + encouragement_list[-1]

    output = "It seems that you are feeling quite " + feelings + ". Please always remember "+ encouragement + "! Hope you feel better :)"

  print()
  print(output)
  print()
