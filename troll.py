import random
import time
import webbrowser


while True:
    pages = random.choice(["trollface.dk", "https://www.youtube.com/watch?v=LPHnO9cUMJM", 
    "https://www.google.com/url?sa=i&url=https%3A%2F%2Ftenor.com%2Fview%2Ftroll-face-smiling-gif-25396270&psig=AOvVaw0-r2VEFqAw1zsrgmrrKy6N&ust=1677861311305000&source=images&cd=vfe&ved=0CA8QjRxqFwoTCPCGrczWvf0CFQAAAAAdAAAAABAR", 
    "https://www.youtube.com/watch?v=1V9xqUX8ftc", 
    "https://www.youtube.com/watch?v=iYGoKb2nsyw", 
    "https://www.youtube.com/watch?v=y2MujPxBJF8", 
    "https://www.youtube.com/watch?v=Ajc_3XCcGrE", 
    "media.giphy.com/media/eVy46EWyclTIA/giphy.gif"]) 
    visit = "https://{}".format(pages)
    webbrowser.open(pages) 
    
    print ("Orbit Siker")

