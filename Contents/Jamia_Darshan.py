import json
import random
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
class storage:
	file="users.json"
	@staticmethod
	def load_users():
		if not os.path.exists(storage.file):
			return {}
		with open(storage.file,"r") as f:
			return json.load(f)
	@staticmethod
	def save_users(users_data):
		with open(storage.file,"w") as f:
			json.dump(users_data,f,indent=4)

class user:
	def __init__(self,username,password):
		self.username=username
		self.password=password 
	@staticmethod
	def register():
		#Prompts user for details and saves them if the username is unique.
		all_users=storage.load_users()
		username=input("Choose username : ")
		if username in all_users:
			print("username already exists ")
			print("try again")
			return None
		password =input("Choose Password : ")
		all_users[username]={"password":password}
		storage.save_users(all_users)
		print("✅Registration Successful.")
		return user(username,password)
	@staticmethod
	def login():
		#Checks input credentials against stored data.
		all_users=storage.load_users()
		username=input("username : ")
		password =input("password : ")
		if username not in all_users or all_users[username]["password"]!=password:
			print("❌invalid credentials ")
			print("try again..")
			return None
		print(f"\n☀️Welcome Back , {username}")
		return user(username,password)
	def save(self):
		all_users=storage.load_users()
		all_users[self.username]={"password":self.password}
		storage.save_users(all_users)
def jamia_darshan():
	'''Initializes the Gemini AI Chatbot with a specific Jamia persona.
    It tells the story of the university rather than just giving facts.'''
	current_dir=os.path.dirname(os.path.abspath(__file__))
	env_path=os.path.join(current_dir,'.env')
	load_dotenv(dotenv_path=env_path)
	api_key=os.getenv("GEMINI_API_KEY")
	client =genai.Client(api_key=api_key)
	sys_instruct = '''You are "JAMIA DARSHAN", a wise and soulful observer of Jamia Millia Islamia. 
You don't just provide facts; you tell the 'story' of Jamia as someone who has 
walked its lanes for decades. 

YOUR PERSONA:
- You are deeply respectful of Jamia's history as a 'Swadeshi' university born 
  out of the Khilafat and Non-Cooperation movements in 1920.
- Your tone is academic yet poetic, warm, and welcoming—like a senior professor 
  or a long-time resident of the campus.
- You refer to the founders (Hakim Ajmal Khan, Maulana Mohamed Ali Jauhar, 
  Dr. Zakir Husain) with great reverence.

YOUR KNOWLEDGE BASE:
1. HISTORY: Know the journey from Aligarh (1920) to Karol Bagh (1925) and 
   finally to the Okhla campus (1935 onwards). Mention the sacrifices made to 
   build Jamia 'stone by stone.'
2. LANDMARKS: You know the campus intimately—from the iconic Seven Arched 
   Bridge (Sathpula) and the Ghalib Statue to the quiet corners of Dr. Zakir 
   Husain Library and the vibrant MCRC (Mass Comm) building.
3. CULTURE: You understand the "Jamia Tehzeeb" (culture)—a mix of nationalist 
   fervor, secularism, and a commitment to marginalized sections.
4. MODERN ACHIEVEMENTS: You are proud of its A++ NAAC rating, its 3rd NIRF 
   rank (2023), and its famous alumni like Virender Sehwag or Barkha Dutt.

GUIDELINES:
- If a user asks a basic question, answer it with a touch of storytelling. 
  (e.g., instead of "It was founded in 1920," say "Jamia’s heartbeat first 
  started in 1920 in Aligarh, as a radical act of protest against colonial 
  education.")
- Always stay in character as "JAMIA DARSHAN". 
- Encourage the user to explore both the heritage and the modern academic 
  excellence of the university'''
	config=types.GenerateContentConfig(
	system_instruction=sys_instruct,
	temperature=0.7,
	top_p=0.95,
	max_output_tokens=500,)
	chat=client.chats.create(model="gemini-2.5-flash",config=config)
	while True:
		user_input=input("\nYou(type 'quit' or 'exit' for returning to dashboard) : ").strip()
		if user_input.lower() in ['quit','exit']:
			break
		else:
			response=chat.send_message(user_input)
			print(f"\n🛜Jamia Darshan : {response.text}")
def view_attendence():
	user_sem=int(input("Enter your sem(1-2) : "))
	if user_sem==1:
		phy=random.randint(65,90)
		chem=random.randint(65,90)
		maths=random.randint(65,90)
		comms=random.randint(65,90)
		constitution=random.randint(65,90)
		civil=random.randint(65,90)
		mech=random.randint(65,90)
		avg_attendence=(phy+chem+maths+comms+constitution+civil+mech)/7
		print(f"Attendance in Physics is : {phy}%")
		print(f"Attendance in Chemistry is : {chem}%")
		print(f"Attendance in Maths is : {maths}%")
		print(f"Attendance in Communicationn is : {comms}%")
		print(f"Attendance in Constitution is : {constitution}%")
		print(f"Attendance in Civil is : {civil}%")
		print(f"Attendance in Mech is : {mech}%")
		print(f"Avg Attendance : {avg_attendence}%")
		if avg_attendence>=75:
			print("Applicable for End semester exam🔥")
		else:
			print("Not aaplicable for end semester exam😔")
	elif user_sem==2:
		phy=random.randint(65,90)
		maths=random.randint(65,90)
		biology=random.randint(65,90)
		Env=random.randint(65,90)
		Elec=random.randint(65,90)
		Ece=random.randint(65,90)
		Computer=random.randint(65,90)
		avg_attendence=(phy+maths+biology+Env+Elec+Ece+Computer)/7
		print(f"Attendance in Physics is : {phy}%")
		print(f"Attendance in Maths is : {maths}%")
		print(f"Attendance in Biology is : {biology}%")
		print(f"Attendance in Evn is : {Env}%")
		print(f"Attendance in Electrical is : {Elec}%")
		print(f"Attendance in ECE is : {Ece}%")
		print(f"Attendance in Computer is : {Computer}%")
		print(f"Avg Attendance is : {avg_attendence}%")
		if avg_attendence>=75:
			print("Applicable for End semester exam🔥")
		else:
			print("Not aaplicable for end semester exam😔")
	else:
		print("❌Enter only 1st year Semester ")
		print("\nTry Again...")
		view_attendence()
	dashboard()
def contact_us():
	#Provides official contact information for the Faculty of Engineering.
	print("🏷️Name of Dean(FET) : Prof Mohammad Sharif")
	print("📌Address: Jamia Millia Islamia, Jamia Nagar, New Delhi - 110025, India.")
	print("📞Main EPABX (Switchboard): +91 (11) 2698 1717 / 2698 4617 / 2698 4658")
	print("🧑‍💻For more information visit our site ,Official Website: www.jmi.ac.in")
	dashboard()
def view_results():
	user_sem=int(input("Enter your sem(1-2) : "))
	if user_sem==1:
		phy=random.randint(0,100)
		chem=random.randint(0,100)
		maths=random.randint(0,100)
		comms=random.randint(0,100)
		constitution=random.randint(0,100)
		civil=random.randint(0,100)
		mech=random.randint(0,100)
		avg_marks=(phy+chem+maths+comms+constitution+civil+mech)/7
		print(f"Marks in Physics  : {phy}")
		print(f"Marks in Chemistry : {chem}")
		print(f"Marks in Maths  : {maths}")
		print(f"Marks in Communication  : {comms}")
		print(f"Marks in Constitution  : {constitution}")
		print(f"Marks in Civil  : {civil}")
		print(f"Marks in Mechanical  : {mech}")
		print(f"Average Marks  : {avg_marks}")
		if avg_marks>=40:
			print("Congratulations You are Passed🔥")
		else:
			print("Failed😔")
	elif user_sem==2:
		phy=random.randint(0,100)
		maths=random.randint(0,100)
		biology=random.randint(0,100)
		env=random.randint(0,100)
		elec=random.randint(0,100)
		ece=random.randint(0,100)
		computer=random.randint(0,100)
		avg_marks=(phy+maths+biology+env+elec+ece+computer)/7
		print(f"Marks in Physics  : {phy}")
		print(f"Marks in Maths : {maths}")
		print(f"Marks in Biology : {biology}")
		print(f"Marks in Env  : {env}")
		print(f"Marks in Electrical  : {elec}")
		print(f"Marks in Ece : {ece}")
		print(f"Marks in Computer  : {computer}")
		print(f"Average Marks  : {avg_marks}")
		if avg_marks>=40:
			print("\nCongratulations You are Passed🔥")
		else:
			print("\nFailed😔")
	else:
		print("❌Enter only 1st year Semester ")
		print("\nTry Again...")
		view_results()
	dashboard()
def exit_program():
	print("Exiting...")
	print("Thanks for using Jamia Dashboard❤️")
def dashboard():
	#Main navigation menu after successful login.
	print("\n---💠JAMIA CLI DASHBOARD ---")
	print("1.View Attendance ")
	print("2.View Result")
	print("3.Contact Us")
	print("4.Jamia Darshan(Chatbot)")
	print("5.Exit")
	user_choice=input("Choose option(1-5): ")
	if user_choice=="1":
		view_attendence()
	elif user_choice=="2":
		view_results()
	elif user_choice=="3":
		contact_us()
	elif user_choice=="4":
		jamia_darshan()
		dashboard()# Return to dashboard after chat
	elif user_choice=="5":
		exit_program()
	else:
		print("❌Wrong option...")
		print("try again...")
		dashboard()
def main():
	#The starting point of the application for registration and login.
	print("---🎊Welcome---")
	print("\n1.Register\n2.Login\n3.Exit")
	choice=input("Select option : ")
	active_user=None
	if choice=="1":
		active_user=user.register()
	elif choice=="2":
		active_user=user.login()
	elif choice=="3":
		print("👋Bye..")
		return
	else:
		print("❌invalid choice")
		print("try again...")
		main()
		return 
	if active_user:
		dashboard()
	else:
		main()
if __name__=='__main__':
	main()
