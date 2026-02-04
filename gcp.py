import time

def slow(text):
    for c in text:
        print(c, end="", flush=True)
        time.sleep(0.03)
    print()

print("\033[96m")
slow("===================================")
slow("   🚀 WELCOME TO GOOGLE CLOUD 🚀   ")
slow("===================================")
print("\033[0m")

slow("Initializing Cloud Shell...")
time.sleep(1)
slow("Loading Python environment...")
time.sleep(1)
slow("Connected to project: cloudcomputing12")
time.sleep(1)

print("\n🎉 You are ready to build on GCP!")
