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
		all_users=storage.load_users()
		username=input("✒️ Choose your username: ")
		if username in all_users:
			print("⚠️ This name is already etched in our records.")
			print("Please try another identity.")
			return None
		password =input("🔐 Choose your Password: ")
		all_users[username]={"password":password}
		storage.save_users(all_users)
		print("✅ Registration Successful. Welcome to the Jamia family.")
		return user(username,password)
	@staticmethod
	def login():
		all_users=storage.load_users()
		username=input("👤 Username: ")
		password =input("🔑 Password: ")
		if username not in all_users or all_users[username]["password"]!=password:
			print("❌ The gates remain closed; invalid credentials.")
			print("Try once more, friend.")
			return None
		print(f"\n☀️ Welcome Back to your alma mater, {username}")
		return user(username,password)
	def save(self):
		all_users=storage.load_users()
		all_users[self.username]={"password":self.password}
		storage.save_users(all_users)

def jamia_darshan():
	current_dir=os.path.dirname(os.path.abspath(__file__))
	env_path=os.path.join(current_dir,'.env')
	load_dotenv(dotenv_path=env_path)
	api_key=os.getenv("GEMINI_API_KEY")
	client =genai.Client(api_key=api_key)
	sys_instruct = '''You are "JAMIA DARSHAN", a wise and soulful observer of Jamia Millia Islamia...''' # (Persona text remains same)
	config=types.GenerateContentConfig(
	system_instruction=sys_instruct,
	temperature=0.7,
	top_p=0.95,
	max_output_tokens=500,)
	chat=client.chats.create(model="gemini-2.5-flash",config=config)
	print("\n📜 Jamia Darshan is listening. Let us talk of history, stones, and dreams.")
	while True:
		user_input=input("\nYou (type 'quit' to return to the courtyard): ").strip()
		if user_input.lower() in ['quit','exit']:
			break
		else:
			response=chat.send_message(user_input)
			print(f"\n🏛️ Jamia Darshan: {response.text}")

def view_attendence():
	user_sem=int(input("📖 Enter your current Semester (1-2): "))
	if user_sem==1:
		subjects = ["Physics", "Chemistry", "Maths", "Communication", "Constitution", "Civil", "Mech"]
		marks = [random.randint(65,90) for _ in subjects]
		avg_attendence=sum(marks)/len(marks)
		
		print("\n--- 🏫 Semester 1 Attendance Ledger ---")
		for sub, m in zip(subjects, marks):
			print(f"📍 {sub}: {m}%")
		
		print(f"\n📊 Aggregate Presence: {avg_attendence:.2f}%")
		if avg_attendence>=75:
			print("🔥 You have walked the lanes well. Applicable for End semester exams.")
		else:
			print("😔 The hallways missed you too often. Not applicable for exams.")
	elif user_sem==2:
		subjects = ["Physics", "Maths", "Biology", "Env", "Electrical", "ECE", "Computer"]
		marks = [random.randint(65,90) for _ in subjects]
		avg_attendence=sum(marks)/len(marks)

		print("\n--- 🏫 Semester 2 Attendance Ledger ---")
		for sub, m in zip(subjects, marks):
			print(f"📍 {sub}: {m}%")

		print(f"\n📊 Aggregate Presence: {avg_attendence:.2f}%")
		if avg_attendence>=75:
			print("🔥 Your dedication honors the founders. Applicable for End semester exams.")
		else:
			print("😔 A bridge needs every stone; your attendance is lacking. Not applicable.")
	else:
		print("❌ Please enter a valid 1st year Semester.")
		view_attendence()
	dashboard()

def contact_us():
	print("\n--- 📞 Connect with the Faculty ---")
	print("🏷️ Dean (FET): Prof. Mohammad Sharif")
	print("📌 Heart of the Campus: Jamia Nagar, New Delhi - 110025")
	print("📞 Voice of Jamia (EPABX): +91 (11) 2698 1717")
	print("🧑‍💻 Digital Gateway: www.jmi.ac.in")
	dashboard()

def view_results():
	user_sem=int(input("📜 Enter Semester to view your journey (1-2): "))
	if user_sem==1:
		subjects = ["Physics", "Chemistry", "Maths", "Communication", "Constitution", "Civil", "Mech"]
		marks = [random.randint(30,100) for _ in subjects]
		avg_marks=sum(marks)/len(marks)

		print("\n--- 🎓 Semester 1 Academic Record ---")
		for sub, m in zip(subjects, marks):
			print(f"📝 {sub}: {m}")

		print(f"\n⚖️ Scholarly Average: {avg_marks:.2f}")
		if avg_marks>=40:
			print("✨ Congratulations! You have carried the torch forward. Passed. 🔥")
		else:
			print("🕯️ The path is steep. You must strive harder next time. Failed. 😔")
	elif user_sem==2:
		subjects = ["Physics", "Maths", "Biology", "Env", "Electrical", "ECE", "Computer"]
		marks = [random.randint(30,100) for _ in subjects]
		avg_marks=sum(marks)/len(marks)

		print("\n--- 🎓 Semester 2 Academic Record ---")
		for sub, m in zip(subjects, marks):
			print(f"📝 {sub}: {m}")

		print(f"\n⚖️ Scholarly Average: {avg_marks:.2f}")
		if avg_marks>=40:
			print("✨ Well done! Your hard work bears fruit. Passed. 🔥")
		else:
			print("🕯️ Knowledge requires patience and persistence. Failed. 😔")
	else:
		print("❌ This archive only holds 1st year records.")
		view_results()
	dashboard()

def exit_program():
	print("\n🚶 Departing the campus...")
	print("May the Jamia Tehzeeb stay with you. Khuda Hafiz. ❤️")

def dashboard():
	print("\n--- 💠 THE JAMIA DARSHAN DASHBOARD ---")
	print("1. 🏫 View My Attendance")
	print("2. 📜 View My Results")
	print("3. 📞 Contact the Faculty")
	print("4. 🏛️ Enter Jamia Darshan (Chat)")
	print("5. 🚪 Leave Dashboard")
	user_choice=input("\nWhere shall we go? (1-5): ")
	if user_choice=="1":
		view_attendence()
	elif user_choice=="2":
		view_results()
	elif user_choice=="3":
		contact_us()
	elif user_choice=="4":
		jamia_darshan()
		dashboard()
	elif user_choice=="5":
		exit_program()
	else:
		print("⚠️ An unknown path. Please choose 1 through 5.")
		dashboard()

def main():
	print("\n--- 🎊 Welcome to the Gateway of Jamia ---")
	print("1. ✒️ Register New Student\n2. 🔑 Student Login\n3. 🚪 Exit")
	choice=input("\nSelect your path: ")
	active_user=None
	if choice=="1":
		active_user=user.register()
	elif choice=="2":
		active_user=user.login()
	elif choice=="3":
		print("👋 Until we meet again.")
		return
	else:
		print("❌ That choice is not in our books.")
		main()
		return 
	if active_user:
		dashboard()
	else:
		main()

if __name__=='__main__':
	main()
