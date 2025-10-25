 
from songLogic import uploadMedia , play , play_music , pause_music, stop_music , displaySongList,unpause_music
print("Welcome to music library ")
print("************************")

while True:
     print("Enter number \n1. upload music \n2. display list \n3.choose song to play  \n0  Exit")
 
     choice = int(input("Enter a number: "))
     if choice ==0:
        break
     if choice == 1:
         
           print("*************") 
           print("Upload new song")
           print("*************")
           dir_input = input("enter directory name = ")
           source_path = input("Enter file path \n")
           uploadMedia(dir_input=dir_input, source_path=source_path)
           

           
     if choice == 2:
        print("Displaying list")
        print("***************")
        for i in displaySongList():
          print(i)
        
          
     if choice == 3:
        flag = True
        print("To play a music enter a number")
        print("******************")
        i = int(input("Enter a number: "))
        print("press 1 to pause")
        print("press 2 to replay")
        print("press 3 to stop")
        play(i=i)
        
        while flag == True: 
         ask = int(input("Enter a number: "))
         if ask == 1:
           pause_music()
       
         if ask ==2:
           unpause_music()
           
         if ask == 3:
             stop_music()
             break
        
           
        
             
        
             
         
              


        
           
           
              
       

    



        # song_path = dir_name + "/" + song_list[0] # Replace with the actual path to your song file
        # print(song_list,song_path)
        # play_music(song_path)

        # # Simulate user interaction
        #  time.sleep(5) # Play for 5 seconds
        # pause_music()
        # time.sleep(3) # Pause for 3 seconds
        # unpause_music()
        # time.sleep(5) # Play for another 5 seconds
        # stop_music()



"""
 module 
 upload 
 view 
 play(input)
  pause,replay , stop 
  new song
  exit 
  


  add new album(create folder with 1 song)
  view album
  select album and disply song
  play song--


 """