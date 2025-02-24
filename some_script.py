from demo1.models.user import User
from demo1.database import engine
from demo1.database import engine, Session

def main():
    session = Session()
    
    # Add a new user
    new_user = User(email_address='ani1301997@gmail.com', password='securepassword')
    session.add(new_user)
    session.commit()
    
    # Query the user
    result = session.query(User).filter_by(email_address='ani1301997@gmail.com').first()
    print(result.email_address)
    
    session.close()

if __name__ == "__main__":
    main()