from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.subscription import Subscription
from project.trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    @staticmethod
    def add(obj, collection):
        if obj not in collection:
            collection.append(obj)

    @staticmethod
    def find_object(obj_id, collection, param):
        return list(filter(lambda x: getattr(x, param, None) == obj_id, collection))[0]

    def add_customer(self, customer: Customer):
        self.add(customer, self.customers)

    def add_trainer(self, trainer: Trainer):
        self.add(trainer, self.trainers)

    def add_equipment(self, equipment: Equipment):
        self.add(equipment, self.equipment)

    def add_plan(self, plan: ExercisePlan):
        self.add(plan, self.plans)

    def add_subscription(self, subscription: Subscription):
        self.add(subscription, self.subscriptions)

    def subscription_info(self, subscription_id: int):
        sub = self.find_object(subscription_id, self.subscriptions, 'id')
        customer = self.find_object(sub.customer_id, self.customers, 'id')
        trainer = self.find_object(sub.trainer_id, self.trainers, 'id')
        plan = self.find_object(trainer.id, self.plans, 'trainer_id')
        equipment = self.find_object(plan.equipment_id, self.equipment, 'id')
        info = (sub, customer, trainer, equipment, plan)
        return '\n'.join(map(str, info))
