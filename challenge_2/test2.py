import firebase_admin
from firebase_admin import credentials, firestore, db

# Initialize Firebase Admin SDK
def initialize_firebase():
    # Path to your service account key JSON file
    service_account_path = "database1.json"
    
    # Initialize Firebase Admin
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred, {
        'databaseURL': 'https://database1-517fc-default-rtdb.firebaseio.com/',  # Replace with your Firebase Database URL
    })
    print("Firebase initialized successfully.")
    
    





# Save data to Realtime Database
def save_data_realtime_db(reference_path, data):
    try:
        ref = db.reference(reference_path)
        ref.set(data)
        print(f"Data saved to Realtime Database: {reference_path}")
    except Exception as e:
        print(f"Error saving to Realtime Database: {e}")
        
        
        
        

# Fetch data from Realtime Database
def fetch_data_realtime_db(reference_path):
    try:
        ref = db.reference(reference_path)
        data = ref.get()
        print(f"Data fetched from Realtime Database: {data}")
        return data
    except Exception as e:
        print(f"Error fetching from Realtime Database: {e}")
        
        

def store_data(item,Quantity): 
    ing_name=item
    ing_quantity=Quantity
    save_data_realtime_db("Data/ingredients/"+str(ing_name), ing_quantity)
    
    
def Fetch_data(item):
    fetched_realtime_db_data = fetch_data_realtime_db("Data/ingredients")
    return fetched_realtime_db_data[item]
    

def Fetch_dataframe():
    fetched_realtime_db_data = fetch_data_realtime_db("Data/ingredients")
    return fetched_realtime_db_data;
    
        

# Main function to demonstrate usage
if __name__ == "__main__":
    initialize_firebase()

    # Realtime Database Example
    ing_name="Potato"
    ing_quantity=69
    store_data(ing_name,ing_quantity)
    
    
    ing_name="Tomato"
    ing_quantity=15
    store_data(ing_name,ing_quantity)
    
    
    
    
    total=Fetch_data("Potato")
    print(total)
    
    dataframe=Fetch_dataframe()
    print(dataframe)

