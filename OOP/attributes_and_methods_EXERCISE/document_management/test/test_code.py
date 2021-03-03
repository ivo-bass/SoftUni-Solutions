# from project.category import Category
# from project.document import Document
# from project.storage import Storage
# from project.topic import Topic

from OOP.attributes_and_methods_EXERCISE.document_management.project.category import Category
from OOP.attributes_and_methods_EXERCISE.document_management.project.document import Document
from OOP.attributes_and_methods_EXERCISE.document_management.project.storage import Storage
from OOP.attributes_and_methods_EXERCISE.document_management.project.topic import Topic

c1 = Category(1, "work")
t1 = Topic(1, "daily tasks", "C:\\work_documents")
d1 = Document(1, 1, 1, "finilize project")

d1.add_tag("urgent")
d1.add_tag("work")

storage = Storage()
storage.add_category(c1)
storage.add_topic(t1)
storage.add_document(d1)

print(c1)
print(t1)
print(storage.get_document(1))
print(storage)
