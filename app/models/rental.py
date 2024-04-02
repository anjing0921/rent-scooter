from app import db

class Rental(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    is_returned = db.Column(db.Boolean,  default = False, nullable=False)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    customer = db.relationship("Customer", back_populates="rentals")
    scooter_id = db.Column(db.Integer, db.ForeignKey('scooter.id'), nullable=False)
    scooter = db.relationship("Scooter", back_populates="rentals")

    def to_dict(self):
        rental_dict = {}
        rental_dict["id"] = self.id
        rental_dict["customer_id"] = self.customer_id
        rental_dict["scooter_id"] = self.scooter_id
        rental_dict["is_returned"] = self.is_returned
        return rental_dict
    
    @classmethod
    def from_dict(cls, rental_data):
        new_rental = Rental(
            customer_id = rental_data["customer_id"],
            scooter_id = rental_data["scooter_id"]
        )
        return new_rental