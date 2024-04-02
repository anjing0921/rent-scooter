from app import db

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.VARCHAR(50), nullable=False)
    phone = db.Column(db.VARCHAR(25), nullable=False)
    rentals = db.relationship("Rental", back_populates="customer")
    
    def to_dict(self):
        customer_as_dict = {}
        customer_as_dict["id"] = self.id
        customer_as_dict["name"] = self.name
        customer_as_dict["email"] = self.email
        customer_as_dict["phone"] = self.phone

        return customer_as_dict
    
    @classmethod
    def from_dict(cls, customer_data):
        new_customer = Customer(name=customer_data["name"],
                                email=customer_data["email"],
                                phone=customer_data["phone"],
                        )
        return new_customer
    

