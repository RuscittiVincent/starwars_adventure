scenes = {
    "description": "You are on a mission to deliver plans to a rebel base. You land on Tatooene and mus find a guide.",
    "choices":["Look for Obi-Wan", "Head to the cantina"], 
"results": ["obiwan", "cantina"] 
},
 "obiwan": { 
    "description": "You find Obi-Wan Kenobi. He agrees to help you.",
    "choices": ["Travel to the Rebel base", "Return to your ship"], 
    "results": ["win", "lose"]
},
"cantina": {
    "description": "In the cantina, you encounter some unsavory types.", 
    "choices": ["Talk to the band", "Sit quietly in a corner"], 
    "results": ["band", "corner"]
},
"band": {
    "description": "The band knows someone who can help. You meet Han Solo.", 
    "choices": ["Hire Han" "Decline his offer"].
    "results": ["win", "Lose"] 
	},
"corner": {
    "description": "You are noticed and questioned by Stormtroopers.",
    "choices": ["Fight" "Flee"],
    "results": ["lose", "Lose"] 
},
"win" :
    “description”: "You successfully make it to the Rebel base. The galaxy is in your debt!", 
    “choices”: [],
    “results”: []
},
"lose": {
    "description": "You failed your mission. The galaxy is doomed!", 
    "Choices":[]
    "Results": []
}
def display_scene(scene):
    print (scenes [scene] ["description" ]) 
    for idx, choice in enumerate(scenes[scene] ["choices"], start=1):  
        print (f" {idx}. {choice}") 

def get_choice(scene): 
   choice = int(input ("What will you do? (Enter a number): ")) - 1 
   if 0 <= choice < len(scenes[scene] ["results"]): 
        return scenes [scene]["results"] [choice] 
   else: 
        print("Invalid choice. Try again.") 
        return get_choice(scene)   
   

def main() : 
    current_scene = "start" 
    while current_scene not in ["win", "lose"]: 
            display_scene(current_scene) 
            current_scene = get_choice (current_scene) 
        display-scene (current_scene)) main() 