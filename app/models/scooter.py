from app import db

class Scooter(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    model = db.Column(db.String,  nullable=False)
    charge_percent = db.Column(db.Float,  nullable=False)
    rentals = db.relationship("Rental", back_populates="scooter")

    def to_dict(self):
        scooter_dict = {}
        scooter_dict["id"] = self.id
        scooter_dict["model"] = self.model
        scooter_dict["charge_percent"] = self.charge_percent
        return scooter_dict
    
    @classmethod
    def from_dict(cls, scooter_data):
        new_scooter = Scooter(model= scooter_data["model"],
                    charge_percent = scooter_data["charge_percent"]
                            )
        return new_scooter

