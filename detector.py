from playsound import playsound

# check if the model's confidence score for the word "like" exceeds the 50% threshold, and plays the sound if it is
if prediction > 0.5:
  print("LIKE DETECTED.") # what more can i say
  playsound('notification.mp3') # plays the mp3 file
