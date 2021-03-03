import unittest


from project.customer import Customer
from project.equipment import Equipment
from project.exercise_plan import ExercisePlan
from project.gym import Gym
from project.subscription import Subscription
from project.trainer import Trainer


class TestGym(unittest.TestCase):
    def test_customer_init(self):
        Customer.id = 1
        c = Customer("Pesho", "addr.", "pesho@gmail.com")
        self.assertEqual(c.id, 1)
        self.assertEqual(c.name, "Pesho")
        self.assertEqual(c.address, "addr.")
        self.assertEqual(c.email, "pesho@gmail.com")

    def test_customer_repr(self):
        Customer.id = 1
        c = Customer("Pesho", "addr.", "pesho@gmail.com")
        self.assertEqual(str(c), "Customer <1> Pesho; Address: addr.; Email: pesho@gmail.com")

    def test_equipment_init(self):
        Equipment.id = 1
        e = Equipment("Pesho")
        self.assertEqual(e.id, 1)
        self.assertEqual(e.name, "Pesho")

    def test_equipment_repr(self):
        Equipment.id = 1
        e = Equipment("Pesho")
        self.assertEqual(str(e), "Equipment <1> Pesho")

    def test_trainer_init(self):
        Trainer.id = 1
        t = Trainer("Pesho")
        self.assertEqual(t.id, 1)
        self.assertEqual(t.name, "Pesho")

    def test_trainer_repr(self):
        Trainer.id = 1
        t = Trainer("Pesho")
        self.assertEqual(str(t), "Trainer <1> Pesho")

    def test_subscription_init(self):
        Subscription.id = 1
        s = Subscription("20.02.2020", 1, 1, 1)
        self.assertEqual(s.id, 1)
        self.assertEqual(s.date, "20.02.2020")
        self.assertEqual(s.customer_id, 1)
        self.assertEqual(s.trainer_id, 1)
        self.assertEqual(s.exercise_id, 1)

    def test_plan_init(self):
        ExercisePlan.id = 1
        p = ExercisePlan(1, 1, 10)
        self.assertEqual(p.id, 1)
        self.assertEqual(p.trainer_id, 1)
        self.assertEqual(p.equipment_id, 1)
        self.assertEqual(p.duration, 10)

    def test_plan_from_hours(self):
        ExercisePlan.id = 1
        p = ExercisePlan.from_hours(1, 1, 16)
        self.assertEqual(p.id, 1)
        self.assertEqual(p.trainer_id, 1)
        self.assertEqual(p.equipment_id, 1)
        self.assertEqual(p.duration, 960)

    def test_plan_repr(self):
        ExercisePlan.id = 1
        p = ExercisePlan(1, 1, 15)
        self.assertEqual(str(p), "Plan <1> with duration 15 minutes")

    def test_gym_init(self):
        g = Gym()
        self.assertEqual(g.customers, [])
        self.assertEqual(g.trainers, [])
        self.assertEqual(g.equipment, [])
        self.assertEqual(g.plans, [])
        self.assertEqual(g.subscriptions, [])

    def test_gym_add_customer(self):
        Gym.id = 1
        g = Gym()
        c = Customer("Pesho", "addr.", "pesho@gmail.com")
        g.add_customer(c)
        g.add_customer(c)
        self.assertEqual(g.customers, [c])

    def test_gym_add_trainer(self):
        g = Gym()
        t = Trainer("Pesho")
        g.add_trainer(t)
        g.add_trainer(t)
        self.assertEqual(g.trainers, [t])

    def test_gym_add_equipment(self):
        g = Gym()
        e = Equipment("Pesho")
        g.add_equipment(e)
        g.add_equipment(e)
        self.assertEqual(g.equipment, [e])

    def test_gym_add_plan(self):
        g = Gym()
        p = ExercisePlan(1, 1, 10)
        g.add_plan(p)
        g.add_plan(p)
        self.assertEqual(g.plans, [p])

    def test_gym_add_subscription(self):
        g = Gym()
        s = Subscription("10.02.2020", 1, 1, 1)
        g.add_subscription(s)
        g.add_subscription(s)
        self.assertEqual(g.subscriptions, [s])

    def test_gym_subscription_info(self):
        Gym.id = 1
        Subscription.id = 1
        ExercisePlan.id = 1
        Equipment.id = 1
        Trainer.id = 1
        Customer.id = 1
        g = Gym()
        s = Subscription("10.02.2020", 1, 1, 1)
        p = ExercisePlan(1, 1, 10)
        e = Equipment("Pesho")
        t = Trainer("Pesho")
        c = Customer("Pesho", "addr.", "pesho@gmail.com")
        g.add_subscription(s)
        g.add_customer(c)
        g.add_equipment(e)
        g.add_plan(p)
        g.add_trainer(t)
        self.assertEqual(g.subscription_info(1),
                         "Subscription <1> on 10.02.2020\nCustomer <1> Pesho; Address: addr.; Email: pesho@gmail.com\nTrainer <1> Pesho\nEquipment <1> Pesho\nPlan <1> with duration 10 minutes")

    def test_customer_static_method(self):
        Customer.id = 1
        self.assertEqual(Customer.get_next_id(), 1)

    def test_equipment_static_method(self):
        Equipment.id = 1
        self.assertEqual(Equipment.get_next_id(), 1)

    def test_trainer_static_method(self):
        Trainer.id = 1
        self.assertEqual(Trainer.get_next_id(), 1)

    def test_subscription_static_method(self):
        Subscription.id = 1
        self.assertEqual(Subscription.get_next_id(), 1)

    def test_plan_static_method(self):
        ExercisePlan.id = 1
        self.assertEqual(ExercisePlan.get_next_id(), 1)


if __name__ == "__main__":
    unittest.main()
