(4/29/26 @8:03PM) Hello Mr. Thomas, I unfortunately procrastinated my project by a bit.. Here marks the beginning of Sprint 2..!

WHAT IS THIS PROJECT:
Essentially, I want to get better at public speaking and talking to others in general, but I find myself often using a lot of filler words such as like. SPECIFICALLY "like". I would like to make some piece of software to detect when a user says "like" to then emit a loud buzz sound so the user can catch themselves and restructure their sentence. 

For this project, I used a Raspberry Pi Zero W, USB Mic, a PirateAudio audio board that has a small display and speaker, and an external battery. I even soldered all the pins in myself ;), I've soldered a few times before but this was the first time I could say I was proud of my work. See pictures:

<img width="1920" height="1440" alt="1" src="https://github.com/user-attachments/assets/b2ba6e0f-120e-4209-8ed9-e01870877c42" />

<img width="1920" height="1440" alt="2" src="https://github.com/user-attachments/assets/2e185702-cb42-4951-a3c4-b71f3594758e" />

This was supposed to allow me to connect to my home server where the software was hosted (too weak to run on the Zero W), however I could not get the Pi to communicate with my computer. I was able to SSH into it from my Mac, but nothing on the Pi, so the idea was scrapped for another time.
...Which is unfortunate cause this is what I spent a lot of my time on, even though the project didn't NEED it, I thought it would be cool. 

The next step is to get openWakeWord working. The way it works is you spell out the word you want it to detect (like) and it trains a bunch of models on the pronounciation. I had to spell it like "laiik" to get it to sound right for training. Here's what the generater looked like:
<img width="1031" height="533" alt="image" src="https://github.com/user-attachments/assets/bad95d36-5c82-4991-b8bd-ce8024d1cd2d" />

Then you need to download the data:
<img width="1025" height="682" alt="image" src="https://github.com/user-attachments/assets/4a9c5401-6640-49bb-88b2-57a7c59ba901" />

(8:56 PM) As of writing, it keeps crashing. I don't know why. I'm restarting it. Again.

(9:07 PM) It seems stable now. The downloads already done too (yay).

(9:10 PM) It's now training the model:
<img width="874" height="428" alt="image" src="https://github.com/user-attachments/assets/1d21b00a-a187-43c5-8c49-3ecbd5343c55" />

(9:25 PM) While it's training I was looking into how I can get my sound to play when it detects the wake word, and it looks like we will be using whats called "playsound" 

(9:59 PM) IT WORKS!!! Albeit a littttttle finicky. It has trouble detecting the "like", most likely due to it not having enough training, and it did sound a little wierd when I spelled out "laiik". It was the best I could get for it to sound like the word as "like" wasn't sounding right. I am proud I got this working for now though.
