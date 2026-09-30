class Delivery:
    def __init__(self, order_id, destination):
        self.order_id = order_id
        self.destination = destination
    def deliver(self):
        print("Delivery is being processed")
class Trackable:
    def track(self):
        print("Tracking Delivery")
class StandardDelivery(Delivery):
    def deliver(self):
        print(f"Order {self.order_id} will arrive in 3-5 days.")
class ExpressDelivery(Delivery, Trackable):
    def deliver(self):
        print(f"Order {self.order_id} will arrive within 24 hours.")
    def track(self):
        print(f"Tracking Order {self.order_id}....")
standard = StandardDelivery("D101", "Bangkok")
express = ExpressDelivery("D102", "Chiang Mai")
deliveries = [standard, express]
for delivery in deliveries:
    delivery.deliver()
express.track()